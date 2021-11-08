{-# OPTIONS_GHC -Wall #-}

{-# LANGUAGE ViewPatterns #-}
module Main where 

{- x :: Int
x = 3

y :: Int
y = y + 1

d1, d2 :: Double
d1 = 4.5387
d2 = 6.2831e-4

s :: String
s = "Hello, Haskell!"

ex01 = 3 + 2
ex02 = 19 - 27
ex03 = 2.35 * 8.6
ex04 = 8.7 / 3.1
ex05 = mod 19 3
ex06 = 19 `mod` 3
ex07 = 7 ^ 222
ex08 = (-3) * (-7)

sumtorial :: Integer -> Integer
sumtorial 0 = 0
sumtorial n = n + sumtorial (n-1)

hailstone :: Integer -> Integer
hailstone n
  | n `mod` 2 == 0 = n `div` 2
  | otherwise      = 3*n + 1

p :: (Int, Char)
p = (3, 'x')

f :: Int -> Int -> Int -> Int
f x y z = x + y + z
ex17 = f 3 17 8

nums, range, range2 :: [Integer]
nums   = [1,2,3,19]
range  = [1..100]
range2 = [2,4..100]

hello1 :: [Char]
hello1 = ['h', 'e', 'l', 'l', 'o']

intListLength :: [Integer] -> Integer
intListLength []     = 0
intListLength (x:xs) = 1 + intListLength xs -}

main :: IO ()

-- Excercise 1
toDigits :: Integer -> [Integer]
toDigits n
  | n > 0 = toDigits (n `div` 10) ++ [n `mod` 10]
  | otherwise = []

toDigitsRev :: Integer -> [Integer]
toDigitsRev n
  | n > 0     = n `mod` 10 : toDigitsRev (n `div` 10)
  | otherwise = []


-- Excercise 2
doubleEveryOther :: [Integer] -> [Integer]
doubleEveryOther (reverse -> (x:y:zs)) =
  doubleEveryOther (reverse zs) ++ [2*y, x]
doubleEveryOther _ = []

-- Excercise 3
sumDigits :: [Integer] -> Integer
sumDigits lst = sum $ map (sum . toDigits) lst

-- Excercise 4
validate :: Integer -> Bool
validate n
  | n > 0     = mod (sumDigits . doubleEveryOther . toDigits $ n) 10 == 0
  | otherwise = False

main = do
    print(toDigits 1234)
    print(toDigitsRev 1234)
    print(sumDigits [1, 16, 2, 5])
    print(validate 4012888888881881)
    -- print(digitsList 23)
    -- digitsList :: Integer -> [Integer]
    -- digitsList n = [n, n-1, n-2]
