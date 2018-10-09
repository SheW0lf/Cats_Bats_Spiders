#!/bin/bash
#  Author: emdavis7
#  Language: bash
#  Github: github.com/emdavis7

x=1
while [ $x -le 100 ]
do
  if [[ 0 -eq "($x%3) + ($x%5)" ]] 
  then
  # Check if divide by 3 & 5 #
    echo "fizz buzz"
  elif [[ 0 -eq "($x%5)" ]]
  then
  # Check if divide by 5 #   
    echo "buzz"
  elif [[ 0 -eq "($x%3)" ]]
  then
  # Check if divide by 3 #
    echo "fizz"
   else
    echo "$x"
   fi	
  x=$(( $x + 1 ))
done
