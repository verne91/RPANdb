#!/usr/bin/env python
#

def main():
	full_list = "genes_sorted_num.csv"
	notfull_list = "453_gene_feature.csv"

	a_hash = {}
	header = ["gene_no"]
	with open(notfull_list) as fin:
		for line in fin:
			tmp = line.strip().split(",")
			if tmp[0] == "gene_id":
				header+= tmp
			else:
				a_hash[tmp[0]] = tmp
	print header
	fout = open("full_gene_feature.csv","w")
	with open(full_list) as fin:
		for line in fin:
			tmp = line.strip().split(",")
			fout.write(tmp[0]+","+tmp[-1]+",")
			if a_hash.has_key(tmp[-1]):
				fout.write(",".join(a_hash[tmp[-1]][1:])+"\n")
			else:
				fout.write(",".join(["0"]*15+["na"]+["0.0"]*5+["FALSE"]*5+["0.0"]*9+["FALSE"]*6+["TRUE"])+"\n")
	fout.close()
main()
				
