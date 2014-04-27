path <- "/Users/apple/Documents/kuaipan/快盘/coursera-project/Getting and Cleaning Data"
setwd(path)
data <- read.csv("getdata-data-ss06hid.csv")
logical <- data[data$ACR == 3 && data$AGS == 6,]
head(logical,3)

