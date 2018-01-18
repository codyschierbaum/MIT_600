import argparse
import time
import sys
import requests

parser=argparse.ArgumentParser("Runs the live trade prices")
parser.add_argument("-w","--wait", help="how long to wait between checks",default=10, type=int)
parser.add_argument("-p","--pair", help="specify the currency pair to view",default="ETH_USD")
parser.add_argument("-u","--url",help="specify the API URL to use",default="https://api-public.sandbox.gdax.com/")
args=parser.parse_args()
API_url=args.url
def reqst(path):
	if path==None:
		path="/"
	r=requests.get(args.url+path)
	return r.json()

while True:
	for i in reqst('/products'):
		print(i)
		for e in i:
			print(e,': ',i[e])
		time.sleep(2)
	print('Waiting {} seconds'.format(args.wait))
	time.sleep(args.wait)

if __name__=="__main__":
	main.sys.args[1:]
