#!/usr/bin/env python
import os

def main():
	f = "/export/home/csun/3krice/pandb_20160504/gene_categorization/GeneFeature.txt"
	rscript = "Rscript /export/home/csun/3krice/pandb_20150928/plot_sgheat/plot-SBG-Heat.R"
	with open(f) as fin:
		for line in fin:
			tmp = line.strip().split()
			if tmp[0] != 'gene_id':
				name = tmp[0]+".svg"
				ar = tmp[27:32]+[tmp[20]]+tmp[32:36]+[tmp[19]]+[tmp[21]]
				ars = map(str,ar)
				arss = " ".join(ars)
				argg = rscript+" "+name+" "+arss
				os.system(argg)
main()
