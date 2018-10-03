--AUTHOR: TylerMaclay
--LANGUAGE: Haskell
--Github: https://github.com/TylerMaclay

catsBatsSpiders :: Int -> String
catsBatsSpiders x 

    | (x `mod` 15 == 0) = "Spiders"
    | (x `mod` 5 == 0) = "Bats"
    | (x `mod` 3 == 0) = "Cats"
    | otherwise =  show x

main = mapM_ putStrLn [catsBatsSpiders x | x <- [1..100]]