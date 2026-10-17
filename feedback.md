# Góp ý khi chỉnh sửa luận văn

Tài liệu này tổng hợp các góp ý đã trao đổi khi sửa abstract và mục 1.1 của Chapter 1. Dùng để kiểm tra các phần được chỉnh sửa tiếp theo.

## 1. Văn phong và cách viết

- Dùng văn phong khoa học, mạch lạc, rõ ràng, khúc chiết và chặt chẽ.
- Ưu tiên từ ngữ thông dụng, câu trực tiếp và cách diễn đạt cụ thể.
- Hạn chế viết tắt. Khi cần dùng, viết đầy đủ thuật ngữ và đặt chữ viết tắt trong ngoặc ở lần xuất hiện đầu tiên; chỉ dùng dạng viết tắt sau khi đã giới thiệu. Tiêu đề cũng không dùng chữ viết tắt chưa được giải thích. Ví dụ: “term frequency and inverse document frequency (TF-IDF)”.
- Không dùng `--` trong văn bản luận văn, trừ khi không thể tránh được. Ưu tiên viết lại câu, dùng dấu phẩy, dấu hai chấm hoặc diễn đạt quan hệ bằng từ ngữ; tránh dùng dấu gạch ngang thay cho cấu trúc câu rõ ràng.
- Không dùng từ láy, tiếng lóng, từ địa phương, từ lạ hoặc ít được sử dụng; tránh diễn đạt mỹ miều quá mức.
- Mỗi đoạn phát triển một ý chính. Mỗi câu cần có quan hệ rõ với câu trước.
- Câu kết đoạn nên rút ra hệ quả hoặc yêu cầu đánh giá từ lập luận trước đó, thay vì lặp lại các phép so sánh. Có thể dùng “Therefore” khi quan hệ suy luận đã rõ.
- Tách câu dài chứa nhiều mục tiêu, điều kiện hoặc kết quả. Không rút gọn đến mức làm mất điều kiện quan trọng của thí nghiệm.
- Bỏ câu dẫn mang tính tu từ hoặc đánh giá chung không cần thiết, chẳng hạn “generally promising”, “central scientific questions” hoặc “secondary implementation details”.
- Tránh cách nói thiếu chính xác như “beat BM25”, “carry over” hoặc “clearest gain” khi có thể nêu trực tiếp phương pháp so sánh và mức thay đổi.
- Kiểm tra ngữ pháp, chính tả và cấu trúc câu sau khi sửa. Ví dụ, không viết “Retrieval methods includes ... are compared”; có thể tách thành “The evaluated methods are ...” và một câu riêng về metric.

## 2. Thuật ngữ đã thống nhất

| Cách diễn đạt cần thay | Cách diễn đạt ưu tiên |
| --- | --- |
| “improves a lexical BM25 reference”, “strong lexical reference” | Nêu BM25 là baseline và so sánh điểm đánh giá retrieval với baseline đó. Ví dụ: “using BM25's evaluation scores as the baseline”. |
| “legal-domain adaptation” | Nêu trực tiếp việc fine-tuning mô hình embedding. Ví dụ: “fine-tuning the BGE-M3 embedding model”. |
| “two-way hybrid”, “three-way hybrid” | Gọi đúng tên cấu hình: “BM25+BGE-M3” và “BM25+BGE-M3+E5”. |
| “In Study A”, “In Study B” | Mô tả mục tiêu hoặc cách chọn mô hình của từng thí nghiệm ngay trong câu. |
| “corrected evaluation on queries excluded from training and model selection”, “held-out evaluation” | Ưu tiên “evaluation on a separate test set” khi tập này được giữ riêng khỏi huấn luyện và chọn mô hình. |
| “parsed corpus representations” | Nêu nguồn dữ liệu ở dạng raw HTML và bước trích xuất thành văn bản điều luật phục vụ retrieval. |

Các thuật ngữ chuyên môn cần thiết vẫn được sử dụng, nhưng phải có ý nghĩa rõ trong ngữ cảnh. Dùng nhất quán tên BGE-M3 và multilingual-E5-base; có thể viết E5 sau khi đã giới thiệu tên đầy đủ.

## 3. Những ý cần phân biệt rõ

### Baseline và các phép so sánh

- So sánh BM25+BGE-M3 với BM25 để đánh giá cải thiện so với baseline.
- So sánh BM25+BGE-M3+E5 với BM25+BGE-M3 để đánh giá phần cải thiện do thêm E5.
- Không dùng kết quả tốt hơn BM25 để kết luận rằng thêm E5 có ích.
- Phân biệt điểm dùng để xếp hạng tài liệu của BM25 với điểm đánh giá như NDCG@10. Baseline trong phần kết quả là hiệu quả retrieval được đo bằng metric, không phải so sánh trực tiếp các thang điểm thô của những mô hình khác nhau.

### Fine-tuning và hiệu quả hybrid

