from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json
import re

from markdown_it import MarkdownIt

SOURCE = Path('source/thesisproposalTuan.md')
PARSER = MarkdownIt('commonmark').enable('table')
MATH = []
STATS = Counter()
REFERENCES = {}


def escape(text):
    substitutions = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}', '−': r'\ensuremath{-}'}
    return ''.join(substitutions.get(character, character) for character in text)


def protect_math(text):
    def save(match):
        index = len(MATH)
        MATH.append(match.group())
        return f'ZZMATH{index}ZZ'
    return re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)', save, text, flags=re.S)


def breakable(text):
    parts = re.split(r'(\S{18,})', text)
    return ''.join(r'\allowbreak{}'.join(escape(piece) for piece in re.findall(r'.{1,8}', part)) if len(part) >= 18 and not any(character.isspace() for character in part) else escape(part).replace('+', r'+\allowbreak{}').replace('/', r'/\allowbreak{}').replace(r'\_', r'\_\allowbreak{}') for part in parts)


def plain(text):
    parts = re.split(r'(ZZMATH\d+ZZ|\[[^\[\]\n]+, \d{4}\])', text)
    result = []
    for part in parts:
        match = re.fullmatch(r'ZZMATH(\d+)ZZ', part)
        if match:
            result.append(MATH[int(match.group(1))])
            STATS['math_expressions'] += 1
        elif part[1:-1] in REFERENCES and part.startswith('['):
            result.append(r'\hyperlink{reference-' + REFERENCES[part[1:-1]] + '}{' + escape(part) + '}')
        else:
            result.append(breakable(part))
    return ''.join(result)


def inline(tokens):
    result = []
    for token in tokens or []:
        if token.type == 'text':
            result.append(plain(token.content))
        elif token.type == 'code_inline':
            pieces = re.findall(r'.{1,8}', token.content)
            result.append(r'\texttt{' + r'\allowbreak{}'.join(escape(piece) for piece in pieces) + '}')
        elif token.type in ('softbreak', 'hardbreak'):
            result.append(' ' if token.type == 'softbreak' else '\\\\\n')
        elif token.type in ('strong_open', 'em_open'):
            result.append(r'\textbf{' if token.type == 'strong_open' else r'\emph{')
        elif token.type in ('strong_close', 'em_close', 'link_close'):
            result.append('}')
        elif token.type == 'link_open':
            address = token.attrGet('href')
            if address.startswith('#'):
                result.append(r'\hyperlink{' + escape(address[1:]) + '}{')
            else:
                result.append(r'\href{' + address.replace('%', r'\%').replace('#', r'\#') + '}{')
        else:
            raise ValueError(f'Unsupported inline token: {token.type}')
    return ''.join(result)


def inline_text(text):
    return inline(PARSER.parseInline(protect_math(text))[0].children)


def diagram(content, caption):
    nodes = {}
    edges = []
    for line in content.splitlines()[1:]:
        for name, label in re.findall(r'([A-Z]+)\[([^\]]+)\]', line):
            nodes[name] = label
        reduced = re.sub(r'\[[^\]]*\]', '', line).strip()
        match = re.fullmatch(r'([A-Z]+)\s*-->\s*([A-Z]+)', reduced)
        if match:
            edges.append(match.groups())
    depths = {name: 0 for name in nodes}
    for unused in range(len(nodes)):
        changed = False
        for origin, destination in edges:
            if depths[destination] <= depths[origin]:
                depths[destination] = depths[origin] + 1
                changed = True
        if not changed:
            break
    groups = defaultdict(list)
    for name in nodes:
        groups[depths[name]].append(name)
    positions = {}
    row = 0
    for depth in sorted(groups):
        names = groups[depth]
        for offset in range(0, len(names), 3):
            batch = names[offset:offset + 3]
            for column, name in enumerate(batch):
                positions[name] = ((column - (len(batch) - 1) / 2) * 5.05, -row * 1.55)
            row += 1
    result = [r'\begin{figure}[p]', r'\centering', r'\begin{tikzpicture}[>=Latex, every node/.style={draw=black!65, rounded corners=2pt, fill=black!3, text width=4.35cm, minimum height=0.85cm, align=center, font=\small}, every path/.style={draw=black!60, thick}]']
    for name, label in nodes.items():
        horizontal, vertical = positions[name]
        result.append(f'\\node ({name}) at ({horizontal:.2f},{vertical:.2f}) {{{escape(label)}}};')
    skipped_edges = 0
    for origin, destination in edges:
        if positions[origin][1] - positions[destination][1] > 1.6:
            side = 'east' if skipped_edges % 2 == 0 else 'west'
            lane = 7.5 if side == 'east' else -7.5
            skipped_edges += 1
            result.append(f'\\draw[->] ({origin}.{side}) -- ({lane},{positions[origin][1]:.2f}) |- ({destination}.{side});')
        else:
            result.append(f'\\draw[->] ({origin}.south) -- ({destination}.north);')
    result.extend([r'\end{tikzpicture}', r'\caption{' + inline_text(caption[2]) + '}', r'\label{fig:' + caption[1] + '}', r'\end{figure}'])
    STATS['figures'] += 1
    return '\n'.join(result)


