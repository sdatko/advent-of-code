#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

WORK_DIR=${1:-.}

EXPECTED_ANSWERS=(
    793524
    61515678
    536
    558
    244
    9406609920
    182
    109
    938
    696
    6799
    3354
    124
    34862
    1521
    1016
    1639024365
    219202240
    1998
    347250213298688
    2113
    1865
    2458
    145117
    410
    600691418730595
    8566770985168
    4832039794082
    959
    116590
    18142
    1069784384303
    218
    1908
    25190263477788
    297139939002972
    120
    350
)


#
# Cleanup function for the script, trap ensures to execute it
#
function cleanup() {
    tput -T xterm sgr0
}
trap cleanup EXIT


#
# Have expected answers as command line arguments
#
set -- "${EXPECTED_ANSWERS[@]}"


#
# Test the solutions
#
error=0

for DIRECTORY in "${WORK_DIR}/day-"*; do
    pushd "${DIRECTORY}" > /dev/null

    if [ -f 'part-1.py' ]; then
        EXPECTED_ANSWER=$1
        ACTUAL_ANSWER=$(python3 part-1.py)
        if [ "${ACTUAL_ANSWER}" != "${EXPECTED_ANSWER}" ]; then
            echo -ne "\033[31m"
            error=1
        else
            echo -ne "\033[32m"
        fi
        echo "---> ${DIRECTORY}/part-1.py"
        shift
    fi

    if [ -f 'part-2.py' ]; then
        EXPECTED_ANSWER=$1
        ACTUAL_ANSWER=$(python3 part-2.py)

        if [ "${ACTUAL_ANSWER}" != "${EXPECTED_ANSWER}" ]; then
            echo -ne "\033[31m"
            error=1
        else
            echo -ne "\033[32m"
        fi
        echo "---> ${DIRECTORY}/part-2.py"
        shift
    fi

    popd > /dev/null
done

exit "${error}"
