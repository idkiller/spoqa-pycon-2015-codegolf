#coding:L1
import zlib
x=zlib.decompress("x�u��1C[�(���K�p��r��A���Y�X*l+��M�sWqo���)�s��hx�%��z����v�p%�ID����:���l�Z��a�<�D�Wj�~Xi��a5;>����3�˯���O.��C@�X>���y#7f�/���Q��n��Q�")
s=""
for l in range(len(x)/2):
    i=int(x[0:2],16)
    j=i%127
    x=x[2:]
    s+=' '*j if l%2 else '*'*j
    if i&128:s+='\n'
print(s)
