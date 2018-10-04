#!/usr/bin/julia

# AUTHOR: Germán Aguilera
# LANGUAGE: Julia
# GITHUB: https://github.com/germmand

function main()
    for i = 1:100
        if i % 3 == 0
            println("Cats")
        elseif i % 5 == 0
            println("Bats")
        elseif i % 3 == 0 && i % 5 == 0
            println("Spiders")
        else
            println(i)
        end
    end
end

main()
