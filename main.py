#project!
#Who makes more money men or Women depending on their age?

#                     Difference in annual pay for  Men   &   Women depending on their age
# 15-24                                             11.25     12.47
# 25-49                                             22.67     20.42
# 50-64                                             26.28     22.61
# 65+                                               20        19.98

import matplotlib.pyplot as ply
import numpy as np

price1 = (11.25 + 12.47)/2
print(price1)
price2 = (22.67 + 20.42)/2
print(price2)
price3 = (26.28 + 22.61)/2
print(price3)
price4 = (20 + 19.98)/2
print(price4)

averagePrice = [11.86, 21.545, 24.445, 19.990]
age = ["15-24", "25-49", "50-64", "65+"]
difference = [-1.22, 2.25, 3.67, 0.02]

   
Women = [12.47, 20.42, 22.61, 19.98]
Men = [11.25, 22.67, 26.28, 20]
  
n=4
r = np.arange(n)
width = 0.25
  
  
ply.bar(r, Women, color = 'b',
        width = width, edgecolor = 'black',
        label='Women')
ply.bar(r + width, Men, color = 'g',
        width = width, edgecolor = 'black',
        label='Men')
ply.bar(r - width, averagePrice, color = 'r',
        width = width, edgecolor = 'black',
        label='average')
  
ply.xlabel("age")
ply.ylabel("money")
ply.title("Gender pay gap!")
  
ply.grid(linestyle='--')
ply.xticks(r + width/2,["15-24", "25-49", "50-64", "65+"])
ply.legend()
  
ply.show()













        