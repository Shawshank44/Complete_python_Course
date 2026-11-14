# Exercise is code decode program :

import random as r
import string

st = input("Enter the string: ")
words = st.split(" ")
coding = input("1 for coding or 0 for decoding: ")
coding = True if (coding == "1") else False
if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            j1 = ''.join(r.choices(string.ascii_letters, k=3))
            j2 = ''.join(r.choices(string.ascii_letters, k=3))
            stnew = j1 + word[1:] + word[0] + j2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