def table(tokens, caption):
    rows = []
    current = []
    for token in tokens:
        if token.type == 'tr_open':
            current = []
        elif token.type == 'inline':
            current.append((inline(token.children), token.content))
        elif token.type == 'tr_close':
            rows.append(current)
    columns = len(rows[0])
    assert all(len(row) == columns for row in rows)
    max_lengths = [max(len(row[column][1]) for row in rows) for column in range(columns)]
    landscape = columns >= 7 or (columns >= 5 and sum(max_lengths) > 420)
    available = 24.7 if landscape else 16.0
    weights = [min(max(length ** 0.5, 3.5), 17) for length in max_lengths]
    widths = [(available - columns * 0.22) * weight / sum(weights) for weight in weights]
    specification = ''.join(r'>{\raggedright\arraybackslash}p{' + f'{width:.3f}cm' + '}' for width in widths)
    result = [r'\begin{landscape}' if landscape else '', r'\begingroup', r'\footnotesize' if landscape or columns >= 5 else r'\small', r'\setlength{\tabcolsep}{3pt}', r'\renewcommand{\arraystretch}{1.18}', r'\begin{longtable}{' + specification + '}']
    if caption:
        result.extend([r'\caption{' + inline_text(caption[2]) + r'}\label{tab:' + caption[1] + r'}\\'])
    header = ' & '.join(r'\textbf{' + cell[0] + '}' for cell in rows[0]) + r' \\'
    result.extend([r'\toprule', header, r'\midrule', r'\endfirsthead', r'\toprule', header, r'\midrule', r'\endhead', r'\midrule', r'\multicolumn{' + str(columns) + r'}{r}{\footnotesize Continued on next page}\\', r'\endfoot', r'\bottomrule', r'\endlastfoot'])
    for cells in rows[1:]:
        result.append(' & '.join(cell[0] for cell in cells) + r' \\')
    result.append(r'\end{longtable}')
    result.extend([r'\endgroup', r'\end{landscape}' if landscape else ''])
    STATS['tables'] += 1
    STATS['table_cells'] += sum(len(row) for row in rows)
    return '\n'.join(result)


