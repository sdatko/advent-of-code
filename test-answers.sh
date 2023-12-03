#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

#
# Helper variables
#
RED="$(tput -T xterm setaf 1 || true)"
GREEN="$(tput -T xterm setaf 2 || true)"
YELLOW="$(tput -T xterm setaf 3 || true)"
RESET="$(tput -T xterm sgr0 || true)"

YEAR='*'
DAY='*'
PART='*'

ERRORS=0


#
# Helper functions
#
function erro {
    echo "$@" >&2
}

function usage {
    echo
    echo "Usage: ${0} [-h] [-y <YEAR>] [-d <DAY>] [-p <PART>]"
    echo
}


#
# Cleanup function for the script, trap ensures to execute it
#
function cleanup {
    tput -T xterm sgr0
}

trap cleanup EXIT


#
# Parameters
#
while getopts ":y:d:p:h" opt; do
    case "${opt}" in
        h)
            usage
            exit 0
            ;;
        y)
            YEAR=${OPTARG}
            ;;
        d)
            DAY=${OPTARG}
            ;;
        p)
            PART=${OPTARG}
            ;;
        \?)
            usage
            erro "${RED}ERROR Invalid option: -${OPTARG}${RESET}"
            exit 1
            ;;
        :)
            usage
            erro "${RED}ERROR Option -${OPTARG} requires an argument.${RESET}"
            exit 1
            ;;
    esac
done


#
# Files to check
#
# shellcheck disable=SC2206  # we intentionally allow globbing here
FILES=(year-${YEAR}/day-${DAY}/part-${PART}.py)


#
# Expected outcomes
#
declare -A ANSWERS

for ANSWERS_FILE in ./year-*/answers.sh; do
    # shellcheck source=year-2015/answers.sh
    . "${ANSWERS_FILE}"
done


#
# Compare the outcomes
#
for FILE in "${FILES[@]}"; do
    DIRECTORY=$(dirname "${FILE}")
    MODULE=$(basename "${FILE%.*}")

    if [ ! "${ANSWERS[${FILE}]+exists}" ]; then
        echo "${RED}${FILE}: ERROR no expected value defined${RESET}"
        (( ERRORS += 1 ))
        continue
    fi

    TIME_START=$(date +%s%3N)

    if ! ACTUAL=$(
        pushd "${DIRECTORY}" > /dev/null
        python3 -m "${MODULE}" 2>/dev/null
        popd > /dev/null
    ); then
        echo "${RED}${FILE}: ERROR running the script${RESET}"
        (( ERRORS += 1 ))
        continue
    fi

    TIME_END=$(date +%s%3N)
    DURATION=$(bc <<< "${TIME_END} - ${TIME_START}")

    if [ "${DURATION}" -gt 2000 ]; then
        DURATION="${RED}(${DURATION} ms)${RESET}"
    elif [ "${DURATION}" -gt 1000 ]; then
        DURATION="${YELLOW}(${DURATION} ms)${RESET}"
    else
        DURATION="${GREEN}(${DURATION} ms)${RESET}"
    fi

    EXPECTED="${ANSWERS[${FILE}]}"
    if [ "${ACTUAL}" != "${EXPECTED}" ]; then
        EXPECTED="${EXPECTED//$'\n'/\\n}"
        ACTUAL="${ACTUAL//$'\n'/\\n}"
        echo "${RED}${FILE}: ERROR expected ${EXPECTED}, got ${ACTUAL}${RESET}"
        (( ERRORS += 1 ))
        continue
    else
        echo "${GREEN}${FILE}: OK ${DURATION}${RESET}"
    fi
done


#
# Set the exit status
#
echo ':: Summary'
if [ "${ERRORS}" -gt 0 ]; then
    echo "${RED}${ERRORS} errors!${RESET}"
    exit 1
else
    echo "${GREEN}No errors!${RESET}"
fi
