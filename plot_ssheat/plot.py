#!/usr/bin/env python
import os

def main():
	f = "/export/home/csun/3krice/pandb_20160504/gene_categorization/GeneFeature.txt"
	rscript = "Rscript /export/home/csun/3krice/pandb_20150928/plot_ssheat/plot-SB-Heat.R"
	with open(f) as fin:
		for line in fin:
			tmp = line.strip().split()
			if tmp[0] != 'gene_id':
				name = tmp[0]+".svg"
				ar = [tmp[18]]
				ar.append(tmp[17])
				ar += tmp[19:22]
				ars = map(str,ar)
				arss = " ".join(ars)
				argg = rscript+" "+name+" "+arss
				os.system(argg)
main()
