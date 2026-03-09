#!/usr/bin/env bash
#
# archive-content.sh — Archive current content and prepare for a new run.
# Keeps only the last 3 archives. Prompts for confirmation before archiving.
#
# Usage:
#   ./scripts/archive-content.sh
#   ./scripts/archive-content.sh --yes   # Skip confirmation prompt
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONTENT_DIR="$REPO_ROOT/content"
ARCHIVE_DIR="$REPO_ROOT/archive"
MAX_ARCHIVES=3

# ── Check if there's content to archive ──────────────────────────────────
if [ ! -d "$CONTENT_DIR" ] || [ -z "$(ls -A "$CONTENT_DIR" 2>/dev/null)" ]; then
  echo "Nothing to archive — content/ is empty or missing."
  exit 0
fi

# Skip pipeline-config.md from the "has content" check
content_files=$(find "$CONTENT_DIR" -type f ! -name 'pipeline-config.md' | head -1)
if [ -z "$content_files" ]; then
  echo "Nothing to archive — content/ only has pipeline-config.md."
  exit 0
fi

# ── Show what will be archived ───────────────────────────────────────────
echo ""
echo "=== Content to be archived ==="
find "$CONTENT_DIR" -type f ! -name 'pipeline-config.md' | sort | sed "s|$REPO_ROOT/||"
echo ""

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ARCHIVE_NAME="run-$TIMESTAMP"
echo "Archive destination: archive/$ARCHIVE_NAME/"
echo ""

# ── Confirm ──────────────────────────────────────────────────────────────
if [[ "${1:-}" != "--yes" ]]; then
  read -rp "Archive current content and prepare for a new run? [y/N] " confirm
  if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
  fi
fi

# ── Archive ──────────────────────────────────────────────────────────────
mkdir -p "$ARCHIVE_DIR/$ARCHIVE_NAME"

# Copy everything except pipeline-config.md (user config stays)
rsync -a --exclude='pipeline-config.md' "$CONTENT_DIR/" "$ARCHIVE_DIR/$ARCHIVE_NAME/"

echo "Archived to archive/$ARCHIVE_NAME/"

# ── Clean content/ for new run ───────────────────────────────────────────
# Remove everything except pipeline-config.md
find "$CONTENT_DIR" -mindepth 1 ! -name 'pipeline-config.md' -exec rm -rf {} + 2>/dev/null || true

# Recreate visuals directory
mkdir -p "$CONTENT_DIR/visuals"

echo "Cleaned content/ — ready for a new pipeline run."

# ── Prune old archives (keep last 3) ────────────────────────────────────
archive_count=$(find "$ARCHIVE_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
if [ "$archive_count" -gt "$MAX_ARCHIVES" ]; then
  remove_count=$((archive_count - MAX_ARCHIVES))
  # Sort by name (timestamp-based) and remove oldest
  find "$ARCHIVE_DIR" -mindepth 1 -maxdepth 1 -type d | sort | head -n "$remove_count" | while read -r dir; do
    rm -rf "$dir"
    echo "Pruned old archive: $(basename "$dir")"
  done
fi

echo ""
echo "=== Done ==="
echo "Archives: $( find "$ARCHIVE_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')/$MAX_ARCHIVES"
find "$ARCHIVE_DIR" -mindepth 1 -maxdepth 1 -type d | sort | sed "s|$REPO_ROOT/||"
