{-# OPTIONS_GHC -Wall #-}

{-# LANGUAGE ViewPatterns #-}
module Main where 

gt100 :: Integer -> Bool
gt100 x = x > 100

greaterThan100 :: [Integer] -> [Integer]
greaterThan100 xs = filter gt100 xs

greaterThan100_2 :: [Integer] -> [Integer]
greaterThan100_2 xs = filter (\x -> x > 100) xs

greaterThan100_3 :: [Integer] -> [Integer]
greaterThan100_3 xs = filter (>100) xs

foo :: (b -> c) -> (a -> b) -> (a -> c)
foo f g = \x -> f (g x)

foobar :: [Integer] -> Integer
foobar []     = 0
foobar (x:xs)
  | x > 3     = (7*x + 2) + foobar xs
  | otherwise = foobar xs

-- Excercise 1
fun1 :: [Integer] -> Integer
fun1 [] = 1
fun1 (x:xs)
    | even x = (x - 2) * fun1 xs
    | otherwise = fun1 xs

fun1' :: [Integer] -> Integer
fun1' = product . map (subtract 2) . filter even

fun2 :: Integer -> Integer
fun2 1 = 0
fun2 n | even n = n + fun2 (n ‘div‘ 2)
| otherwise = fun2 (3 * n + 1)

fun2' :: Integer -> Integer
fun2' = sum . filter even . takeWhile (/= 1) . iterate (\n -> if even n then n `div` 2 else 3*n+1)

-- Excercise 3
xor :: [Bool] -> Bool
xor = foldr xor2 False

map’ :: (a -> b) -> [a] -> [b]
map’ f = foldr (\x y -> f x : y) []


main = do
    print(fun1' [])
