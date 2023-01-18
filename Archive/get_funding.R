rm(list = ls())
options(scipen=999)
install.packages(c("httr", "jsonlite"))
install.packages("RSocrata")
library(httr)
library(jsonlite)
library(ggplot2)
library(dplyr)
library(RSocrata)
res <- GET("https://cohesiondata.ec.europa.eu/resource/tc55-7ysv.json?$limit=40000")
data <- fromJSON(rawToChar(res$content))
data$modelled_annual_eu_payments <- as.numeric(data$modelled_annual_eu_payments)
###### aggregate 
funding_average <- aggregate(modelled_annual_eu_payments~country,data,sum)
funding_average <- funding_average[order(funding_average$)]


ggplot(funding_average, aes(country,modelled_annual_eu_payments , Freq,  fill=country)) + 
  coord_flip() +
  geom_bar(stat="identity", width=.90) + 
  xlab("") + # Set axis labels
  ylab("") + 
  guides(fill=FALSE) +
  ggtitle("funding by country since 1989") + 
  theme_minimal()



ggplot(funding_average, aes(country,modelled_annual_eu_payments , Freq,  fill=country)) + 
  coord_flip() +
  geom_bar(stat="identity", width=.90) + 
  xlab("") + # Set axis labels
  ylab("") + 
  guides(fill=FALSE) +
  ggtitle("funding by country since 1989") + 
  theme_minimal()



