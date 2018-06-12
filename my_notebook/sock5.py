import socket
import socks
import requests

#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
#socket.socket = socks.socksocket
#url = 'http://rest.kegg.jp/get/hsa:10458+ece:Z5100/aaseq'
#link = requests.get(url)
#print(link.text)

my_proxies = {"http": "127.0.0.1:12333", "https": "127.0.0.1:12333"}
resp = requests.get("https://www.kegg.jp/kegg/rest/keggapi.html", proxies=my_proxies, timeout=50)
print(resp.text)