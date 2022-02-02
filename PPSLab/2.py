try:
 n = int(input("Enter no of elements: "))
 nos_list = []    
 for i in range(n):   
  num = int(input("Enter no: "))
  nos_list.append(num)  
 maxNo = max(nos_list) 
 minNo = min(nos_list)   
 sumNos = sum(nos_list)  
 average = sumNos/len(nos_list) 
 print('Max no is ',maxNo)
 print('Min no is ',minNo)
 print('Numbers Entered ',len(nos_list)) 
 print('Sum of nos is ',sumNos)
 print('Average of nos is ',average)
except ValueError:
 print('Enter n and all elements as integer')


