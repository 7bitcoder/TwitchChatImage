import itertools

send = ''
##perm = list(set(itertools.permutations((True,True,False,False,False,False,False,False))))
for i in range(129,255):
    file = open("code.txt", "a")
    data = bin(i)[2:].zfill(8)
    print(data)
    dat = ''
    for j in range(8):
        if(data[j] == '1'):
            dat = dat + 'x'
        else:
            dat = dat + 'o'
        if(j%2 == 1):
            dat = dat + '\n'
    print(dat+'\n  :'+ str(i) + '\n')
    x = input()
    send = send + 'elif (T == '
    send = send + "(" + data[0] + ","+ data[1] + ","+ data[2] + ","+ data[3] + ","+ data[4] + ","+ data[5] + ","+ data[6] + ","+ data[7] + ")):"
    send = send  + '\n'+'\t' + "return u'\\u28"+x+ "'\n"
    print(send)
    file.write(send)
    send = ''
    file.close()
#    elif (T == ((False, True), (False, False), (False, False), (False, False))):##pojedyncze
#        return u'\u2808'
