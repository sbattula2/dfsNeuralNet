library(rvest)
library(stringi)
#library(XML)
#library(RCurl)

PRE <-c("https://www.basketball-reference.com/teams/")
MID <-c("ATL","BOS","BRK","CHO","CHI",
        "DEN","DET","GSW","HOU","IND",
        "LAC","LAL","MEM","MIA","MIL",
        "MIN","NOP","NYK","OKC","ORL",
        "PHI","PHO","POR","SAC","SAS",
        "TOR","UTA","WAS","DAL","CLE")
POST<-c("/2020.html")

LINKS<-c()
for(abbrev in MID){
  LINKS<-c(LINKS,paste(PRE,abbrev,POST,sep=""))
}

downloadRosters<-function(){
  
  for(index in (1:length(MID))){
    
    readHT <-read_html((LINKS[index]))
    
    table <- readHT%>%html_nodes(xpath='//*[@id="roster"]')%>%html_table(fill=TRUE)

    roster<-data.frame(table)
    names = roster[2]
    
    for(ind in 1:length(names[,1])){
      names[ind,1] = stri_trans_general(as.character(names[ind,1]), "Latin-ASCII") 
    }
    
    roster[2]<-names
    
    print(LINKS[index])
    print(MID[index])
    
    filename<-paste(MID[index],".csv",sep="")
    write.csv(roster,file=filename)
    
  }
}

setwd("C:\\NBA DFS 2019\\Anthropomorphic\\")
downloadRosters()


# winshareData<-read.csv("C:\\Python Projects\\Yahoo Daily Fantasy\\Rosters\\teamData.csv")
#  
# getWinShareData<-function(teamName){
#   for(q in (1:length(winshareData$Team))){
#     if(winshareData$Team[q]==teamName){
#       return(winshareData[q,(3:8)])
#     }
#   }
# }
# nullRow<-function(){
#   nullDF<-data.frame("OWS_FC"=NA,"DWS_FC"=NA,"OWS_MC"=NA,"DWS_MC"=NA,"OWS_BC"=NA,"DWS_BC"=NA)
# }



