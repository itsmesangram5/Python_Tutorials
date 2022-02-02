mydic = { 
    "Sangram": "Nangare",
    'Numbers':[1,2,3],
    "newdic":{'1':'s',"2":"p"},
    1:2
    }
# print(mydic.keys())
# it you find type of above output them it will 
# a list
# print(type(mydic.keys()))
# hense convert it into a list
# print(list(mydic.keys()))
# print(mydic.values())
# print(mydic.items())
# prints all items in mydic as key value pairs
# anotherdic={'ss':'nn',
# 'pp':'bb'}
# mydic.update(anotherdic)
# print(mydic["Sangram2"])#shows error
print(mydic.get("Sangram2"))#shows none if not present
# diff bet .get and [] Syntax