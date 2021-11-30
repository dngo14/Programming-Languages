#!/usr/bin/Rscript --vanilla
print('hello world')

dbl_var <- c(1, 2.5, 4.5)
int_var <- c(1L, 6L, 10L)
log_var <- c(TRUE, FALSE, T, F)
chr_var <- c("these are", "some strings")
typeof(int_var)
is.double(dbl_var)
str(c("a", 1))
x <- list(1:3, "a", c(TRUE, FALSE, TRUE), c(2.3, 5.9))
str(x)
y <- 1:10
attr(y, "my_attribute") <- "This is a vector"
attr(y, "my_attribute")
y <- c(a = 1, 2, 3)
names(y)
x <- factor(c("a", "b", "b", "a"))
a <- matrix(1:6, ncol = 3, nrow = 2)
b <- array(1:12, c(2, 3, 2))
df <- data.frame(x = 1:3, y = c("a", "b", "c"))
str(df)

# Exercise 1
#Logical, integer, double, character, complex and raw
#A list differs from an atomic vector in how their types can be of any type

#Exercise 2
#is.vector returns a bool and checks if the object is a vector with no attributes
#is.numeric just checks if it is a number of sorts
#is.list and is.charater actually checks if it is a list and or a character

#Exercise 3
c(1, FALSE)
#c(1, 0)
c("a", 1)
#("a", "1")
c(list(1), "a")
#(list(1), list("a"))
c(TRUE, 1L)
#(1,1)

#Exercise 4
#Since a list can contain elements of any type, thus it has to be unlisted first

#Exercise 5
#The first work because R converts FALSE to 0 and "1" to 1, while "one" cannot be changed to an integer

#Exercise 6
#NA is a constant of length 1 and because NA changes to the correct type

#Exercise 1
#Contains names, classes, and row.names

#Exercise 2
#It depends, if it has characters and numbers the numbers would change to characters
#If it has bools and numbers the bools would change to numbers

#Exercise 3
#Yes, you can