#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

#
# Expected outcomes
#
declare -A ANSWERS=(
    [year-2017/day-01/part-1.py]=1102
    [year-2017/day-01/part-2.py]=1076

    [year-2018/day-01/part-1.py]=437
    [year-2018/day-01/part-2.py]=655

    [year-2019/day-01/part-1.py]=3497399
    [year-2019/day-01/part-2.py]=5243207

    [year-2020/day-01/part-1.py]=793524
    [year-2020/day-01/part-2.py]=61515678
    [year-2020/day-02/part-1.py]=536
    [year-2020/day-02/part-2.py]=558
    [year-2020/day-03/part-1.py]=244
    [year-2020/day-03/part-2.py]=9406609920
    [year-2020/day-04/part-1.py]=182
    [year-2020/day-04/part-2.py]=109
    [year-2020/day-05/part-1.py]=938
    [year-2020/day-05/part-2.py]=696
    [year-2020/day-06/part-1.py]=6799
    [year-2020/day-06/part-2.py]=3354
    [year-2020/day-07/part-1.py]=124
    [year-2020/day-07/part-2.py]=34862
    [year-2020/day-08/part-1.py]=1521
    [year-2020/day-08/part-2.py]=1016
    [year-2020/day-09/part-1.py]=1639024365
    [year-2020/day-09/part-2.py]=219202240
    [year-2020/day-10/part-1.py]=1998
    [year-2020/day-10/part-2.py]=347250213298688
    [year-2020/day-11/part-1.py]=2113
    [year-2020/day-11/part-2.py]=1865
    [year-2020/day-12/part-1.py]=2458
    [year-2020/day-12/part-2.py]=145117
    [year-2020/day-13/part-1.py]=410
    [year-2020/day-13/part-2.py]=600691418730595
    [year-2020/day-14/part-1.py]=8566770985168
    [year-2020/day-14/part-2.py]=4832039794082
    [year-2020/day-15/part-1.py]=959
    [year-2020/day-15/part-2.py]=116590
    [year-2020/day-16/part-1.py]=18142
    [year-2020/day-16/part-2.py]=1069784384303
    [year-2020/day-17/part-1.py]=218
    [year-2020/day-17/part-2.py]=1908
    [year-2020/day-18/part-1.py]=25190263477788
    [year-2020/day-18/part-2.py]=297139939002972
    [year-2020/day-19/part-1.py]=120
    [year-2020/day-19/part-2.py]=350

    [year-2021/day-01/part-1.py]=1342
    [year-2021/day-01/part-2.py]=1378
    [year-2021/day-02/part-1.py]=1488669
    [year-2021/day-02/part-2.py]=1176514794
    [year-2021/day-03/part-1.py]=738234
    [year-2021/day-03/part-2.py]=3969126
    [year-2021/day-04/part-1.py]=63552
    [year-2021/day-04/part-2.py]=9020
    [year-2021/day-05/part-1.py]=5698
    [year-2021/day-05/part-2.py]=15463
    [year-2021/day-06/part-1.py]=371379
    [year-2021/day-06/part-2.py]=1674303997472
    [year-2021/day-07/part-1.py]=356179
    [year-2021/day-07/part-2.py]=99788435
    [year-2021/day-08/part-1.py]=445
    [year-2021/day-08/part-2.py]=1043101
    [year-2021/day-09/part-1.py]=504
    [year-2021/day-09/part-2.py]=1558722
    [year-2021/day-10/part-1.py]=268845
    [year-2021/day-10/part-2.py]=4038824534
    [year-2021/day-11/part-1.py]=1599
    [year-2021/day-11/part-2.py]=418
    [year-2021/day-12/part-1.py]=4659
    [year-2021/day-12/part-2.py]=148962
    [year-2021/day-13/part-1.py]=745
    [year-2021/day-13/part-2.py]=' ##  ###  #  #   ## #### ###   ##   ## 
#  # #  # # #     # #    #  # #  # #  #
#  # ###  ##      # ###  ###  #    #   
#### #  # # #     # #    #  # # ## #   
#  # #  # # #  #  # #    #  # #  # #  #
#  # ###  #  #  ##  #    ###   ###  ## '
    [year-2021/day-14/part-1.py]=4517
    [year-2021/day-14/part-2.py]=4704817645083
    [year-2021/day-15/part-1.py]=447
    [year-2021/day-15/part-2.py]=2825
    [year-2021/day-16/part-1.py]=883
    [year-2021/day-16/part-2.py]=1675198555015
    [year-2021/day-17/part-1.py]=5151
    [year-2021/day-17/part-2.py]=968
    [year-2021/day-18/part-1.py]=3884
    [year-2021/day-18/part-2.py]=4595
    [year-2021/day-19/part-1.py]=332
    [year-2021/day-19/part-2.py]=8507
    [year-2021/day-20/part-1.py]=5479
    [year-2021/day-20/part-2.py]=19012
    [year-2021/day-21/part-1.py]=908091
    [year-2021/day-21/part-2.py]=190897246590017
    [year-2021/day-22/part-1.py]=598616
    [year-2021/day-22/part-2.py]=1193043154475246
    [year-2021/day-23/part-1.py]=10607
    [year-2021/day-23/part-2.py]=59071
    [year-2021/day-24/part-1.py]=41299994879959
    [year-2021/day-24/part-2.py]=11189561113216
    [year-2021/day-25/part-1.py]=278
    [year-2021/day-25/part-2.py]=0

    [year-2022/day-01/part-1.py]=71023
    [year-2022/day-01/part-2.py]=206289
    [year-2022/day-02/part-1.py]=13526
    [year-2022/day-02/part-2.py]=14204
    [year-2022/day-03/part-1.py]=7817
    [year-2022/day-03/part-2.py]=2444
    [year-2022/day-04/part-1.py]=528
    [year-2022/day-04/part-2.py]=881
    [year-2022/day-05/part-1.py]=TGWSMRBPN
    [year-2022/day-05/part-2.py]=TZLTLWRNF
    [year-2022/day-06/part-1.py]=1480
    [year-2022/day-06/part-2.py]=2746
    [year-2022/day-07/part-1.py]=1182909
    [year-2022/day-07/part-2.py]=2832508
    [year-2022/day-08/part-1.py]=1560
    [year-2022/day-08/part-2.py]=252000
)


