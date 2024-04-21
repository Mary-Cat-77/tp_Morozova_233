#!/bin/bash

echo $1
if ! [ -d $1 ]; then
    echo 'No directory'
fi
if ! [ -d $2 ]; then
    mkdir $2
fi
for file in `find $1 -type f -name "*"`
    do 
        if ! [ -f $2/$(basename $file) ]; then
            cp $file $2/ 
        else 
            cp $file $2/new_$(basename $file)
        fi
done