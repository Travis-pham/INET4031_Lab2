#!/bin/bash

a=2
b=2
c=$((a+b))
echo "Bash says: Hello, World!"
echo "$a + $b = $c"
declare -a string_list=("User1" "User2" "User3")
for user in "${string_list[@]}";
do
	echo "$user"
done
