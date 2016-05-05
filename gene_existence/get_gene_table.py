#!/usr/bin/env python
#
import sys

def main():
	lines_info = sys.argv[1]
	genes_info = sys.argv[2]
	gene_exist = sys.argv[3]
	out_file = sys.argv[4]

	lines_hash = {}
	with open(lines_info) as fin:
		for line in fin:
			lines_hash[line.split(',')[1]] = line.split(',')[0]
	print "lines hash is constructed."

	genes_hash = {}
	with open(genes_info) as fin:
		for line in fin:
			genes_hash[line.strip().split(',')[-1]] = line.strip().split(',')[0]
	print "genes hash is constructed."

	header_list = []
	fout = open(out_file,'w')
	with open(gene_exist) as fin:
		for line in fin:
			tmp = line.strip().split('\t')
			if tmp[0] == "Gene":
				header_list = tmp[1:]
			else:
				gene_id = tmp[0]
				gene_no = genes_hash[gene_id]
				for i in range(len(tmp)-1):
					if tmp[i+1] == '1':
						line_name = header_list[i]
						if line_name in lines_hash.keys():
							line_no = lines_hash[line_name]
							fout.write(','.join([line_no,line_name,gene_no,gene_id])+"\n")
	fout.close()
main()