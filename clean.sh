#!/usr/bin/env bash
#
# Helper script that removes all Python cache files
# and empty directories from the directory tree given
# as first argument (default: current working directory).
#
set -o errexit
set -o nounset
set -o pipefail

ENTRY_DIR="${1:-.}"

find "${ENTRY_DIR}" \
    -not -path '*/.*' \
    '(' \
        '(' \
            -type d \
            -empty \
        ')' \
        -o \
        '(' \
            -type d \
            -name '__pycache__' \
        ')' \
        -o \
        '(' \
            -type f \
            -name '*.py[cod]' \
        ')' \
    ')' \
    -print \
    -delete
