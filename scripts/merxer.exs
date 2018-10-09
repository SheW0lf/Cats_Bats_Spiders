# Author: Thawatchai Singngam
# Language: Elixir
# Github: https://github.com/merxer

defmodule Hacktoberfest do
    def cat_bat_spider(n) do
        case {rem(n,3), rem(n,5), rem(n,15)} do
            {_, _, 0} -> "spiders"
            {_, 0, _} -> "bats"
            {0, _, _} -> "cats"
            _ -> n
        end
    end
end

for loop <- 1..100 do
    Hacktoberfest.cat_bat_spider(loop)
    |> IO.puts
end
