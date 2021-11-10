{-# OPTIONS_GHC -Wall #-}
module Main where
import Log

{- parseMessage :: String -> String
parseMessage line -- = let singlewords = words line 
    | (singlewords!!0 == "I") = "I"
    | (singlewords!!0 == "W") = "W"
    | (singlewords!!0 == "E") = "E"
    | otherwise = "U"
    where singlewords = words line

main :: IO ()
main = do 
    print(parseMessage "E 2 562 help help") -}

join sep xs = foldr (\a b-> a ++ if b=="" then b else sep ++ b) "" xs

parseMessage :: String -> LogMessage
parseMessage line -- = let singlewords = words line 
    | (head singlewords == "I") = LogMessage Info (read (singlewords!!1) :: Int) (join " " (drop 2 singlewords))
    | (head singlewords == "W") = LogMessage Info (read (singlewords!!1) :: Int) (join " " (drop 2 singlewords))
    | (head singlewords == "E") = LogMessage (Error (read (singlewords!!1) :: Int)) (read (singlewords!!2) :: Int) (join " " (drop 3 singlewords))
    | otherwise = Unknown (join " " singlewords)
    where singlewords = words line

parse :: String -> [LogMessage]
parse = map parseMessage . lines

insert :: LogMessage -> MessageTree -> MessageTree
insert lmsg@LogMessage{} Leaf = Node Leaf lmsg Leaf 
insert lmsg1@(LogMessage _ ts1 _) (Node left lmsg2@(LogMessage _ ts2 _) right)
  | ts1 > ts2 = Node left lmsg2 (insert lmsg1 right)
  | otherwise = Node (insert lmsg1 left) lmsg2 right
insert _ tree = tree

build :: [LogMessage] -> MessageTree
build = foldr insert Leaf

inOrder :: MessageTree -> [LogMessage]
inOrder Leaf = []
inOrder (Node left lmsg right) = inOrder left ++ [lmsg] ++ inOrder right

main :: IO ()
main = do 
    print(parseMessage "E 2 562 help help")
    print(parseMessage "I 29 la la la")
    print(parseMessage "This is not in the right format")
    print(testParse parse 10 "error.log")

