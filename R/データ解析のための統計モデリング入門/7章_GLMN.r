data <- read.csv("../working/R/データ解析のための統計モデリング入門/data/data.csv")
# X == 4
d4 <- data[data$x == 4, ]
table(d4$y)
c(mean(d4$y), var(d4$y))
glmmML(cbind(y, N - y) ~ x, data = data, family = binomial, cluster = id)