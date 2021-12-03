#!/usr/bin/Rscript --vanilla

x <- c(2.1, 4.2, 3.3, 5.4)
x[order(x)]

a <- matrix(1:9, nrow = 3)
colnames(a) <- c("A", "B", "C")
a[1:2, ]

a[c(TRUE, FALSE, TRUE), c("B", "A")]
a[0, -2]

df <- data.frame(x = 1:3, y = 3:1, z = letters[1:3])

df[df$x == 2, ]

df[c(1, 3), ]

df[c("x", "z")]

df[, c("x", "z")]

a <- list(a = 1, b = 2)
a[[1]]
a[["a"]]

x <- list(abc = 1)
x$a




#Exercise 1
#mtcars[mtcars$cyl = 4, ]
#mtcars[mtcars$cyl == 4, ]

#mtcars[-1:4, ]
#mtcars[-(1:4), ]

#mtcars[mtcars$cyl <= 5]
#mtcars[mtcars$cyl <= 5,]

#mtcars[mtcars$cyl == 4 | 6, ]
#mtcars[mtcars$cyl == c(4, 6), ]

#Exercise 4
#Why does mtcars[1:20] return an error? 
#How does it differ from the similar mtcars[1:20, ]?
#The first one is looking for 20 columns while the second goes to the rows


#Exercise 1
#How would you randomly permute the columns of a data frame? (This is an important technique in random forests.) Can you simultaneously permute the rows and columns in one step?
#using [ and sample()
#Yes you can simultaneously permute the row and column at the same time

#Exercise 2
#How would you select a random sample of m rows from a data frame? What if the sample had to be contiguous (i.e. with an initial row, a final row, and every row in between)?
#Subset with sample and [] to get a row
#we would get the start and final row and then subset with [:]

#Exercise 3
#We would use order and sort
#mtcars[order(names(mtcars))]
