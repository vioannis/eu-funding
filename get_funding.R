rm(list = ls())
options(scipen=999)
install.packages(c("httr", "jsonlite"))
install.packages("RSocrata")
library(httr)
library(jsonlite)
library("RSocrata")
res <- GET("https://cohesiondata.ec.europa.eu/resource/tc55-7ysv.json?$limit=40000")
#rawToChar(res$content)
data <- fromJSON(rawToChar(res$content))


###### aggregate 