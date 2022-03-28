#############################################################
d <- read.csv("../working/R/データ解析のための統計モデリング入門/data/data3a.csv")
#############################################################
#一定モデル
fit1 <- glm(
    y ~ 1,
    family = poisson,
    data = d
)
#############################################################
fit2 <- glm(
    y ~ x,
    family = poisson,
    data = d
)
#############################################################
#residual deviance 残差逸脱度
fit2$deviance
#############################################################
#ΔD_1_2
fit1$deviance - fit2$deviance
#############################################################
#sample d
d$y_rnd <- rpois(100, lambda = mean(d$y))
#############################################################
fit1 <- glm(y_rnd ~ 1, family = poisson, data = d)
fit2 <- glm(y_rnd ~ x, family = poisson, data = d)
fit1$deviance - fit2$deviance
#############################################################
#検定統計量の分布
get_pb <- function(d)
{
    n_sample <- nrow(d) #number of d
    y_mean <- mean(d$y) # nolint
    d$y_rnd <- rpois(n_sample, lambda = y_mean)
    fit1 <- glm(y_rnd ~ 1, data = d, family = poisson)
    fit2 <- glm(y_rnd ~ x, data = d, family = poisson)
    fit1$deviance - fit2$deviance
}

pb <- function(d, n_bootstrap)
{
    replicate(n_bootstrap, get_pb(d))
}

#サンプルデータ1000件
dd12 <- pb(d, n_bootstrap = 1000)
summary(dd12)
hist(dd12, 100)
abline(v = 4.5, lwd = 2)
#ΔD_1_2 >= 4.5
sum(dd12 >= 4.5)

quantile(dd12, 0.95)
