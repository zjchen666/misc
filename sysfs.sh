#!/bin/bash

    for i in /sys/bus/*/devices/*/dev /sys/class/*/*/dev
    do
        if [ -f $i ]
	then
	    MAJOR=$(sed 's/:.*//' < $i)
	    MINOR=$(sed 's/.*://' < $i)
	    DEVNAME=$(echo $i | sed -e 's@/dev@@' -e 's@.*/@@')
	    echo /dev/$DEVNAME c $MAJOR $MINOR
	fi
    done
