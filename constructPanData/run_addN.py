import os

def main():
	for fa in os.listdir("/export/home/csun/3krice/new_ref_20160504/split/"):
		os.system("nohup python2.6 /export/home/csun/3krice/new_ref_20160504/addN/addN.py /export/home/csun/3krice/new_ref_20160504/split/"+fa+" >"+fa+".out 2>&1 &")

main()