library(rvest)

teamID <- read.csv("C:\\NBA DFS\\TeamID.csv", header=TRUE)


for(i in 1:length(teamID$ABB_REF)){ 
  teamName<-teamID$ABB_REF[i]
  teamLower<-sapply(teamName,tolower)
  
  print(teamName)
  
  tpp <- 'C:\\NBA DFS\\Team Boxscores\\'
  tbPath<-paste(tpp,teamName,sep="")
  tbPath<-paste(tbPath,".csv",sep="")
    
  boxScore <- read.csv(tbPath, header=TRUE)
  away=0
  
  for(j in 1:length(boxScore$HOME)){
    
    date<-gsub("[[:punct:]]", "", boxScore$DATE[j])
    date<-paste(date,0,sep="")
    link<-"https://www.basketball-reference.com/boxscores/"
    post<-paste(date,teamName,sep="")
    post<-paste(post,".html",sep="")
    
    if(boxScore$HOME[j]=="True"){    
      
      link<-paste(link,post,sep="")
      print(link)

      tableXpath<-as.character(boxScore$XPATH[j])
      cT<-scrapeTable(link,tableXpath)
      
      #Save in home folder of team
      pathToSave<-"C:\\NBA DFS\\Basic Box Scores\\"
      pathToSave<-paste(pathToSave,teamName,sep="")
      pathToSave<-paste(pathToSave,"\\Home\\",sep="")
      
      
      fileName="Game"
      fileName=paste(fileName,teamName,sep="")
      fileName=paste(fileName,date,sep="")
      fileName=paste(fileName,".csv",sep="")
      fileName=paste(pathToSave,fileName,sep="")
      
      pC <- data.frame("Starters"=as.character(cT[,1]),
                       "MP"=as.character(cT[,2]),
                       "FG"=as.numeric(cT[,3]),
                       "FGA"=as.numeric(cT[,4]),
                       "FG%"=as.numeric(cT[,5]),
                       "3P"=as.numeric(cT[,6]),
                       "3PA"=as.numeric(cT[,7]),
                       "3P%"=as.numeric(cT[,8]),
                       "FT"=as.numeric(cT[,9]),
                       "FTA"=as.numeric(cT[,10]),
                       "FT%"=as.numeric(cT[,11]),
                       "ORB"=as.numeric(cT[,12]),
                       "DRB"=as.numeric(cT[,13]),
                       "TRB"=as.numeric(cT[,14]),
                       "AST"=as.numeric(cT[,15]),
                       "STL"=as.numeric(cT[,16]),
                       "BLK"=as.numeric(cT[,17]),
                       "TOV"=as.numeric(cT[,18]),
                       "PF"=as.numeric(cT[,19]),
                       "PTS"=as.numeric(cT[,20]),
                       "PM"=as.numeric(cT[,21]),
                       stringsAsFactors = FALSE)
      
      pC<-pC[-c(1,7),]
      
      write.csv(pC, file = fileName,row.names=TRUE)
      
    }
    
    else{
      opp<-boxScore$OPP[j]
      oppLower<-sapply(opp,tolower)
      post<-paste(date,opp,"",sep="")
      post<-paste(post,".html",sep="")
      link<-paste(link,post,"",sep="")
    
      tableXpath<-as.character(boxScore$XPATH[j])
      
      #Save in away folder of team
      cT<-scrapeTable(link,tableXpath)
      
      pathToSave<-"C:\\NBA DFS\\Basic Box Scores\\"
      pathToSave<-paste(pathToSave,teamName,sep="")
      pathToSave<-paste(pathToSave,"\\Away\\",sep="")
      
      print(link)
      
      fileName="Game"
      fileName=paste(fileName,teamName,sep="")
      fileName=paste(fileName,date,sep="")
      fileName=paste(fileName,".csv",sep="")
      fileName=paste(pathToSave,fileName,sep="")
      
      pC <- data.frame("Starters"=as.character(cT[,1]),
                       "MP"=as.character(cT[,2][]),
                       "FG"=as.numeric(cT[,3]),
                       "FGA"=as.numeric(cT[,4]),
                       "FG%"=as.numeric(cT[,5]),
                       "3P"=as.numeric(cT[,6]),
                       "3PA"=as.numeric(cT[,7]),
                       "3P%"=as.numeric(cT[,8]),
                       "FT"=as.numeric(cT[,9]),
                       "FTA"=as.numeric(cT[,10]),
                       "FT%"=as.numeric(cT[,11]),
                       "ORB"=as.numeric(cT[,12]),
                       "DRB"=as.numeric(cT[,13]),
                       "TRB"=as.numeric(cT[,14]),
                       "AST"=as.numeric(cT[,15]),
                       "STL"=as.numeric(cT[,16]),
                       "BLK"=as.numeric(cT[,17]),
                       "TOV"=as.numeric(cT[,18]),
                       "PF"=as.numeric(cT[,19]),
                       "PTS"=as.numeric(cT[,20]),
                       "PM"=as.numeric(cT[,21]),
                       stringsAsFactors = FALSE)
      
      pC<-pC[-c(1,7),]
      
      write.csv(pC, file = fileName,row.names=TRUE)
    
    } 
    
  }
}

scrapeTable<-function(link,element){
  readHT <-read_html((link))
  box <- readHT%>%html_nodes(xpath=element)%>%html_table(fill=TRUE)  
  boxTable<-data.frame(box)
  
  return(boxTable)
  
}








