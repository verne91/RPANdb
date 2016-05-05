#gtf to gff3 converter
#Chen Sun
#2015-8-11

import sys
import re

def main():
    input_gtf = sys.argv[1]
    out_gff = sys.argv[2]
    fout = open(out_gff,"w")

    gene_id_old = ""
    flag = True
    gr = re.compile(r'.*"(\w+)"?.*')
    block = []
    with open(input_gtf) as fin:
        for line in fin:
            tmp = line.strip().split("\t")
            m = gr.match(tmp[8])
            gene_id = m.group(1)
            
            if gene_id == gene_id_old or flag == True:
                block.append(tmp)
                gene_id_old = gene_id
                flag = False
            else:
                min_pos = 1000000000
                max_pos = 0
                for rec in block:
                    if int(rec[3]) < min_pos:
                        min_pos = int(rec[3])
                    if int(rec[4]) > max_pos:
                        max_pos = int(rec[4])
                # print block
                fout.write(block[0][0]+"\t"+block[0][1]+"\tgene\t"+str(min_pos)+"\t"+str(max_pos)+"\t"+"\t".join(block[0][5:8])+"\tID="+gene_id_old+"\n")
                for rec in block:
                    fout.write("\t".join(rec[0:8])+"\tParent="+gene_id_old+"\n")
                block = []
                block.append(tmp)
                gene_id_old = gene_id
    min_pos = 1000000000
    max_pos = 0
    for rec in block:
        if int(rec[3]) < min_pos:
            min_pos = int(rec[3])
        if int(rec[4]) > max_pos:
            max_pos = int(rec[4])
    fout.write(block[0][0]+"\t"+block[0][1]+"\tgene\t"+str(min_pos)+"\t"+str(max_pos)+"\t"+"\t".join(block[0][5:8])+"\tID="+gene_id_old+"\n")
    for rec in block:
        fout.write("\t".join(rec[0:8])+"\tParent="+gene_id_old+"\n")
    block = []
    gene_id_old = gene_id

    fout.close()
main()