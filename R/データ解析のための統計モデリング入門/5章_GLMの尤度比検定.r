#############################################################
data <- read.csv("/Users/haratodaisuke/Library/Mobile Documents/com~apple~CloudDocs/working/R/データ解析のための統計モデリング入門/data/data3a.csv")
#############################################################
#一定モデル
fit1 <- glm(
    y ~ 1,
    family = poisson,
    data = data
)
#############################################################
fit2 <- glm(
    y ~ x,
    family = poisson,
    data = data
)
#############################################################
#residual deviance 残差逸脱度
fit2$deviance
#############################################################
#ΔD_1_2
fit1$deviance - fit2$deviance
#############################################################
#sample data
data$y_rnd <- rpois(100, lambda = mean(data$y))
#############################################################
fit1 <- glm(y_rnd ~ 1, family = poisson, data = data)
fit2 <- glm(y_rnd ~ x, family = poisson, data = data)
fit1$deviance - fit2$deviance
#############################################################
#検定統計量の分布
get_pb <- function(data)
{
    n_sample <- nrow(data) #number of data
    y_mean <- mean(data$y)
    data$y_rnd <- rpois(n_sample, lambda = y_mean)
    fit1 <- glm(y_rnd ~ 1, data = data, family = poisson)
    fit2 <- glm(y_rnd ~ x, data = data, family = poisson)
    fit1$deviance - fit2$deviance
}

pb <- function(d, n_bootstrap)
{
    replicate(n_bootstrap, get_pb(d))
}

dd12 <- pb(d, n_bootstrap = 1000)
