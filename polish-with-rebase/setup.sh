#!/bin/bash
#
source ../utils.sh

export DEFAULT_BRANCH=my-feature
make-exercise-repo

cp ../resources/validate.sh .
git add .; git commit -m "Initial commit"

git commit --allow-empty -m "I do nothing, remove me please. I'm also a very long message"

cp ../resources/main_01.py main.py
git add .; git commit -m "add 'say_hi' function."

cp ../resources/main_02.py main.py
git add .; git commit -m "Add 'say_bye' function"

cp ../resources/main_03.py main.py
git add .; git commit -m "Add 'say_bye' function"

cp ../resources/main_04.py main.py
git add .; git commit -m "WIP: add 'add_two_numbers'"

cp ../resources/main_05.py main.py
git add .; git commit -m "WIP: add signature"

