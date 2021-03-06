  library(rvest)
  library(stringi)
  
  
  TRANSLIT = list(    'S'='S', 's'='s', 'Z'='Z', 'z'='z', '�'='A', '�'='A', '�'='A', '�'='A', '�'='A', '�'='A', '�'='A', '�'='C', '�'='E', '�'='E',
                      '�'='E', '�'='E', '�'='I', '�'='I', '�'='I', '�'='I', '�'='N', '�'='O', '�'='O', '�'='O', '�'='O', '�'='O', '�'='O', '�'='U',
                      '�'='U', '�'='U', '�'='U', '�'='Y', '�'='B', '�'='Ss', '�'='a', '�'='a', '�'='a', '�'='a', '�'='a', '�'='a', '�'='a', '�'='c',
                      '�'='e', '�'='e', '�'='e', '�'='e', '�'='i', '�'='i', '�'='i', '�'='i', '�'='o', '�'='n', '�'='o', '�'='o', '�'='o', '�'='o',
                      '�'='o', '�'='o', '�'='u', '�'='u', '�'='u', '�'='y', '�'='y', '�'='b', '�'='y' )
  
  
  df <- read.csv(file="C:/NBA DFS/dailyLinks.csv", header=TRUE, sep=",")
  setwd("C:/NBA DFS/Daily Leaders")
  
  for(index in 1:length(df[,1])){
    
    dH <- read_html(as.character(df$Link[index]))
    
    mT <- dH%>%html_nodes("#stats")%>%html_table(fill=TRUE)
    
    if(length(mT)>0){
    rT<-data.frame(mT)
  
    names<-rT[2]
    
    
    remove<-c()
    
    for(index2 in 1:length(names[,1])){
      
      if(names[index2,1]=="Player"){
        remove<-c(remove,index)
      }
      
      names[index2,1] = stri_trans_general(as.character(names[index2,1]), "Latin-ASCII")
      
    }
    
    if (length(remove)>0){
      print('Horse')
      cT<-rT[-remove,]
      clock<-as.numeric(substr(rT$MP,1,nchar(rT$MP)-3))
      cT$MP<-as.numeric(clock[-remove])
    }
    
    else{
      print('Scrpalsdf')
      cT<-rT
      cT$MP<-as.numeric(substr(rT$MP,1,nchar(rT$MP)-3))
    }
    
    
    clock<-as.numeric(substr(rT$MP,1,nchar(rT$MP)-3))
    
    cT$MP<-as.numeric(clock[-remove])
    #cT$MP<-clock
    
    needed <- data.frame("Name"=(cT$Player),"MP"=as.numeric(cT$MP),"FG"=as.numeric(cT$FG),
                         "FGA"=as.numeric(cT$FGA),
                         "FT"=as.numeric(cT$FT),
                         "FTA"=as.numeric(cT$FTA),
                         "ORB"=as.numeric(cT$ORB),
                         "DRB"=as.numeric(cT$DRB),
                         "AST"=as.numeric(cT$AST),
                         "STL"=as.numeric(cT$STL),
                         "BLK"=as.numeric(cT$BLK),
                         "TOV"=as.numeric(cT$TOV)
                         ,"PTS"=as.numeric(cT$PTS),
                         stringsAsFactors = FALSE)
    
    
    longFP<-((needed$ORB*1.2)+(needed$DRB*1.2)+(needed$AST*1.5)+
               (needed$STL*3)+(needed$BLK*3)+(needed$PTS)-(needed$TOV))
    
    needed$FPTS<-longFP
    fileName = paste(as.character(df$File[index]),"",sep="")
    #print(fileName)
    
    print(substring(as.character(df$File[index]),1,1))
    print(index)
    
    write.csv(needed,file = fileName)
    #print('saved')
    
    }
      
  else{
    print(df$File[index])
    print('no good')
  }
    
  
  }
  
