getListOfPlayers<-function(){
  
  library(rvest)
  
  dataHolder <-read_html("https://www.basketball-reference.com/leagues/NBA_2019_advanced.html")
  
  links <- dataHolder %>% html_nodes("th+ .left a") %>% html_attr("href")
  
  masterTable <- dataHolder%>%html_nodes("#advanced_stats")%>%html_table(fill=TRUE)
  
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
                   "G"=as.numeric(cT[,6]),
                   "MP"=as.numeric(cT[,7]),
                   "PER"=as.numeric(cT[,8]),
                   "TS%"=as.numeric(cT[,9]),
                   "3PAr"=as.numeric(cT[,10]),
                   "FTr"=as.numeric(cT[,11]),
                   "ORB"=as.numeric(cT[,12]),
                   "AST"=as.numeric(cT[,13]),
                   "STL"=as.numeric(cT[,14]),
                   "BLK"=as.numeric(cT[,15]),
                   "TOV"=as.numeric(cT[,16]),
                   "USG"=as.numeric(cT[,19]),
                   "OWS"=as.numeric(cT[,18]),
                   "DWS"=as.numeric(cT[,19]),
                   "WS"=as.numeric(cT[,20]),
                   "WS48"=as.numeric(cT[,21]),
                   "OBPM"=as.numeric(cT[,22]),
                   "DBPM"=as.numeric(cT[,23]),
                   "BPM"=as.numeric(cT[,24]),
                   stringsAsFactors = FALSE)
  
  return(pC)
}

listPlayers_2017<-getListOfPlayers()
setwd("C:\\YDFS Project\\Data Prep")
write.csv(listPlayers_2017,"advancedLogs.csv")

