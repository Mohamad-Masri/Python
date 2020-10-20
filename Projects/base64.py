#pip install pybase64

import base64
print(base64.b64encode("password".encode("utf-8")))

print(base64.b64decode("cGFzc3dvcmQ=").decode("utf-8"))

b'Y29uZ3JhdHN5b3Vnb3R0aGVwYXNz'
