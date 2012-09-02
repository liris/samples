#!/bin/bash

echo "--- useSemaphore useFair ---"

for i in {0..5}
do
    count=`echo 10^$i | bc`
    /usr/bin/time -f "%E" java SemaTest $count true true
done


echo "--- useSemaphore not useFair ---"

for i in {0..5}
do
    count=`echo 10^$i | bc`
    /usr/bin/time -f "%E" java SemaTest $count true false
done


echo "--- not useSemaphore ---"

for i in {0..5}
do
    count=`echo 10^$i | bc`
    /usr/bin/time -f "%E" java SemaTest $count false false
done