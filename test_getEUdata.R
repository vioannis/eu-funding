#THIS IS JUST A TEST FOR GIT HUB ACTIONS, NO USE FOR THE ACTUAL TASK

rm(list = ls())
options(scipen=999)
install.packages(c("httr", "jsonlite"))
install.packages("RSocrata")
library(httr)
library(jsonlite)
library("RSocrata")
res <- GET("https://cohesiondata.ec.europa.eu/resource/tc55-7ysv.json?$limit=1000")
#rawToChar(res$content)
data <- fromJSON(rawToChar(res$content))

cat(sprintf("last update on %s.", as.character(Sys.Date())))

write.csv(data, paste0("/data/", format(Sys.time(), "%d-%b-%Y"), ".csv") )