- Câu hỏi cần trình bày rõ: fine-tuning có cải thiện standalone dense retrieval hay không, và cải thiện đó có được giữ lại khi mô hình được tích hợp vào hybrid hay không.
- Không gộp câu hỏi này với việc kết quả trên development set có được giữ lại trên tập đánh giá hay không.
- Khi bỏ nhãn Study A/Study B, vẫn phải phân biệt thí nghiệm chọn mô hình dựa trên hiệu quả hybrid với thí nghiệm fine-tuning cho standalone dense retrieval.
- Nếu kết quả hybrid được đo khi giữ cố định trọng số fusion, cần nêu điều kiện này khi diễn giải kết quả fine-tuning.

### Raw HTML và văn bản được lập chỉ mục

- “Raw HTML format” mô tả định dạng tài liệu nguồn.
- Khi phương pháp sử dụng văn bản điều luật được trích xuất từ HTML, phải viết rõ bước này; không khiến người đọc hiểu rằng mô hình nhận trực tiếp mã HTML thô.
- Cách viết tham khảo: “article text extracted from legal documents collected in raw HTML format”.
- Khi điều kiện Zalo sử dụng reference text thay thế cho bài trích xuất không có sẵn, giữ thông tin này ở phần phương pháp hoặc nơi cần thiết để giải thích phép so sánh.

### BCA, corpus và ánh xạ

- Giải thích các nhóm câu hỏi thông qua quan hệ dẫn chiếu chung đến tài liệu pháp luật, thay vì chỉ dùng từ “components” mà không có ngữ cảnh.
- Cách viết tham khảo: “For BCA's smaller groups of questions linked by shared legal references, the results do not provide sufficient evidence that adding E5 improves retrieval.”
- Giữ rõ phạm vi nhóm nhỏ nếu kết luận được rút ra từ nhóm này; không tự mở rộng thành kết luận cho toàn bộ BCA.
- Phân biệt điều luật không có trong corpus với lỗi ánh xạ giữa điều luật tham chiếu và định danh tài liệu.
- Điều luật không có trong corpus thì mô hình không thể truy xuất. Lỗi ánh xạ có thể làm sai kết quả đánh giá ngay cả khi nội dung liên quan vẫn có trong corpus.

## 4. Mức độ khẳng định và giới hạn kết luận

- Kết luận phải dựa trên đúng dữ liệu, cấu hình và điều kiện đánh giá đã sử dụng.
- Nêu rõ khi kết quả BCA là tổng hợp mô tả; không mặc nhiên coi đó là bằng chứng thống kê độc lập.
- “Chưa đủ bằng chứng cho thấy có cải thiện” không đồng nghĩa với “đã chứng minh không có tác dụng”.
- Không khẳng định cải thiện phổ quát từ một điều kiện có kết quả tốt.
- Không suy ra tính đúng đắn của câu trả lời pháp lý chỉ từ điểm retrieval cao hơn.
- “Held-out” cho biết tập câu hỏi được giữ riêng khỏi huấn luyện và chọn mô hình; không tự động có nghĩa là tập này chưa từng được xem xét trong phân tích trước đó.
- Giữ các giới hạn post-hoc hoặc việc đã quan sát tập đánh giá khi chúng ảnh hưởng đến mức độ chắc chắn của kết luận.

## 5. Trình tự và kiểm tra khi chỉnh sửa

- Với phần bối cảnh nghiên cứu, trình bày theo trình tự: bối cảnh và nhiệm vụ → khó khăn → phương pháp → vấn đề cần đánh giá.
- Với abstract, trình bày: mục tiêu → dữ liệu và phương pháp → kết quả chính → kết luận và giới hạn cần thiết.
- Giữ nguyên số liệu, trích dẫn và nội dung thí nghiệm khi chỉ chỉnh văn phong, trừ khi đã xác minh được lỗi.
- Giữ thay đổi trong phạm vi mục được yêu cầu; đọc lại nội dung hiện tại trước khi sửa để bảo toàn các chỉnh sửa mới của tác giả.
- Trong chương cơ sở lý thuyết, ưu tiên phương pháp và khái niệm cần để giải thích thí nghiệm thực tế. Bỏ phần giới thiệu phương pháp không sử dụng nếu không cần thiết cho lập luận hoặc phép so sánh; không đưa dynamic mining vào khi thí nghiệm chưa xác nhận có sử dụng.
- Sau khi sửa, kiểm tra lại độ rõ của thuật ngữ, quan hệ giữa các phép so sánh và phạm vi kết luận. Khi kiểm tra bản PDF, xác nhận nội dung mới đã được cập nhật và bố cục còn phù hợp.

## 6. Citation và lập luận về research gap

- Mỗi nhận định về kết quả hoặc giới hạn của nghiên cứu trước phải có citation hỗ trợ đúng nội dung; đặt citation gần nhận định đó.
- Phân biệt phạm vi bằng chứng: legal case retrieval khác Vietnamese statutory article retrieval; kết quả standalone dense retrieval không tự chứng minh hiệu quả của hybrid.
- Trình bày research gap theo trình tự: bằng chứng từ nghiên cứu trước → phạm vi của bằng chứng → câu hỏi cụ thể luận văn cần kiểm chứng → cách đánh giá.
- Không khẳng định “chưa có nghiên cứu nào” nếu chưa có tổng quan đủ để chứng minh. Giới hạn lập luận vào các nguồn đã review và câu hỏi thực nghiệm của luận văn.
- Citation hỗ trợ cơ sở phương pháp, không thay thế kết quả thực nghiệm của luận văn. Với thiết kế và quy trình do luận văn thực hiện, dẫn chiếu đến chương phương pháp khi cần.

