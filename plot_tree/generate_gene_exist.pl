#!/usr/bin/perl
use strict;
use warnings;

my $usage="$0 gene.exist dis.txt outdir
";
die $usage if @ARGV!=3;
my ($efile,$dfile,$outdir)=@ARGV;

my %h;
open(IN,$ARGV[1]);
while(<IN>){
    chomp;
    $h{$_}=1;
}
close IN;

print STDERR scalar(keys %h);

$outdir.="/" unless $outdir=~/\/$/;

my @name;
my $i=0;
my $j=0;
open(IN,$efile);
while(<IN>){
    chomp;
    $i++;
    my @t=split /\t/,$_;
    my $n=shift @t;
#    print STDERR $n,"\n";
    if($i==1){
	@name=@t;
    }
    else{
#	$n=substr($n,0,length($n)-1); #for geneFam use GF0: ->GF0
	next unless defined($h{$n});
#	print STDERR $h{$n};
	my $f=$outdir.$n;
	print STDERR "Generate for $n\n";
	open(OUT,">$f") || die "cannot open $f\n";
	for($i=0;$i<@name;$i++){
	    print OUT $name[$i],"\t",$t[$i],"\n";
	}
	print OUT "CX401\t0\n";
	close OUT;
    }
}
close IN;