def render(text, front=False):
    tokens = PARSER.parse(protect_math(text))
    result = []
    pending_caption = None
    position = 0
    while position < len(tokens):
        token = tokens[position]
        if token.type == 'heading_open':
            title = tokens[position + 1].content
            level = int(token.tag[1])
            numbering = re.match(r'^([A-G\d]+(?:\.\d+)+)\.?\s+', title)
            if numbering:
                level = numbering.group(1).count('.') + 1
            title = re.sub(r'^(?:Appendix [A-G]\.\s*|(?:\d+|[A-G])(?:\.\d+)*\.?\s+)', '', title)
            command = 'chapter*' if front else {1: 'chapter', 2: 'section', 3: 'subsection', 4: 'subsubsection'}[level]
            formatted = inline_text(title)
            result.append('\\' + command + '{' + formatted + '}')
            if front:
                result.append(r'\addcontentsline{toc}{chapter}{' + formatted + '}')
            else:
                STATS['headings'] += 1
            position += 3
            continue
        if token.type == 'paragraph_open':
            body = tokens[position + 1]
            match = re.match(r'^\*\*(Table|Figure) ([A-G\d]+\.\d+)\. (.+?)\*\*\s*(.*)$', body.content, flags=re.S)
            if match:
                assert pending_caption is None, pending_caption
                pending_caption = match.group(1, 2, 3)
                if match.group(4):
                    result.append(inline_text(match.group(4)) + '\n')
                position += 3
                continue
            result.append('\n')
        elif token.type == 'paragraph_close':
            result.append('\n\n')
        elif token.type == 'inline':
            result.append(inline(token.children))
        elif token.type == 'table_open':
            end = position + 1
            while tokens[end].type != 'table_close':
                end += 1
            assert not pending_caption or pending_caption[0] == 'Table'
            result.append(table(tokens[position:end + 1], pending_caption))
            pending_caption = None
            position = end + 1
            continue
        elif token.type == 'fence':
            if token.info == 'mermaid':
                if pending_caption is None and 'A[Research Question]' in token.content:
                    result.append(r'\input{figures/research_overview}')
                    STATS['figures'] += 1
                else:
                    assert pending_caption and pending_caption[0] == 'Figure'
                    result.append(diagram(token.content, pending_caption))
                pending_caption = None
            else:
                result.append(r'\begin{Verbatim}[fontsize=\footnotesize,breaklines=true,breakanywhere=true]' + '\n' + token.content + r'\end{Verbatim}')
                STATS['code_blocks'] += 1
        elif token.type in ('bullet_list_open', 'ordered_list_open', 'blockquote_open'):
            environment = {'bullet_list_open': 'itemize', 'ordered_list_open': 'enumerate', 'blockquote_open': 'quote'}[token.type]
            result.append(r'\begin{' + environment + '}')
        elif token.type in ('bullet_list_close', 'ordered_list_close', 'blockquote_close'):
            environment = {'bullet_list_close': 'itemize', 'ordered_list_close': 'enumerate', 'blockquote_close': 'quote'}[token.type]
            result.append(r'\end{' + environment + '}')
        elif token.type == 'list_item_open':
            result.append(r'\item ')
        elif token.type != 'list_item_close':
            raise ValueError(f'Unsupported block token: {token.type}')
        position += 1
    assert pending_caption is None, pending_caption
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(result)) + '\n'


def write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


