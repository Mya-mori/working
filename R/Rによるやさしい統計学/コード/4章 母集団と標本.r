###############################################################################
#####                           4章 母集団と標本                          #####
###############################################################################
身長 <- runif(10, 150, 180)
var(身長)

#ceiling 小数点以下を切り下げ
サイコロ <- ceiling(runif(6, min=0, max=6))
table(サイコロ)

サイコロ2 <- ceiling(runif(10000000, min=0, max=6))
table(サイコロ2)

barplot(c(2/3, 1/3), names.arg=c("male", "female"))

#正規分布 N(0, 1^2)
curve(dnorm(x, mean=0, sd=1), from=-4, to=4)

#正規分布の比較
curve(dnorm(x, mean=0, sd=1), from=-4, to=4)
curve(dnorm(x, mean=1, sd=1), add=TRUE)
curve(dnorm(x, mean=0, sd=2), add=TRUE)

#無作為抽出
rnorm(n=10, mean=50, sd=10)

標本 <- rnorm(n=10, mean=50, sd=10)
hist(標本)

大標本　<- rnorm(n=1000000, mean=50, sd=10)
hist(大標本)

mean(標本)

#標本分布を求める
#モンテカルロ・シミュレーション
標本平均 <- numeric(length=100000)

for(i in 1:100000){
  標本 <- rnorm(n=10, mean=50, sd=10)
  標本平均[i] <- mean(標本)
}

hist(標本平均)

#誤差5以下
abs5以下 <- ifelse(abs(標本平均-50) <= 5, 1, 0)
table(abs5以下)

mean(標本平均)
var(標本平均)

hist(標本平均, freq=FALSE)
curve(dnorm(x, mean=50, sd=sqrt(10)), add=TRUE)

#標本分散と不偏分散の標本分布
標本分散 <- numeric(length=100000)
不偏分散 <- numeric(length=100000)

for(i in 1:100000){
  標本 <- rnorm(n=100, mean=50, sd=10)
  標本分散[i] <- mean((標本-mean(標本))^2)
  不偏分散[i] <- var(標本)
}

mean(標本分散)
mean(不偏分散)

sd(標本分散)
sd(不偏分散)

hist(標本分散, breaks=seq(0, 500, 10))
hist(不偏分散, breaks=seq(0, 500, 10))

標本平均 <- numeric(length = 100000)
標本中央値 <- numeric(length = 100000)

for(i in 1:100000){
  標本 <- rnorm(n=10000, mean=50, sd=10)
  標本平均[i] <-mean(標本)
  標本中央値[i] <- median(標本)
}

mean(標本平均)
mean(標本中央値)

### 練習問題 ###
#(1)
標本平均 <- numeric(length=5000)

for(i in 1:5000){
  標本 <- rnorm(n=20, mean=50, sd=10)
  標本平均[i] <- mean(標本)
}
hist(標本平均, freq=FALSE)
curve(dnorm(x, mean=50, sd=sqrt(100/20)), add=TRUE)
