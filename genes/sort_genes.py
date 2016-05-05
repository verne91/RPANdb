import os

def main():
	chr_name = []
	gff_file = "/export/home/csun/3krice/pandb_20160504/genes/genes_temp.csv"
	with open("chr_name") as fin:
		for line in fin:
			chr_name.append(line.strip())
	for chro in chr_name:
		os.system("grep '"+chro+"' "+gff_file+" > chr_split/"+chro+".temp")
		os.system("sort -n -t ',' -k 3 chr_split/"+chro+".temp"+" > chr_sorted/"+chro+"_sorted.csv")
	cat_cmd = "cat "
	for chro in chr_name:
		cat_cmd += "chr_sorted/"+chro+"_sorted.csv "
	cat_cmd += "> genes_sorted.csv"
	os.system(cat_cmd)
main()
