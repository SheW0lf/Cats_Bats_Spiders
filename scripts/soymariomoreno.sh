#!/bin/bash

//AUTHOR: Mario Moreno
//LANGUAGE: Bash
//GITHUB: https://github.com/soymariomoreno

x=1
while [ $x -le 100 ]
do
  if [[ 0 -eq "($x%3) + ($x%5)" ]] 
  then
  # Check if divide by 3 & 5 #
    echo "Spiders"
  elif [[ 0 -eq "($x%5)" ]]
  then
  # Check if divide by 5 #   
    echo "Cats"
  elif [[ 0 -eq "($x%3)" ]]
  then
  # Check if divide by 3 #
    echo "Bats"
   else
    echo "$x"
   fi	
  x=$(( $x + 1 ))
done