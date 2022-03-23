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
