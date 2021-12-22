#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

WORK_DIR=${1:-.}

EXPECTED_ANSWERS=(
    1342
    1378
    1488669
    1176514794
    738234
    3969126
    63552
    9020
    5698
    15463
    371379
    1674303997472
    356179
    99788435
    445
    1043101
    504
    1558722
    268845
    4038824534
    1599
    418
    4659
    148962
    745
    ' ##  ###  #  #   ## #### ###   ##   ## 
#  # #  # # #     # #    #  # #  # #  #
#  # ###  ##      # ###  ###  #    #   
#### #  # # #     # #    #  # # ## #   
#  # #  # # #  #  # #    #  # #  # #  #
#  # ###  #  #  ##  #    ###   ###  ## '
    4517
    4704817645083
    447
    2825
    883
    1675198555015
    5151
    968
    3884
    4595
    332
    8507
    5479
    19012
    908091
    190897246590017
    598616
    1193043154475246
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
