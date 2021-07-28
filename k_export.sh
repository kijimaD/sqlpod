#!/bin/sh

# initialize
: > ./docs/100knock_query.org

for file in `\find ./src/100knock -name '*.py'`;
do
  echo $file
  python $file | sed -e s/.*[0-9]m// >> ./docs/100knock_query.org
done
