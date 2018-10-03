//AUTHOR: Damian Dabrowski
//LANGUAGE: Bash
//GITHUB: https://github.com/ddcodepl

for i in `seq 1 100`;
do
    c=$(($i%3))
    b=$(($i%5))

    if [[ $c == 0 ]]
    then
        if [[ $b == 0 ]]
            then echo "Spiders"
        fi
        echo "Cats"
    elif [[ $b == 0 ]]
        then echo "Bats"
    else echo $i
    fi
done
