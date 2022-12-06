#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

#
# Configuration
#
# USE_LINKS – whether to generate links in Markdown (true/false)
#
FILE='README.md'
SECTION_NAME='Summary'
USE_LINKS=true


#
# Gather input
#
DAYS=({01..25})
YEARS=()

for YEAR in year-*; do
    YEARS+=("${YEAR##*-}")
done


#
# Get everything from existing README up to SECTION
#
if LINE_NUMBER=$(grep -nx "${SECTION_NAME}" "${FILE}" | cut -d ':' -f 1); then
    head -n "${LINE_NUMBER}" "${FILE}"
    echo "${SECTION_NAME//?/-}"
    echo
else
    cat "${FILE}"
    echo
    echo
    echo "${SECTION_NAME}"
    echo "${SECTION_NAME//?/-}"
    echo
fi


#
# Table header
#
echo -n '|  day  |'

for YEAR in "${YEARS[@]}"; do
    if ( "${USE_LINKS}" ); then
        echo -n " [${YEAR}](./year-${YEAR}/)      |"
    else
        echo -n " ${YEAR} |"
    fi
done

echo  # newline


#
# Table alignment
#
echo -n '| :---: |'

for YEAR in "${YEARS[@]}"; do
    if ( "${USE_LINKS}" ); then
        echo -n ' :-----------------------: |'
    else
        echo -n ' :--: |'
    fi
done

echo  # newline


#
# Table rows
#
for DAY in "${DAYS[@]}"; do
    echo -n "|   ${DAY}  |"

    for YEAR in "${YEARS[@]}"; do
        if [ -d "year-${YEAR}/day-${DAY}" ]; then
            MARK='✔ '
            if ( "${USE_LINKS}" ); then
                MARK="[${MARK}](./year-${YEAR}/day-${DAY}/)"
            else
                MARK=" ${MARK} "
            fi
        else
            MARK='❌'
            if ( "${USE_LINKS}" ); then
                MARK=" ${MARK}                      "
            else
                MARK=" ${MARK} "
            fi
        fi
        echo -n " ${MARK} |"
    done

    echo  # newline
done


#
# Legend
#
cat << EOF

Legend:
- ✔ – solution exists in repo
- ❌ – no solution yet
EOF
