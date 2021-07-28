#!/bin/sh

# initialize
: > ./docs/dataworld_query.org

for file in `\find ./src/dataworld -name '*.py'`;
do
  echo $file
  python $file | sed -e s/.*[0-9]m// >> ./docs/dataworld_query.org
done
