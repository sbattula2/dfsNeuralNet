library(gsubfn)
library(stringi)
library(rvest)

getListOfPlayers<-function(){
  
  TRANSLIT = list(    'S'='S', 's'='s', 'Z'='Z', 'z'='z', 'À'='A', 'Á'='A', 'Â'='A', 'Ã'='A', 'Ä'='A', 'Å'='A', 'Æ'='A', 'Ç'='C', 'È'='E', 'É'='E',
                      'Ê'='E', 'Ë'='E', 'Ì'='I', 'Í'='I', 'Î'='I', 'Ï'='I', 'Ñ'='N', 'Ò'='O', 'Ó'='O', 'Ô'='O', 'Õ'='O', 'Ö'='O', 'Ø'='O', 'Ù'='U',
                      'Ú'='U', 'Û'='U', 'Ü'='U', 'Ý'='Y', 'Þ'='B', 'ß'='Ss', 'à'='a', 'á'='a', 'â'='a', 'ã'='a', 'ä'='a', 'å'='a', 'æ'='a', 'ç'='c',
                      'è'='e', 'é'='e', 'ê'='e', 'ë'='e', 'ì'='i', 'í'='i', 'î'='i', 'ï'='i', 'ð'='o', 'ñ'='n', 'ò'='o', 'ó'='o', 'ô'='o', 'õ'='o',
                      'ö'='o', 'ø'='o', 'ù'='u', 'ú'='u', 'û'='u', 'ý'='y', 'ý'='y', 'þ'='b', 'ÿ'='y' )
  
  
  dataHolder <-read_html("https://www.basketball-reference.com/leagues/NBA_2019_advanced.html")
  
  links <- dataHolder %>% html_nodes("th+ .left a") %>% html_attr("href")
  
  masterTable <- dataHolder%>%html_nodes("#advanced_stats")%>%html_table(fill=TRUE)
  
  print(masterTable)
  
  masterTable<-data.frame(masterTable)
  
  names<-masterTable[2]
  
  remove<-c()
  
  for(index in 1:length(names[,1])){
    
    if(names[index,1]=="Player"){
      remove<-c(remove,index)
    }
    
    names[index,1] = stri_trans_general(as.character(names[index,1]), "Latin-ASCII")  
  }
  
  print(names[,1])
  names<-names[-remove,]
  cT<-masterTable[-remove,]
  cT$links<-as.character(links)
  
  cT[2]<-names
  
  # pC <- data.frame("Name"=as.character(cT[2]),
  #                  "MP"=as.numeric(cT$Basic.Box.Score.Stats),
  #                  "FG"=as.numeric(cT$Basic.Box.Score.Stats.1),
  #                  "FGA"=as.numeric(cT$Basic.Box.Score.Stats.2),
  #                  "FT"=as.numeric(cT$Basic.Box.Score.Stats.7),
  #                  "FTA"=as.numeric(cT$Basic.Box.Score.Stats.8),
  #                  "ORB"=as.numeric(cT$Basic.Box.Score.Stats.10),
  #                  "DRB"=as.numeric(cT$Basic.Box.Score.Stats.11),
  #                  "AST"=as.numeric(cT$Basic.Box.Score.Stats.13),
  #                  "STL"=as.numeric(cT$Basic.Box.Score.Stats.14),
  #                  "BLK"=as.numeric(cT$Basic.Box.Score.Stats.15),
  #                  "TOV"=as.numeric(cT$Basic.Box.Score.Stats.16),
  #                  "FG%"=as.numeric(cT$Basic.Box.Score.Stats.3),
  #                  "3P"=as.numeric(cT$Basic.Box.Score.Stats.4),
  #                  "3PA"=as.numeric(cT$Basic.Box.Score.Stats.5),
  #                  "3P%"=as.numeric(cT$Basic.Box.Score.Stats.6),
  #                  "2P"=as.numeric(cT$Basic.Box.Score.Stats.1-cT$Basic.Box.Score.Stats.4),
  #                  "2PA"=as.numeric(cT$Basic.Box.Score.Stats.2-cT$Basic.Box.Score.Stats.5),
  #                  "2P%"=as.numeric((cT$Basic.Box.Score.Stats.1-cT$Basic.Box.Score.Stats.4)/(cT$Basic.Box.Score.Stats.2-cT$Basic.Box.Score.Stats.5)*100),
  #                  "FT%"=as.numeric(cT$Basic.Box.Score.Stats.9),
  #                  "PTS"=as.numeric(cT$Basic.Box.Score.Stats.18),
  #                  "links"=as.character(cT$links),
  #                  stringsAsFactors = FALSE)
  # 
  
  return(cT)
}

listPlayers<-getListOfPlayers()
print(listPlayers)
setwd("C:\\NBA DFS")
write.csv(listPlayers,"PlayerAdvanced.csv")