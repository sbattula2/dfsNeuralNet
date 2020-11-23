  library(rvest)
  
  setwd("C:\\NBA DFS")
  longCol<-read.csv(file="PlayerDirectory.csv", header=TRUE, sep=",")
  
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
    
    if(length(logData$ORB)>0){
      for(index in 1:length(logData$ORB)){
        if(logData$ORB[index]=="ORB"||logData$ORB[index]=="Inactive"||logData$ORB[index]=="Did Not Play"||logData$ORB[index]=="Not With Team"||logData$ORB[index]=="Did Not Dress"||logData$ORB[index]=="Player Suspended"){
          headerIndex<-c(headerIndex,index)
        }
      }
      
      
      if(length(headerIndex)>0){
        logData<-logData[-headerIndex,]
      }
      condLog<-data.frame("ORB"=as.numeric(logData$ORB),"DRB"=as.numeric(logData$DRB),
                          "AST"=as.numeric(logData$AST),"STL"=as.numeric(logData$STL),
                          "BLK"=as.numeric(logData$BLK),"TOV"=as.numeric(logData$TOV),"PTS"=as.numeric(logData$PTS),
                          "FG"=as.numeric(logData$FG),"FGA"=as.numeric(logData$FGA),"FT"=as.numeric(logData$FT)
                          ,"FTA"=as.numeric(logData$FTA),"MP"=as.numeric(substr(logData$MP,1,nchar(logData$MP)-3)))
      
      condLog$FPTS<-as.numeric(condLog$ORB)*1.2+as.numeric(condLog$DRB)*1.2+as.numeric(condLog$AST)*1.25+as.numeric(condLog$STL)*3+as.numeric(condLog$BLK)*3-as.numeric(condLog$TOV)+as.numeric(condLog$PTS)
      logData$FPTS<-condLog$FPTS
      
      path<-("C:\\NBA DFS\\Game Logs\\")
      
      fileName<-paste(path,playerName,sep="")    
      fileName<-paste(fileName,".csv",sep="")
      
      print(playerName)
      write.csv(logData, file = fileName)
    }
   
     
    
  }
  
  setwd("C:\\NBA DFS\\Game Logs")
  
  for(index in 1:length(longCol$Player)){
    tryCatch({
      getMedianData2019(index)
    })
  }
