#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Validates that every subfolder under docs/ contains a README.md file.

.DESCRIPTION
    Walks all subdirectories under the docs/ root recursively and reports any
    that are missing a README.md file. Exits 0 when all subfolders pass or when
    docs/ does not exist. Exits 1 when one or more subfolders are missing README.md.

.PARAMETER DocsPath
    Path to the docs/ root directory. Defaults to the docs/ folder at the
    repository root (resolved relative to this script's location).

.EXAMPLE
    pwsh ./scripts/Validate-DocsReadme.ps1

.EXAMPLE
    pwsh ./scripts/Validate-DocsReadme.ps1 -DocsPath ./docs
#>
param(
    [string]$DocsPath = (Join-Path (Split-Path $PSScriptRoot -Parent) 'docs')
)

$DocsPath = (Resolve-Path -LiteralPath $DocsPath -ErrorAction SilentlyContinue)?.Path

if (-not $DocsPath -or -not (Test-Path -LiteralPath $DocsPath -PathType Container)) {
    Write-Output "Nothing to validate - docs/ is missing."
    exit 0
}

$repoRoot = Split-Path $DocsPath -Parent
$missing = @()

Get-ChildItem -LiteralPath $DocsPath -Directory -Recurse | ForEach-Object {
    $readmePath = Join-Path $_.FullName 'README.md'
    if (-not (Test-Path -LiteralPath $readmePath -PathType Leaf)) {
        $relPath = [IO.Path]::GetRelativePath($repoRoot, $_.FullName)
        $missing += $relPath
    }
}

if ($missing.Count -gt 0) {
    foreach ($folder in $missing) {
        Write-Error "Missing README.md in $folder"
    }
    exit 1
}

$total = (Get-ChildItem -LiteralPath $DocsPath -Directory -Recurse | Measure-Object).Count
Write-Output "Validated $total docs subfolders."
exit 0
