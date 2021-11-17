{-# OPTIONS_GHC -Wall #-}

module Main where 
import Parser
import ExprT

{- f :: a -> a -> a
f a1 a2 = case (typeOf a1) of
            Int  -> a1 + a2
            Bool -> a1 && a2
            _    -> a1 -}

f1 :: a -> a -> a
f1 x y = x

f2 :: a -> a -> a
f2 x y = y

{- class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool -}

data Foo = F Int | G Char

instance Eq Foo where
  (F i1) == (F i2) = i1 == i2
  (G c1) == (G c2) = c1 == c2
  _ == _ = False

  foo1 /= foo2 = not (foo1 == foo2)

{- class Functor f where
    fmap :: (a -> b) -> f a -> f b -}

--instance Functor Maybe where
  --fmap _ Nothing  = Nothing
  --fmap h (Just a) = Just (h a)

-- instance Functor [] where
  --fmap _ []     = []
  --fmap f (x:xs) = f x : fmap f xs
  -- or just
  -- fmap = map

-- Response
-- The response talks how haskell has very few libraries, however the libraries
-- that are available, have a lot of detail. In addition to this, Haskell is concise
-- and defined that if it compiles, it is most likely correct. 

-- Excercise One
eval :: ExprT -> Integer
eval (ExprT.Lit x) = x
eval (ExprT.Add x y) = eval x + eval y
eval (ExprT.Mul x y) = eval x * eval y

-- Excercise Two
evalStr :: String -> Maybe Integer
evalStr = fmap eval . parseExp ExprT.Lit ExprT.Add ExprT.Mul

-- Exercise 3
class Expr x where
  lit :: Integer -> x
  add :: x -> x -> x
  mul :: x -> x -> x

instance Expr ExprT where
  lit x   = Lit x
  add a b = Add a b
  mul a b = Mul a b

reify :: ExprT -> ExprT
reify = id


main = do 
    print(eval (Mul (Add (Lit 2) (Lit 3)) (Lit 4)))
    print(reify $ mul (add (lit 2) (lit 3)) (lit 4))
    

