def main():
	num = 1
	fout = open("genes_sorted_num.csv","w")
	with open("genes_sorted.csv") as fin:
		for line in fin:
			fout.write(str(num)+","+line)
			num += 1
	fout.close()
main()
