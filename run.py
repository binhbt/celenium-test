import subprocess
import os
import threading
from concurrent.futures import ThreadPoolExecutor as PoolExecutor

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
def excute_command(command):
   print(command)
   subprocess.run(command, shell=True)

email = 'pstempien@coretechnology.pl'
passw ='Sigma2017@'
message = 'Tin nhan thu 3'
ids=['278704599679113','2283359851932462','2192140324217507','447580675997425','797978367269285','2377284532324008','2148843068562324','2336619386627058','627855861064357','2863079640399056']

ids1=['278704599679113']

commands =[]
for id in ids:
   # command = './fbpost_photo '+id+' "'+message+'" '+email+' '+ passw+' invisible'
   command = 'python3 fb_post.py '+id+' "'+message+'" '+email+' '+ passw+' invisible'

   commands.append(command)
   # x = threading.Thread(target=excute_command, args=(command,))
   # x.start()

with PoolExecutor(max_workers=3) as executor:
    for _ in executor.map(excute_command, commands):
        pass
print("All tasks complete")


import http.client
import socket

def get_it(url):
   for i in range(0, 100):
    print(i)
    try:
        print(url)
        # always set a timeout when you connect to an external server
        connection = http.client.HTTPSConnection(url, timeout=2)

        connection.request("GET", "/")

        response = connection.getresponse()

        return response.read()
    except socket.timeout:
        # in a real world scenario you would probably do stuff if the
        # socket goes into timeout
        pass

urls = [
    "www.google.com",
    "www.youtube.com",
    "www.wikipedia.org",
    "www.reddit.com",
    "www.httpbin.org"
] * 10

# with PoolExecutor(max_workers=4) as executor:
#     for _ in executor.map(get_it, urls):
#         pass
