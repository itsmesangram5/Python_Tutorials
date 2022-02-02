with open('sample6.txt','r') as p:
    z=p.read()
    with open('sample7.txt','r') as m:
        y=m.read()
        if z==y:
            print("files are identical")
        else:
            print("Files are not identical !! ")    