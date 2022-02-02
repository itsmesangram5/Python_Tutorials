# use open function to read the contents of a file 
# f=open('24sample.txt','r')
f=open('sample1.txt')#by default the mode is r
# data=f.read()
data=f.read(5)
print(data)
f.close()
# with open('sample3.txt','w') as f:      opening file without closing no need to close
