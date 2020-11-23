library(rvest)
setwd("C:/NBA DFS/Daily Leaders/Monthly Schedules")

links<- c('https://www.basketball-reference.com/leagues/NBA_2019_games-october.html',
          'https://www.basketball-reference.com/leagues/NBA_2019_games-november.html',
          'https://www.basketball-reference.com/leagues/NBA_2019_games-december.html',
          'https://www.basketball-reference.com/leagues/NBA_2019_games-january.html',
          'https://www.basketball-reference.com/leagues/NBA_2019_games-february.html',
          'https://www.basketball-reference.com/leagues/NBA_2019_games-march.html',
          'https://www.basketball-reference.com/leagues/NBA_2019_games-april.html')

fileName <-c('schedOct.csv','schedNov.csv','schedDec.csv','schedJan.csv','schedFeb.csv','schedMar.csv','schedApr.csv')

for(index in 1:length(links)){
  
  dH <- read_html(as.character(links[index]))
  mT <- dH%>%html_nodes("#schedule")%>%html_table(fill=TRUE)
  rT<-data.frame(mT)
  
  write.csv(rT,file = fileName[index])
  
}

