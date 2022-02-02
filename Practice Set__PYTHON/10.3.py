class sample():
    a=5

z=sample()
z.a=6  #__________changing the instance attribute will not change the class attribute
# sample.a=9

print(z.a)
print(sample.a)