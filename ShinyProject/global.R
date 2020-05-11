## global.R ##
library(shiny)
library(shinydashboard)
library(googleVis)
library(DT)
library(dplyr)
library(ggplot2)
library(tidyr)
library(tidyverse)
library(stringr)
library(lubridate)
library(zoo)
library(tm)
library(wordcloud)
library(memoise)
library(Cairo)
library(plotly)

# convert matrix to dataframe
steam_raw = read.csv("./steam.csv",stringsAsFactors = F)
steamraw = read.csv("./steam1.csv",stringsAsFactors = F)
steam_raw$release_date = as.Date(steam_raw$release_date) 
steamdata = steam_raw %>%
  mutate(unpacked1 = str_split(genres, ";")) %>% 
  unnest %>%
  mutate(genres_v2 = str_trim(unpacked1)) %>% 
  mutate(unpacked2 = str_split(categories, ";")) %>% 
  unnest %>%
  mutate(categories_v2 = str_trim(unpacked2)) %>% select(name,release_date,
                                                         developer,publisher,platforms, categories = categories_v2, genres = genres_v2,achievements,
                                                         positive_ratings,negative_ratings,average_playtime,price)






 # Data in the word cloud ####
# wordcloud_rep <- repeatable(wordcloud)
wordcloud  = steam_raw %>% group_by(developer) %>% summarise(number = n()) %>% arrange(.,desc(number))


#Data in the time tab ####
linetable = steam_raw %>% group_by(Release_date = as.yearqtr(release_date)) %>% summarise(Game_number = n()) 



#Bar chart of play time ####
avgtime = steamraw %>% arrange(.,desc(average_playtime)) %>% select(name,average_playtime) %>% head(.,20)
medtime = steamraw %>% arrange(.,desc(median_playtime)) %>% select(name,median_playtime) %>% head(.,20)


#Data in the platform tab ####
platformdf = steamdata %>% select(name,genres,platforms) %>% mutate(Platforms = str_split(platforms, ";")) %>%  unnest %>% group_by(Platforms,genres) %>% 
  summarise(Game_number = n()) %>% spread(key = genres,value = Game_number) 

bardata = steamdata %>% group_by(genres) %>% summarise(positive_ratings = sum(positive_ratings),negative_ratings = sum(negative_ratings))



#owners - time&price ####

price_owners = steam_raw %>% group_by(owners) %>% summarise(price = mean(price)) %>% 
  mutate(D=as.numeric(gsub("\\-.*","",owners)) ) %>% arrange(D) %>% select(-3)


time_owners = steam_raw %>% group_by(owners) %>% summarise(avgtime = mean(average_playtime)) %>% 
  mutate(D=as.numeric(gsub("\\-.*","",owners)) ) %>% arrange(D) %>% select(-3)
