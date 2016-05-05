#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

def main():
	fout = open(sys.argv[2], 'w')
	mrna_id = 0
	cds_len = 0
	exon_num = 0
	with open(sys.argv[1]) as fin:
		for line in fin:
			temp = line.strip().split('\t')
			if temp[2] == 'gene':
				if mrna_id != 0:
					fout.write(source+','+chr_num+','+pos_start+','+pos_end+','+strand+','+str(cds_len)+','+str(exon_num)+','+trans_id+'\n')
					cds_len = 0
					exon_num = 0
				mrna_id += 1
				chr_num = temp[0]
				source = temp[1]
				pos_start = temp[3]
				pos_end = temp[4]
				strand = temp[6]
				m1 = re.match(r'ID=([Os|Un].*)', temp[8])
				
				trans_id = m1.group(1)
				
			elif temp[2][:4] == 'five' or temp[2] == "5UTR":
				exon_num += 1
				five_end = int(temp[4])
			elif temp[2] == 'CDS':
				cds_len += int(temp[4]) - int(temp[3]) + 1
				if abs(int(temp[3]) - five_end) != 1:
					exon_num += 1
				cds_end = int(temp[4])
			elif temp[2][:5] == 'three' or temp[2] == "3UTR":
				if abs(int(temp[3]) - cds_end) != 1:
					exon_num += 1
			
	fout.write(source+','+chr_num+','+','+pos_start+','+pos_end+','+strand+','+str(cds_len)+','+str(exon_num)+','+trans_id+'\n')

	fout.close()
main()