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
