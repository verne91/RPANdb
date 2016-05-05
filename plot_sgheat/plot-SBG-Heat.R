library("ggplot2")
argv <- commandArgs(TRUE)
  p=argv[2:13]
  p=as.numeric(p)
  n=argv[1]
  col=p
  for(j in 1: length(p)){
    col[j]=rgb(1,1-p[j],1-p[j])
  }
  p=p*100
  p=round(p,digits=1)
  p=as.character(p)
  for(j in 1: length(p)){
    if(p[j]=="100.0"){p[j]="100%"}
    else{p[j]=paste(p[j],"%",sep="")}
  }
  
  svg(filename=n,width=12,height=1.2)
  ggplot()+geom_rect(aes(xmin=c(0:11),xmax=c(1:12),ymin=0,ymax=1),fill=col,color="white")+ 
    geom_text(aes(x=c(0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5),y=0.7,label=c("IG1","IG2","IG3","IG4","IG5","AUSG6","JG7","JG8","JG9","JG10","AROG11","ADM")))+
    geom_text(aes(x=c(0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5),y=0.3,label=p))+
    theme_bw()+theme(axis.ticks=element_blank(),line=element_blank(),panel.border=element_blank(),axis.title=element_blank())+
    scale_x_continuous(breaks=c(0,5),labels=rep("",2))+scale_y_continuous(breaks=c(0,1),labels=rep("",2))
  dev.off()

