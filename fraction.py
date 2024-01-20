def is_even(number):
    if type(number)==int:
      if number %2==0:
         return "even"
      else:
         return 'odd'
      
    else:
       return "not allowed"  
    

for i in range(1,11):
    print(is_even("niloy"))   