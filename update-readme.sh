#!/usr/bin/env bash
#
# Script generates progress summary for the readme file,
# based on directories created in this repository.
#
set -o errexit
set -o nounset
set -o pipefail

README_FILE='README.md'
README_TMP_FILE='"README.md.tmp'

DAYS=({01..25})
YEARS=()

for YEAR in year-*; do
    YEARS+=("${YEAR##*-}")
done

sed -n "1,/^Summary/p" "${README_FILE}" > "${README_TMP_FILE}"

if ! grep -qxF "Summary" "${README_TMP_FILE}"; then
    echo -e "\n\nSummary" >> "${README_TMP_FILE}";
fi

echo -e "-------\n" >> "${README_TMP_FILE}"

for YEAR in "${YEARS[@]}"; do
    echo -n "[**${YEAR}**](./year-${YEAR}/):" >> "${README_TMP_FILE}"

    for DAY in "${DAYS[@]}"; do
        if ! (( (10#$DAY - 1) % 5 )); then
            echo -n " " >> "${README_TMP_FILE}"
        fi

        if [ -d "year-${YEAR}/day-${DAY}" ]; then
            echo -n "[☑](./year-${YEAR}/day-${DAY}/)" >> "${README_TMP_FILE}"
        else
            echo -n "☐" >> "${README_TMP_FILE}"
        fi
    done

    if [ "${YEAR}" != "${YEARS[-1]}" ]; then
        echo "\\" >> "${README_TMP_FILE}"
    fi
done

echo "" >> "${README_TMP_FILE}"

mv "${README_TMP_FILE}" "${README_FILE}"
