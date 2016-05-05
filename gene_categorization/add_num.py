
def main():
	gene_hash = {}
	with open("/export/home/csun/3krice/pandb_20160504/genes/genes_sorted_num.csv") as fin:
		for line in fin:
			tmp = line.strip().split(',')
			gene_hash[tmp[-1]] = tmp[0]
	fout = open("gene_categorization.txt",'w')
	with open("/export/home/csun/3krice/pandb_20160504/gene_categorization/3") as fin:
		for line in fin:
			tmp = line.strip().split()
			fout.write(gene_hash[tmp[0]]+","+",".join(tmp)+"\n")
	fout.close()
main()
