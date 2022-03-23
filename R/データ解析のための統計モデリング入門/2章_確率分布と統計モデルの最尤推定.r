#############################################################
data <- floor(runif(50, min = 0, max = 10))
#データ長
length(data)
#要約統計量
summary(data)
#度数分布
table(data)
#ヒストグラム
hist(data, breaks = 10, col = "red", main = "ヒストグラム")
#標本分散
var(data)
#標本標準偏差
sd(data)
sqrt(var(data))

#############################################################
y <- 0:9
#平均3.56のポアソン分布にしたがって、yが観測される確率
prob <- dpois(y, lambda = 3.56)
plot(y, prob, type = "l", xlab = "y", ylab = "p(y)")

#############################################################
logl <- function(m) sum(dpois(data, m, log = TRUE))
lambda <- seq(2, 5, 0.1)
plot(lambda, sapply(lambda, logl), type = "l")

#############################################################
box <- c()
for (i in 1:3000) {
    data <- rpois(50, 3.5)
    box <- c(box, mean(data))
}
hist(box, breaks = 20, col = "red")

#############################################################
data <- floor(runif(50, min = 0, max = 10))
data