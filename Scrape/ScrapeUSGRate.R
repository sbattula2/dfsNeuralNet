library(rvest)


setwd("C:\\YDFS Project\\Data Prep")
longCol<-read.csv(file="playersList.csv", header=TRUE, sep=",")

getAdvancedStats<-function(playerNum){
  
  playerName<-longCol$Name[playerNum]
  playerRow<-longCol[playerNum,]
  precursor<-c("https://www.basketball-reference.com")
  
  truncatedPlayerLink<-substr(longCol$links[playerNum],1,nchar(as.character(longCol$links[playerNum]))-5)
  playerLink <-paste(precursor,truncatedPlayerLink,".html",sep="")
  
  print(playerNum)
  print(playerLink)
  
  readHT <-read_html(url(playerLink))
  gameLog <- readHT%>%html_nodes("#advanced")%>%html_table(fill=TRUE)
  
  logData<-data.frame(gameLog)
  
  print(logData)
  
  condLog<-data.frame("Season"=as.numeric(logData$Season),"Age"=as.numeric(logData$Age),
                      "TM"=as.numeric(logData$Tm),"PER"=as.numeric(logData$PER),
                      "USG"=as.numeric(logData[,ncol(logData)-9]))
  
  path<-("C:\\YDFS Project\\Data Prep\\Advanced\\")
  
  fileName<-paste(path,playerName,sep="")    
  fileName<-paste(fileName,".csv",sep="")
  
  write.csv(logData, file = fileName)
  }
  
for(index in 1:length(longCol$X)){
  if(index!=0 && index != 2 && index!=90 && index!=126&& index!=280&& index!=479){
    getAdvancedStats(index)
  }
}
