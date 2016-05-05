opendir(DIR,"geneExist");
my @d=readdir(DIR);

my $i=0;
foreach my $t (@d){
    next if $t=~/^\.+/;
    $i++;
    my $d=$t;
    $d=~s/t/g/;
    print STDERR"$i\t$t\n";
    my $cmd="Rscript tree.R gene.tre geneExist/$t geneFigSVG/$d.svg";
    system($cmd);
}
