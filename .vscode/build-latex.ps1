param(
    [Parameter(Mandatory = $true)][string]$RootFile,
    [Parameter(Mandatory = $true)][string]$OutputDirectory
)

$ErrorActionPreference = 'Stop'
$taskTexBin = Join-Path (Split-Path -Parent $PSScriptRoot) '.tools\TinyTeX\bin\windows'
$taskLatexmk = Join-Path $taskTexBin 'latexmk.exe'
if (-not (Test-Path -LiteralPath $taskLatexmk -PathType Leaf)) {
    throw "TinyTeX executable is missing: $taskLatexmk"
}

$env:Path = $taskTexBin + ';' + $env:Path
$taskRoot = (Resolve-Path -LiteralPath $RootFile).Path
Set-Location -LiteralPath (Split-Path -Parent $taskRoot)
Write-Output "Building with TinyTeX: $taskLatexmk"
& $taskLatexmk '-synctex=1' '-interaction=nonstopmode' '-file-line-error' '-halt-on-error' '-pdf' "-outdir=$OutputDirectory" $taskRoot
exit $LASTEXITCODE
