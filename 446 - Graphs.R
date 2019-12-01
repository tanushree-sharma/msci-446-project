# loading in data
data <- read.csv("/Users/tonili/Desktop/446 Data.csv", header=FALSE)

# converting data into numerical values
x <- as.numeric(unlist(data))

# plotting histogram
hist(x, main = "Residual Distribution", xlab = "Residual Error in Y")