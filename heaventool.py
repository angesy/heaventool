import socket
banner = """
 /$$   /$$                                               /$$$$$$$$                  /$$
| $$  | $$                                              |__  $$__/                 | $$
| $$  | $$  /$$$$$$   /$$$$$$  /$$    /$$/$$$$$$  /$$$$$$$ | $$  /$$$$$$   /$$$$$$ | $$
| $$$$$$$$ /$$__  $$ |____  $$|  $$  /$$/$$__  $$| $$__  $$| $$ /$$__  $$ /$$__  $$| $$
| $$__  $$| $$$$$$$$  /$$$$$$$ \  $$/$$/ $$$$$$$$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$
| $$  | $$| $$_____/ /$$__  $$  \  $$$/| $$_____/| $$  | $$| $$| $$  | $$| $$  | $$| $$
| $$  | $$|  $$$$$$$|  $$$$$$$   \  $/ |  $$$$$$$| $$  | $$| $$|  $$$$$$/|  $$$$$$/| $$
|__/  |__/ \_______/ \_______/    \_/   \_______/|__/  |__/|__/ \______/  \______/ |__/"""

#NMAP
def nmap():
 ip = input("\nIP Address: ")
 port = int(input("Port: "))

 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 conn = sock.connect_ex((ip,port))

 if conn == 0:
  print(f"\n{"=" * 16}\n{port} Port: OPEN\n{"=" * 16}")
 else:
  print(f"\n{"=" * 16}\n[X] {port} Port: CLOSED\n{"=" * 16}")

#Menu principal
print(banner)
modo = input("""
+---------------------------------+
| Choose the mode (nmap):           |
+---------------------------------+\n""")
if modo == "nmap":
  nmap()
else:
  print("Esse modo não existe.")