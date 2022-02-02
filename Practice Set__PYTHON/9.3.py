def multi():
  for a in range(1,21):
    with open(f'Practice Set__PYTHON/Multi__Table/table{a}.txt','w') as m: 
      for i in range(1,11) :
        z=a*i
        m.write(f"{z}\n")        
multi()