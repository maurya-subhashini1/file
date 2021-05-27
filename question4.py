b=open("people5.txt","r")
for j in b:
    if"delhi" in j:
        s=open("delhi.txt","a")
        s.write(j)
    elif"shimila" in j:
        v=open("shimila.txt","a")
        v.write(j)
    else:
        c=open("other.txt","a")
        c.write(j)
b.close()


# debug


    