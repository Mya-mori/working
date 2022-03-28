#############################################################
data <- read.csv("../working/R/データ解析のための統計モデリング入門/data/data3a.csv")
fit_all <- glm(
    y ~ x + f,
    family = poisson,
    data = data
)
fit_all
#maximum log likelihood
logLik(fit_all)
#############################################################
log_d <- sum(log(dpois(data$y, lambda = data$y)))
#minimum log likelihood
d <- -2 * log_d ; d
#############################################################
#一定モデル
fit_null <- glm(
    y ~ 1,
    family = poisson,
    data = data
)
fit_null
#maximum log likelihood
max_d <- logLik(fit_null) * -2
#############################################################
#residual deviance
#D - (minimum log likelihood)
max_d - d
#############################################################
