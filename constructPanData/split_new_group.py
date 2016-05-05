#!/usr/bin/env python
#
import sys
import re
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import SingleLetterAlphabet

def main():
	# groupfile = sys.argv[1]
	# "origin.fa" = sys.argv[2]
	# out_dir = sys.argv[3]
	print os.path.exists("lines_info.csv")
	print os.getcwd()

	if os.path.isdir("split"):
		os.system("rm -r "+"split")
		os.makedirs("split")
		os.chdir("split")
	else:
		os.makedirs("split")
		os.chdir("split")

	print os.getcwd()
	group_dict = {}
	with open("/export/home/csun/3krice/new_ref_20160504/lines_info.csv") as fin:
		for line in fin:
			temp = line.strip().split(",")
			group_dict[temp[1]] = temp[5]
	print "Read group infomation completely!"

	my_records = {
		'IG1':[],
		'IG2':[],
		'IG3':[],
		'IG4':[],
		'IG5':[],
		'AUSG6':[],
		'JG7':[],
		'JG8':[],
		'JG9':[],
		'JG10':[],
		'AROG11':[],
		'Adm':[]
	}

	rid = re.compile(r'(\S+):(\S+):(\S+):(\S+)')
	for seq_record in SeqIO.parse("/export/home/csun/3krice/new_ref_20160504/origin.fa", "fasta"):
		m = rid.match(seq_record.id)
		if m:
			sample_name = m.group(1)
			group_id = group_dict[sample_name]
			my_records[group_id].append(seq_record)
	
	print "Read input fasta completely!"

	for rec in my_records:
		SeqIO.write(my_records[rec], rec+".fa", "fasta")
		print "Write group "+rec+"completely!"


main()
