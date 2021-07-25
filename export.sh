#!/bin/sh

# initialize
: > ./docs/query.org

for file in `\find ./src -name '*.py'`;
do
  echo $file
  python $file | sed -e s/.*[0-9]m// >> ./docs/query.org
done
