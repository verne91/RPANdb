def main():
	search_dict = {}
	with open("/export/home/csun/3krice/new_ref_20160504/unaln.loc") as fin:
		for line in fin:
			tmp = line.split()
			search_dict[tmp[1]] = [tmp[0], int(tmp[2])]
	fout = open("unaln.gff","w")
	with open("origin.gff") as fin:
		for line in fin:
			tmp = line.split()
			fout.write(search_dict[tmp[0]][0]+"\t"+tmp[1]+"\t"+tmp[2]+"\t"+str(int(tmp[3])+search_dict[tmp[0]][1]-1)+"\t"+str(int(tmp[4])+search_dict[tmp[0]][1]-1)+"\t"+"\t".join(tmp[5:])+"\n")
	fout.close()
main()