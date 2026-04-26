#!/usr/bin/env bash
set -euo pipefail

# Copy selected HVE Core assets from installed extension into the current repo for local customization.

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
TARGET_GITHUB_DIR="$ROOT_DIR/.github"

usage() {
  cat <<'EOF'
Usage:
  scripts/customize-hve-core.sh list [agents|prompts|instructions|skills]
  scripts/customize-hve-core.sh copy <agents|prompts|instructions|skills> <relative-path> [--force]

Examples:
  scripts/customize-hve-core.sh list agents
  scripts/customize-hve-core.sh copy agents hve-core/task-researcher.agent.md
  scripts/customize-hve-core.sh copy prompts hve-core/task-plan.prompt.md
  scripts/customize-hve-core.sh copy instructions hve-core/markdown.instructions.md --force
EOF
}

find_extension_root() {
  local candidates
  candidates=$(find \
    "$HOME/.vscode/extensions" \
    "$HOME/.vscode-insiders/extensions" \
    -maxdepth 1 -type d -name 'ise-hve-essentials.hve-core-all-*' 2>/dev/null || true)

  if [[ -z "${candidates}" ]]; then
    echo "Error: HVE Core extension not found in ~/.vscode/extensions or ~/.vscode-insiders/extensions" >&2
    exit 1
  fi

  # Choose the latest lexicographically sorted path (version suffix sorts correctly for current naming).
  echo "${candidates}" | sort | tail -n 1
}

list_assets() {
  local kind="${1:-}"
  local ext_root
  ext_root=$(find_extension_root)

  if [[ -z "${kind}" ]]; then
    for k in agents prompts instructions skills; do
      echo "# ${k}"
      find "$ext_root/.github/$k" -type f | sed "s|$ext_root/.github/$k/||" | sort
      echo
    done
    return
  fi

  case "$kind" in
    agents|prompts|instructions|skills) ;;
    *)
      echo "Error: invalid kind '$kind'" >&2
      usage
      exit 1
      ;;
  esac

  find "$ext_root/.github/$kind" -type f | sed "s|$ext_root/.github/$kind/||" | sort
}

copy_asset() {
  local kind="$1"
  local rel="$2"
  local force="${3:-}"

  case "$kind" in
    agents|prompts|instructions|skills) ;;
    *)
      echo "Error: invalid kind '$kind'" >&2
      usage
      exit 1
      ;;
  esac

  local ext_root src dst
  ext_root=$(find_extension_root)
  src="$ext_root/.github/$kind/$rel"
  dst="$TARGET_GITHUB_DIR/$kind/$rel"

  if [[ ! -f "$src" ]]; then
    echo "Error: source not found: $src" >&2
    echo "Tip: run 'scripts/customize-hve-core.sh list $kind' to browse available files." >&2
    exit 1
  fi

  mkdir -p "$(dirname "$dst")"

  if [[ -f "$dst" && "$force" != "--force" ]]; then
    echo "Error: destination exists: $dst" >&2
    echo "Use --force to overwrite." >&2
    exit 1
  fi

  cp "$src" "$dst"
  echo "Copied: $kind/$rel"
  echo "To:     $dst"
}

main() {
  local cmd="${1:-}"

  case "$cmd" in
    list)
      list_assets "${2:-}"
      ;;
    copy)
      if [[ $# -lt 3 ]]; then
        usage
        exit 1
      fi
      copy_asset "$2" "$3" "${4:-}"
      ;;
    -h|--help|help|"")
      usage
      ;;
    *)
      echo "Error: unknown command '$cmd'" >&2
      usage
      exit 1
      ;;
  esac
}

main "$@"
