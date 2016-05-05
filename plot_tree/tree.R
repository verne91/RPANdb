argv <- commandArgs(TRUE)
library("ape")
library("hash")
tree <- read.tree(argv[1])
tree<-tree[[1]]
example <- read.delim(argv[2],header=F)
h<-hash(example[,1],example[,2])
e <- tree$edge
l <- tree$tip.label
n <- length(l)
num <- nrow(e)
len <- c(1:num)
v <- rep("red",num)
for (i in len) {
  if (e[i,2] > n){
    v[i] <- "grey"
    next
  }
  else {
    da <- e[i,2]
    if(h[[l[da]]] == 0){
      v[i] <- "black"
    }
    else if(h[[l[da]]] == 1){
      v[i] <- "red"
    }
    else{v[i]="black"}
  }
}

svg(file=argv[3], width=7, height=4)
plot(tree, type="unrooted", no.margin=TRUE, show.tip.label=F,edge.color = v)
legend(2000,13500,legend=c("Presence","Absence"),fill=c("red","black"),inset=.05,border=NA,bty="n")
dev.off()
