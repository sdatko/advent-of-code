#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

WORK_DIR=${1:-.}
TIMES=10


#
# Cleanup function for the script, trap ensures to execute it
#
function cleanup() {
    tput -T xterm sgr0
}
trap cleanup EXIT


#
# Helper function
#
# Inspired by:
# https://stackoverflow.com/questions/54920113/calculate-average-execution-time-of-a-program-using-bash
#
function avg_time {
    n=$1
    shift

    export LC_ALL=C

    for (( i = 0; i < n; ++i )); do
        # ignore the output of the command
        # but collect time's output in stdout
        { time -p "$@" &>/dev/null; } 2>&1
    done | awk '
        function color_printf(name, value)
        {
             black = "\033[30m";
             red = "\033[31m";
             green = "\033[32m";
             yellow = "\033[33m";
             blue = "\033[34m";
             magenta = "\033[35m";
             cyan = "\033[36m";
             white = "\033[37m";

             if (value > 1.0) color = red;
             else if (value > 0.1) color = yellow;
             else color = green;

             printf(color)
             printf("%s %f\n", name, value);
        }

        /real/ { real = real + $2; nr++ }
        /user/ { user = user + $2; nu++ }
        /sys/  { sys  = sys  + $2; ns++ }
        END    {

                 if (nr>0) avg_real = real/nr;
                     else avg_real = real;
                 if (nu>0) avg_user = user/nu;
                     else avg_user = user;
                 if (ns>0) avg_sys = sys/ns;
                     else avg_sys = sys;

                 color_printf("real", avg_real);
                 color_printf("user", avg_user);
                 color_printf("sys", avg_sys);
               }'
    tput -T xterm sgr0
}


#
# Test the execution times
#
for DIRECTORY in "${WORK_DIR}/day-"*; do
    pushd "${DIRECTORY}" > /dev/null

    if [ -f 'part-1.py' ]; then
        echo "---> ${DIRECTORY}/part-1.py"
        avg_time "${TIMES}" python3 part-1.py
    fi

    if [ -f 'part-2.py' ]; then
        echo "---> ${DIRECTORY}/part-2.py"
        avg_time "${TIMES}" python3 part-2.py
    fi

    popd > /dev/null
done