## 7. Cấu trúc luận văn và dẫn chiếu

- Đã bỏ mục “Research Questions” vì nội dung trùng với “Research Objectives”. Không khôi phục mục này trong các lần chỉnh sửa sau.
- Không dẫn chiếu đến mục Research Questions hoặc dùng các nhãn RQ1, RQ2, RQ3. Khi cần liên kết nội dung, nêu trực tiếp mục tiêu hoặc phép so sánh trong Research Objectives.
- Research Objectives có bốn mục tiêu, bao gồm cả xây dựng và đánh giá BCA. Không thay “three research questions” bằng “three research objectives” một cách máy móc.
- Khi review Chapter 2 và Chapter 5, sửa các dẫn chiếu RQ còn lại thành mô tả nội dung tương ứng; giữ nguyên kết quả và phạm vi kết luận.
- Sau khi bỏ một mục, kiểm tra lại số thứ tự các mục và các dẫn chiếu viết bằng số cố định.
- Đã bỏ mục riêng “Grouped Evaluation and Statistical Interpretation” trong Chapter 3. Trình bày cách chia nhóm ở Chapter 4 và diễn giải thống kê cạnh kết quả liên quan ở Chapter 5; không khôi phục mục riêng này.
- Chapter 4 dùng tiêu đề “Research Methodology”. Sau Research Design and Retrieval Task, đặt Datasets and Corpus Preparation rồi BCA Dataset Construction, trước System Overview. Giữ BCA Dataset Construction là section riêng.
- Phần BGE-M3 Fine-Tuning có hai subsection song song theo tiêu chí chọn mô hình: hybrid retrieval và standalone dense retrieval. Không đặt một thí nghiệm ngang cấp với các bước huấn luyện của thí nghiệm còn lại.
- Benchmark tổng hợp trong Chapter 5 chỉ trình bày reference text của ALQAC và Zalo; bỏ toàn bộ hàng kết quả extracted text và các kết luận so sánh hai phiên bản corpus. Có thể dùng tên dataset trực tiếp trong bảng sau khi đã nêu nguồn reference text. Không nhắc lại reference fallback trong Chapter 5. Với các thí nghiệm fine-tuning đã chạy trên corpus khác, giữ đúng mô tả nguồn dữ liệu thực tế và tách khỏi benchmark reference text; không đổi nhãn hoặc dùng lại điểm số như thể đã chạy trên reference text.
- Dùng label và `\ref` cho các dẫn chiếu đến section của Chapter 4 để tránh sai số mục sau khi tổ chức lại. Phân biệt biến động giữa các seed với độ bất định trên quần thể câu hỏi; không gọi đại lượng bootstrap tail-area là p-value đã được hiệu chuẩn khi quy trình không hỗ trợ cách diễn giải đó.

- Chapter 5 mở đầu bằng Experimental Conditions, nêu phần cứng và phiên bản phần mềm có bằng chứng từ hồ sơ chạy, không suy cấu hình benchmark từ cấu hình fine-tuning. Sau đó trình bày theo thứ tự: kết quả xây dựng và đánh giá BCA (thu thập, coverage, các vấn đề quan sát được và benchmark) → kết quả fine-tuning (tham số được chọn, development và so sánh với pretrained trên test) → benchmark tổng hợp (cấu hình tốt nhất theo từng điều kiện/metric, đóng góp E5 và hybrid). Phân biệt khó khăn minh họa ở câu hỏi đời thường với nguyên nhân lỗi đã đo; không tự gán tần suất hoặc nguyên nhân khi chưa có annotation.
- Caption bảng trong Chapter 5 phải ngắn gọn, dễ hiểu, thường chỉ một câu nêu nội dung so sánh và dataset hoặc tập đánh giá khi cần phân biệt. Không đưa toàn bộ quy trình, công thức delta, trọng số, seed hay kết luận vào caption. Đặt các điều kiện cần thiết trong đoạn dẫn hoặc ghi chú gần bảng; giữ đủ thông tin để phân biệt các tập đánh giá và diễn giải đúng số liệu. Dẫn chiếu bảng bằng `\ref`, tránh viết số bảng cố định.

- Chapter 5 dùng tên “Experiments and Evaluation”, gồm ba section: Experimental Conditions; Benchmark & Evaluation Procedure; Experimental Results & Analysis. Đặt BCA Dataset Results, BGE-M3 Fine-Tuning Results, Overall Retrieval Benchmark và Summary of Results thành bốn subsection trong section kết quả; hạ các mục con hiện có xuống subsubsection. Giữ thứ tự kết quả BCA → fine-tuning → benchmark tổng hợp và dùng label/ref sau khi đổi cấp tiêu đề.
