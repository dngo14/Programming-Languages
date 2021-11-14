{-# OPTIONS_GHC -Wall #-}

{-# LANGUAGE ViewPatterns #-}
module Main where 

data IntList = Empty | Cons Int IntList
  deriving Show

absAll :: IntList -> IntList
absAll Empty       = Empty
absAll (Cons x xs) = Cons (abs x) (absAll xs)

squareAll :: IntList -> IntList
squareAll Empty       = Empty
squareAll (Cons x xs) = Cons (x*x) (squareAll xs)

exampleList = Cons (-1) (Cons 2 (Cons (-6) Empty))

{- addOne x = x + 1
square x = x * x
mapIntList addOne exampleList
mapIntList abs    exampleList
mapIntList square exampleList -}

keepOnlyEven :: IntList -> IntList
keepOnlyEven Empty = Empty
keepOnlyEven (Cons x xs)
  | even x    = Cons x (keepOnlyEven xs)
  | otherwise = keepOnlyEven xs

data List t = E | C t (List t)
lst1 :: List Int
lst1 = C 3 (C 5 (C 2 E))

lst2 :: List Char
lst2 = C 'x' (C 'y' (C 'z' E))

lst3 :: List Bool
lst3 = C True (C False E)

filterList _ E = E
filterList p (C x xs)
  | p x       = C x (filterList p xs)
  | otherwise = filterList p xs

doStuff1 :: [Int] -> Int
doStuff1 []  = 0
doStuff1 [_] = 0
doStuff1 xs  = head xs + (head (tail xs)) 
doStuff2 :: [Int] -> Int
doStuff2 []        = 0
doStuff2 [_]       = 0
doStuff2 (x1:x2:_) = x1 + x2

data NonEmptyList a = NEL a [a]

nelToList :: NonEmptyList a -> [a]
nelToList (NEL x xs) = x:xs

listToNel :: [a] -> Maybe (NonEmptyList a)
listToNel []     = Nothing
listToNel (x:xs) = Just $ NEL x xs

headNEL :: NonEmptyList a -> a
headNEL (NEL a _) = a

tailNEL :: NonEmptyList a -> [a]
tailNEL (NEL _ as) = as

-- Excercise 1
every :: Int -> [a] -> [a]
every 0 _ = []
every 1 xs = xs
every n xs = every2 1 n xs
  where 
    every2 :: Int -> Int -> [a] -> [a]
    every2 _ _ [] = []
    every2 cur n(x:xs)
      | cur == n = x : every2 1 n xs
      | otherwise = every2 (cur+1) n xs

skips :: [a] -> [[a]]
skips [] = []
skips xs = skips2 1 (length xs) xs
  where
    skips2 :: Int -> Int -> [a] -> [[a]]
    skips2 n len xs
      | n > len = []
      | otherwise = every n xs : skips2 (n+1) len xs
--Excercise 2

localMaxima :: [Integer] -> [Integer]
localMaxima [] = []
localMaxima [x] = []
localMaxima [x,y] = []
localMaxima (x:y:z:xs)
  | y > x && y > z = y : localMaxima (y:z:xs)
  | otherwise = localMaxima (y:z:xs)

main = do
  print(skips "ABCD")
  print(every 2 [1..10])
  print(localMaxima [2,9,5,6,1])