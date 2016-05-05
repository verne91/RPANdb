#!/usr/bin/env python
import os

def main():
    fpath = "/export/home/csun/3krice/new_ref_20160504/addN/"
    glist = ['IG1','IG2','IG3','IG4','IG5','AUSG6','JG7','JG8','JG9','JG10','AROG11','Adm']
    com1 = "cat "
    com2 = "cat "
    for i in glist:
        com1 += fpath+i+"_N.fa "
        com2 += fpath+i+".loc "
    com1 += "> unaln.fa"
    os.system(com1)
    com2 += "> unaln.loc"
    os.system(com2)
main()
