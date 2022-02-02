p=open('sample2.txt','rt')
q=p.read()
if "Twinkle" in q:
    print("Yes it contains Twinkle word")
else:
    print("It does not contain Twinkle")
p.close()        