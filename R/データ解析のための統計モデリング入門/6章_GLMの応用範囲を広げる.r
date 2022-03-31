#############################################################
d <- read.csv("../working/R/データ解析のための統計モデリング入門/data/data4a.csv")
#summary
summary(d)
#N 観察種子数, y 生存種数, x 体のサイズ, f 施肥処理
plot(d$x, d$y, pch = c(21, 19))
#############################################################
#logistic function
logistic <- function(z) {
    1 / (1 + exp(-z))
}
z <- seq(-8, 8, 0.1)
plot(z, logistic(z), lwd = 2)
#############################################################
fit_xf <- glm(cbind(y, N - y) ~ x + f, data = d, family = binomial)
library(MASS)
stepAIC(fit_xf)
#############################################################
glm(cbind(y, N - y) ~ x * f, data = d, family = binomial)
glm(y ~ x, offset = x, data = d, family = poisson)
#############################################################
y <- seq(-5, 5, 0.1)
plot(y, dnorm(y, mean = 0, sd = 1), type = "l")
#area
pnorm(1.8, mean = 0, sd = 1) - pnorm(1.2, mean = 0, sd = 1)