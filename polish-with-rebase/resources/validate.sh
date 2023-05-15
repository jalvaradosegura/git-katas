#!/bin/bash

git log --oneline > commits.txt

cp ../resources/validate.py .
cat main.py >> validate.py
cat ../resources/try_function.py >> validate.py

python3 validate.py

if [ $? -eq 0 ]; then
  echo "✅ You passed the test."
else
  echo "\nPlease modify your project and try again."
fi

rm commits.txt
rm validate.py
