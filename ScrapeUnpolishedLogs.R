library(rvest)

#setwd("C:\\NBA DFS")
setwd("C:\\NBA DFS\\Injuries\\Unpolished Gamelogs")

longCol<-read.csv(file="C:\\NBA DFS\\PlayerDirectory.csv", header=TRUE, sep=",")

getMedianData2019<-function(playerNum){
  
  playerName<-longCol$Player[playerNum]
  playerRow<-longCol[playerNum,]
  precursor<-c("https://www.basketball-reference.com")
  
  truncatedPlayerLink<-substr(longCol$links[playerNum],1,nchar(as.character(longCol$links[playerNum]))-5)
  playerLink <-paste(precursor,truncatedPlayerLink,"/gamelog/2019/",sep="")
  
  print(playerNum)
  print(playerLink)
  
  readHT <-read_html(url(playerLink))
  gameLog <- readHT%>%html_nodes("#pgl_basic")%>%html_table(fill=TRUE)
  
  logData<-data.frame(gameLog)
  
  headerIndex<-c()
  
  # if(length(logData$ORB)>0){
  #   for(index in 1:length(logData$ORB)){
  #     if(logData$ORB[index]=="ORB"||logData$ORB[index]=="Inactive"||
  #        logData$ORB[index]=="Did Not Play"||logData$ORB[index]=="Not With Team"||logData$ORB[index]=="Did Not Dress"
  #        ||logData$ORB[index]=="Player Suspended"){
  #       headerIndex<-c(headerIndex,index)
  #     }
  #   }
  #   
    
    #logData<-logData[-headerIndex,]
    
    condLog<-data.frame("ORB"=(logData$ORB),"DRB"=(logData$DRB),
                        "AST"=(logData$AST),"STL"=(logData$STL),
                        "BLK"=(logData$BLK),"TOV"=(logData$TOV),"PTS"=(logData$PTS),
                        "FG"=(logData$FG),"FGA"=(logData$FGA),"FT"=(logData$FT)
                        ,"FTA"=(logData$FTA),"MP"=logData$MP)
    
    #condLog$FPTS<-as.numeric(condLog$ORB)*1.2+as.numeric(condLog$DRB)*1.2+as.numeric(condLog$AST)*1.25+as.numeric(condLog$STL)*3+as.numeric(condLog$BLK)*3-as.numeric(condLog$TOV)+as.numeric(condLog$PTS)
    #logData$FPTS<-condLog$FPTS
    
    path<-("")
    fileName<-paste(path,playerName,sep="")    
    fileName<-paste(fileName,".csv",sep="")
    
    print(logData)
    
    write.csv(logData, file = fileName)
  }


for(index in 622:length(longCol$FTA)){
  if(index!=0 && index != 2 && index!=90 && index!=126&& index!=280&& index!=479){
    getMedianData2019(index)
  }
}
