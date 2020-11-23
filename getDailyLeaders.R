  library(rvest)
  library(stringi)
  
  
  TRANSLIT = list(    'S'='S', 's'='s', 'Z'='Z', 'z'='z', 'À'='A', 'Á'='A', 'Â'='A', 'Ã'='A', 'Ä'='A', 'Å'='A', 'Æ'='A', 'Ç'='C', 'È'='E', 'É'='E',
                      'Ê'='E', 'Ë'='E', 'Ì'='I', 'Í'='I', 'Î'='I', 'Ï'='I', 'Ñ'='N', 'Ò'='O', 'Ó'='O', 'Ô'='O', 'Õ'='O', 'Ö'='O', 'Ø'='O', 'Ù'='U',
                      'Ú'='U', 'Û'='U', 'Ü'='U', 'Ý'='Y', 'Þ'='B', 'ß'='Ss', 'à'='a', 'á'='a', 'â'='a', 'ã'='a', 'ä'='a', 'å'='a', 'æ'='a', 'ç'='c',
                      'è'='e', 'é'='e', 'ê'='e', 'ë'='e', 'ì'='i', 'í'='i', 'î'='i', 'ï'='i', 'ð'='o', 'ñ'='n', 'ò'='o', 'ó'='o', 'ô'='o', 'õ'='o',
                      'ö'='o', 'ø'='o', 'ù'='u', 'ú'='u', 'û'='u', 'ý'='y', 'ý'='y', 'þ'='b', 'ÿ'='y' )
  
  
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
  
