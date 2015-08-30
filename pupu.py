#coding:L1
import zlib
x=zlib.decompress("xÚuË1C[Æ(ÖÙþKˆpörðžAª¶´Y¨X*l+°ÑM©sWqo£ð)›séãhx—%†Žz‰Æ„áv¼p%ID»ÈçŽâ†:íé§Ül¬Z©ËaÂ<ÁDåŠWjõ~Xi³ûa5;>ú‡Ùé¿3òË¯˜²ÚO.ï¨çC@žX>Ñóþy#7fò/™šÏQ·Òn½¤Q°")
s=""
for l in range(len(x)/2):
    i=int(x[0:2],16)
    j=i%127
    x=x[2:]
    s+=' '*j if l%2 else '*'*j
    if i&128:s+='\n'
print(s)
