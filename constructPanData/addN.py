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
	inputfa = sys.argv[1]
	# match = re.match(r'\S+group_(\d+).fa', inputfa)
	# if match:
	# 	group_id = match.group(1)
	group_id = os.path.basename(inputfa)[:-3]
	loc_out = open(group_id+".loc",'w+')

	Ns = ""
	for i in range(100):
		Ns += 'N'
	seq_Ns = Seq(Ns, SingleLetterAlphabet())

	all_seq = seq_Ns
	cur_pos = 101

	for seq_record in SeqIO.parse(inputfa, "fasta"):
		start_pos = cur_pos
		end_pos = start_pos + len(seq_record) - 1
		all_seq += seq_record.seq
		loc_out.write("unaln_"+group_id+"\t"+seq_record.id+"\t"+str(start_pos)+"\t"+str(end_pos)+"\n")
		all_seq += seq_Ns
		cur_pos = end_pos + 101
	loc_out.close()
	rec = SeqRecord(all_seq, id="unaln_"+group_id, description="")
	recs = [rec]
	SeqIO.write(recs, group_id+"_N.fa", "fasta")
main()