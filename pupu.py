#coding:L1
import zlib
x=zlib.decompress("xœuK!ƒ¯ÄÆÎýÐ`gÑ.ºàþb\"ª¶´Y¨X*l+°ÑM©sWqo£ð)›séãhx—%†Žz‰Æ„áv¼p%ID»ÈçÅuÚÓOù²±k¥.‡	ó•+^©uöÃJ›Ý«ÙñÑ?ÌÎù‹1c!¿üŠ)»ýär*ïòÄò‰ž÷OÜ˜É»dj<Gí*üÜ‡ÖQ")
s=""
for l in range(len(x)/2):
    i=int(x[0:2],16)
    j=i%127
    x=x[2:]
    s+='*'*j if l%2 else ' '*j
    if i&128:s+='\n'
print(s)
