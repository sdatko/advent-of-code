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
COMMAND=''

ERRORS=0


#
# Helper functions
#
function erro {
    echo "$@" >&2
}

function usage {
    echo
    echo "Usage: ${0} [-h] [-y <YEAR>] [-d <DAY>] [-p <PART>] [-c <COMMAND>]"
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
while getopts ":y:d:p:c:h" opt; do
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
        c)
            COMMAND=${OPTARG}
            ;;
        \?)
            usage
            erro "${RED}ERROR Invalid option: -${OPTARG}${RESET}"
            exit 2
            ;;
        :)
            usage
            erro "${RED}ERROR Option -${OPTARG} requires an argument.${RESET}"
            exit 2
            ;;
    esac
done


#
# Interpreter selection
#
if [ -z "${COMMAND}" ]; then
    if command -v python3 &> /dev/null; then
        COMMAND='python3'
    elif command -v pypy3 &> /dev/null; then
        COMMAND='pypy3'
    else
        echo "${RED}ERROR Could not find Python 3 intepreter${RESET}"
        exit 2
    fi
fi


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
        _=$(( ERRORS += 1 ))
        continue
    fi

    TIME_START=$(date +%s%3N)

    if ! ACTUAL=$(
        pushd "${DIRECTORY}" > /dev/null
        "${COMMAND}" -m "${MODULE}" 2>/dev/null
        popd > /dev/null
    ); then
        echo "${RED}${FILE}: ERROR running the script${RESET}"
        _=$(( ERRORS += 1 ))
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
        _=$(( ERRORS += 1 ))
        continue
    else
        echo "${GREEN}${FILE}: OK ${DURATION}${RESET}"
    fi
done


#
# Report mismatched answers
#
for FILE in year-*/day-*/part-*.py; do
    unset -v "ANSWERS[${FILE}]"
done

for FILE in "${!ANSWERS[@]}"; do
    echo "${RED}${0}: ERROR missing file ${FILE}${RESET}"
    _=$(( ERRORS += 1 ))
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
