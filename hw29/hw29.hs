
class Monad m where
  return :: a -> m a

  (>>=) :: m a -> (a -> m b) -> m b

  (>>)  :: m a -> m b -> m b
  m1 >> m2 = m1 >>= \_ -> m2

  instance Monad Maybe where
  return  = Just
  Nothing >>= _ = Nothing
  Just x  >>= k = k x

  check :: Int -> Maybe Int
  check n | n < 10    = Just n
          | otherwise = Nothing
  
  halve :: Int -> Maybe Int
  halve n | even n    = Just $ n `div` 2
          | otherwise = Nothing
  
  ex01 = return 7 >>= check >>= halve
  ex02 = return 12 >>= check >>= halve
  ex03 = return 12 >>= halve >>= check

  instance Monad [] where
  return x = [x]
  xs >>= k = concat (map k xs)

  addOneOrTwo :: Int -> [Int]
  addOneOrTwo x = [x+1, x+2]
  
  ex04 = [10,20,30] >>= addOneOrTwo
