#############################################################
data <- read.csv("/Users/haratodaisuke/Library/Mobile Documents/com~apple~CloudDocs/working/R/データ解析のための統計モデリング入門/data/data3a.csv") # nolint
data
#列ごとのデータを取得
data$x
data$y
data$f
#データ型の確認
class(data)
class(data$y)
class(data$x)
class(data$f)
#サマリー
summary(data)
#############################################################
plot(data$x, data$y, pch = c(21, 19))
legend("topleft", legend = c("C", "T"), pch = c(21, 19))
#############################################################
#GLM
glm <- glm(formula = y ~ x, data = data, family = binomial)
help(glm)
#############################################################
fit <- glm(
    y ~ x,
    family = poisson(link = "log"),
    data = data
)
fit
logLik(fit)
#############################################################
plot(data$x, data$y, pch = c(21, 19))
xx <- seq(min(data$x), max(data$x), length = 100)
lines(xx, exp(1.29 + 0.0757 * xx), lwd = 2)
yy <- predict(fit, newdata = data.frame(x = xx))
lines(xx, yy, lwd = 2)
#############################################################
fit.f <- glm(
    y ~ f,
    family = poisson,
    data = data
)
fit.f
logLik(fit.f)