def main():
    if Path('tools/citation-audit.json').exists():
        raise SystemExit(
            'Regeneration is disabled because it would overwrite the reviewed citations. '
            'Edit the LaTeX files directly or preserve the citation revision before '
            'intentionally removing tools/citation-audit.json to regenerate.'
        )
    source = SOURCE.read_text(encoding='utf-8')
    source = source.replace('Here is a shorter version with the RAG introduction kept concise.\n', '')
    source = re.sub(r'(## 1\.6 Scope of the Thesis\s*)## Scope of the Thesis\s*', r'\1', source)
    source = source.replace('The fine-tuning stage adapts the BGE component using development data', 'The fine-tuning stage selects the BGE adaptation recipe on development data, trains on the permitted training folds,')
    source = source.replace('(z_{ij}=s(q_i,d_j)/\tau)', r'\(z_{ij}=s(q_i,d_j)/\tau\)')
    source = source.replace('positive candidate positions (P_i), candidate positions (C_i), and batch size (B)', r'positive candidate positions \(P_i\), candidate positions \(C_i\), and batch size \(B\)')
    malformed = '[\nmathcal L=-\x0crac{1}{B}sum_{i=1}^{B}left[logsum_{jin P_i}exp(z_{ij})-logsum_{jin C_i}exp(z_{ij})\night].\n]'
    repaired = r'\[\mathcal{L}=-\frac{1}{B}\sum_{i=1}^{B}\left[\log\sum_{j\in P_i}\exp(z_{ij})-\log\sum_{j\in C_i}\exp(z_{ij})\right].\]'
    assert malformed in source
    source = source.replace(malformed, repaired)
    source = source.replace(r'P_q(r)=\frac{1}{r}\sum_{j=1}^{r}y_{q,j},\qquad', r'\begin{gathered} P_q(r)=\frac{1}{r}\sum_{j=1}^{r}y_{q,j},\\')
    source = source.replace(r'\mathrm{AP}@10(q)=\frac{\sum_{r=1}^{10}y_{q,r}P_q(r)}{\max(1,\min(|R_q|,10))},\qquad', r'\mathrm{AP}@10(q)=\frac{\sum_{r=1}^{10}y_{q,r}P_q(r)}{\max(1,\min(|R_q|,10))},\\')
    source = source.replace(r'\mathrm{MAP}@10=\frac{1}{|Q|}\sum_{q\in Q}\mathrm{AP}@10(q).', r'\mathrm{MAP}@10=\frac{1}{|Q|}\sum_{q\in Q}\mathrm{AP}@10(q).\end{gathered}')
    references_text = source.split('# References\n', 1)[1].split('# Appendix A.', 1)[0]
    entries = re.findall(r'^- \*\*\[([^\]]+)\]\.\*\* (.+)$', references_text, flags=re.M)
    for index, (author_year, entry) in enumerate(entries, 1):
        REFERENCES[author_year] = str(index)
    bibliography = [r'\chapter*{Bibliography}', r'\addcontentsline{toc}{chapter}{Bibliography}', 'The bibliographic entries and publication-status descriptions below are retained from the supplied manuscript. Its source-check date is 5 September 2026; this document conversion does not constitute a new independent reference audit.\n']
    for author_year, entry in entries:
        bibliography.append(r'\hypertarget{reference-' + REFERENCES[author_year] + r'}{}\noindent\hangindent=1.2em\hangafter=1 ' + r'\textbf{' + escape(author_year) + '.} ' + inline_text(entry) + '\n\\par\\medskip\n')
    write('ref/references.tex', '\n'.join(bibliography))
    STATS['references'] = len(entries)
    front = source.split('# 1. Introduction', 1)[0]
    front_sections = re.split(r'(?m)^## ', front)[1:]
    front_output = []
    for section in front_sections:
        title = section.split('\n', 1)[0]
        if not section.partition('\n')[2].strip():
            continue
        if title in ('Table of Contents', 'List of Figures', 'List of Tables'):
            continue
        front_output.append(render('## ' + section, front=True))
    write('chapters/frontmatter.tex', '\n'.join(front_output))
    section_starts = list(re.finditer(r'(?m)^# (?:[1-6]\. |References$|Appendix [A-G]\. )', source))
    paths = []
    for index, match in enumerate(section_starts):
        end = section_starts[index + 1].start() if index + 1 < len(section_starts) else len(source)
        body = source[match.start():end]
        heading = body.split('\n', 1)[0]
        if heading == '# References':
            continue
        if heading.startswith('# Appendix '):
            letter = heading[len('# Appendix ')]
            path = f'appendices/appendix_{letter.lower()}.tex'
        else:
            number = heading[2]
            path = f'chapters/chapter_{number}.tex'
        write(path, render(body))
        paths.append(path)
    raw_tokens = PARSER.parse(source)
    expected = Counter(token.type for token in raw_tokens)
    assert STATS['tables'] == expected['table_open']
    assert STATS['table_cells'] == expected['td_open'] + expected['th_open']
    assert STATS['figures'] + STATS['code_blocks'] == expected['fence']
    report = {'source': SOURCE.as_posix(), 'synchronized_on': '2026-09-16', 'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(), 'generated_chapters_and_appendices': paths, 'preserved_content_counts': dict(STATS), 'scope': 'Document conversion only; no experiments rerun or external reference audit performed.', 'editorial_repairs': ['Restored corrupted control characters and mathematical delimiters in the supplied multi-positive loss equation and its variable definitions.', 'Split the AP/MAP display across lines without changing its expressions.', 'Normalized Appendix E heading levels to preserve E.1 through E.12 numbering.', 'Omitted duplicate empty headings and an editorial instruction from the source manuscript.', 'Rendered the added research workflow as a grouped native TikZ overview.', 'Clarified development selection versus training folds consistently with the unchanged training protocol.']}
    write('tools/conversion-report.json', json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
