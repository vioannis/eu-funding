\##Plots

PLOTS:

<<<<<<< HEAD

```{r echo=FALSE,message=FALSE,warning=FALSE}
rm(list = ls())
options(scipen=999)
install.packages(c("httr", "jsonlite"))
require("knitr")
require("httr")
require("RSocrata")
require("jsonlite")
require("ggplot2")
require("dplyr")
require("RSocrata")
require("tidyverse")
require("sf")
require("eurostat")
require("geometry")

###### get funding data from EU commission
res <- GET("https://cohesiondata.ec.europa.eu/resource/tc55-7ysv.json?$limit=40000")
data_funding <- fromJSON(rawToChar(res$content))
data_funding$modelled_annual_eu_payments <- as.numeric(data_funding$modelled_annual_eu_payments)/1000000000
###### aggregate 
funding_average <- aggregate(modelled_annual_eu_payments~country,data_funding,sum)

period_average <- aggregate(modelled_annual_eu_payments~programming_period,data_funding,sum)

funding_average_period <- aggregate(modelled_annual_eu_payments~country+programming_period,data_funding,sum)


(p1 <- ggplot(funding_average, aes(reorder(country,-modelled_annual_eu_payments),modelled_annual_eu_payments )) +
  coord_flip() +
  geom_bar(stat="identity", width=.90) + 
  xlab("") + # Set axis labels
  ylab("") + 
  ggtitle("total funding by country since 1989 in billion euro") + 
  theme_minimal())

(p2 <- ggplot(period_average, aes(reorder(programming_period,-modelled_annual_eu_payments),modelled_annual_eu_payments )) +
  coord_flip() +
  geom_bar(stat="identity", width=.90) + 
  xlab("") + # Set axis labels
  ylab("") + 
  ggtitle("total funding by programming period in billion euro") + 
  theme_minimal())

(p3 <- ggplot(funding_average_period[funding_average_period$programming_period=="1989-1993",], aes(reorder(country,-modelled_annual_eu_payments),modelled_annual_eu_payments )) +
  coord_flip() +
  geom_bar(stat="identity", width=.90) + 
  xlab("") + # Set axis labels
  ylab("") + 
  ggtitle("total funding by country 1989-1993 in billion euro") + 
  theme_minimal())


(p4 <- ggplot(funding_average_period[funding_average_period$programming_period=="2014-2020",], aes(reorder(country,-modelled_annual_eu_payments),modelled_annual_eu_payments )) +
  coord_flip() +
  geom_bar(stat="identity", width=.90) + 
  xlab("") + # Set axis labels
  ylab("") + 
  ggtitle("total funding by country since 2014-2020 in billion euro") + 
  theme_minimal())


# Download geospatial data from GISCO
data_geo <- get_eurostat_geospatial(resolution = "60", nuts_level = "0", year = 2021)

# merge with attribute data with geodata
data <- merge(data_geo,funding_average, by.x="NUTS_ID",by.y="country")
data$cat <- cut_to_classes(data$modelled_annual_eu_payments)

## Joining, by = "geo"
(p5 <- ggplot(data = data) +
  geom_sf(aes(fill = cat), size = 0.1) +
  scale_fill_brewer(palette = "Oranges") +
  guides(fill = guide_legend(reverse = TRUE, title = "billion euro")) +
  labs(
    title = "Total fiscal transfers",
    caption = ""
  ) +
  theme_light() +
  theme() +
  coord_sf(xlim = c(-12, 44), ylim = c(35, 70)))

```

![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-1-1.png)
=======
![](README_files/figure-markdown_strict/pressure-1.png)![](README_files/figure-markdown_strict/pressure-2.png)![](README_files/figure-markdown_strict/pressure-3.png)![](README_files/figure-markdown_strict/pressure-4.png)
>>>>>>> f9b7acd307783f20926888ffb58a72f0bfd8ce7d
