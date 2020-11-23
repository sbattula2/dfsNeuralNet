getListOfPlayers<-function(){
  
  library(rvest)
  
  dataHolder <-read_html("https://www.basketball-reference.com/leagues/NBA_2019_per_game.html")
  
  links <- dataHolder %>% html_nodes("th+ .left a") %>% html_attr("href")
  
  masterTable <- dataHolder%>%html_nodes("#per_game_stats")%>%html_table(fill=TRUE)
  
  print(masterTable)
  
  masterTable<-data.frame(masterTable)
  
  names<-masterTable[2]
  
  remove<-c()
  
  for(index in 1:length(names[,1])){
    
    if(names[index,1]=="Player"){
      remove<-c(remove,index)
    }
    
    
  }
  
  cT<-masterTable[-remove,]
  cT$links<-as.character(links)
  
  
  pC <- data.frame("Name"=as.character(cT$Player),
                   "MP"=as.numeric(cT$MP),
                   "FG"=as.numeric(cT$FG),
                   "FGA"=as.numeric(cT$FGA),
                   "FT"=as.numeric(cT$FT),
                   "FTA"=as.numeric(cT$FTA),
                   "ORB"=as.numeric(cT$ORB),
                   "DRB"=as.numeric(cT$DRB),
                   "AST"=as.numeric(cT$AST),
                   "STL"=as.numeric(cT$STL),
                   "BLK"=as.numeric(cT$BLK),
                   "TOV"=as.numeric(cT$TOV)
                   ,"PTS"=as.numeric(cT[,ncol(cT)-1]),
                   "links"=as.character(cT$links),
                   stringsAsFactors = FALSE)
  
  
  return(pC)
}

listPlayers_2017<-getListOfPlayers()
print(listPlayers_2017)
setwd("C:\\YDFS Project\\Data Prep\\Player Directory")
write.csv(listPlayers_2017,"playersList.csv")