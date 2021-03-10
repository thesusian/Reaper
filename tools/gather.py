import time
try:
    import requests
    from bs4 import BeautifulSoup
    from colorama import init, Fore, Back
except:
    print("you need to install reqests,bs4,colorama")
init(autoreset=True)

print (Fore.CYAN+"[X]"+Fore.YELLOW+" Creating archive"+Fore.MAGENTA+""" "proxies.txt" """)
try:
	f = open("proxies.txt","w+")
	print (Fore.CYAN+"[X]"+Fore.YELLOW+" Archive created")
except:
	pass


		
	


url = "https://free-proxy-list.net/anonymous-proxy.html"
r = requests.get(url)
rhtml = r.content
soup = BeautifulSoup(rhtml,"html.parser")

tabla = soup.find("table", {"id" : "proxylisttable"})
cuenta  = 0


formatoip="IP:PORT"
formatopais="PAIS"
formatoweb="WEB"

ippuertolista = []

for columna in tabla.find_all("tr"):
	columnas = columna.find_all("td")
	try:
		ip = columnas[0].get_text()
		puerto = columnas[1].get_text()
		ippuerto = Fore.MAGENTA+ip+":"+puerto
		pais = Fore.YELLOW+columnas[3].get_text()
		webs= Fore.CYAN+"from "+Fore.RED+"https://free-proxy-list.net/anonymous-proxy.html"
		print ("\n"+"%-30s %-30s %s"%(ippuerto,pais,webs))
		cuenta = cuenta+1

		puertoip = "\n"+ip+":"+puerto
		ippuertolista.append(puertoip)


	except:
		pass

print ("-"*30+"\n"+Back.WHITE+Fore.BLACK+"[X]Proxies gathered: "+Fore.RED+str(cuenta))





for x in ippuertolista:
	f.write(x)
f.close()
