#coding:L1
import zlib
x=zlib.decompress("x�u�K!��������`g�.���b\"���Y�X*l+��M�sWqo���)�s��hx�%��z����v�p%�ID����u��O���k�.�	��+^�u��J������?����1c!���)���r�*�����O�ܘɻdj<G�*����Q")
s=""
for l in range(len(x)/2):
    i=int(x[0:2],16)
    j=i%127
    x=x[2:]
    s+='*'*j if l%2 else ' '*j
    if i&128:s+='\n'
print(s)