#
# Helper variables
#
RED="$(tput -T xterm setaf 1 || true)"
GREEN="$(tput -T xterm setaf 2 || true)"
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
# Compare the outcomes
#
for FILE in "${FILES[@]}"; do
    DIRECTORY=$(dirname "${FILE}")
    MODULE=$(basename "${FILE%.*}")

    if [ ! "${ANSWERS["${FILE}"]+exists}" ]; then
        echo "${RED}${FILE}: ERROR no expected value defined${RESET}"
        : $(( ERRORS++ ))
        continue
    fi

    if ! ACTUAL=$(
        pushd "${DIRECTORY}" > /dev/null
        python3 -m "${MODULE}" 2>/dev/null
        popd > /dev/null
    ); then
        echo "${RED}${FILE}: ERROR running the script${RESET}"
        : $(( ERRORS++ ))
        continue
    fi

    EXPECTED="${ANSWERS["${FILE}"]}"
    if [ "${ACTUAL}" != "${EXPECTED}" ]; then
        EXPECTED="${EXPECTED//$'\n'/\\n}"
        ACTUAL="${ACTUAL//$'\n'/\\n}"
        echo "${RED}${FILE}: ERROR expected ${EXPECTED}, got ${ACTUAL}${RESET}"
        : $(( ERRORS++ ))
        continue
    else
        echo "${GREEN}${FILE}: OK${RESET}"
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
