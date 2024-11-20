"""

Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá realizarse 
exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva sino que se modificará la primera. 
Por ejemplo, si lista1 = [8, 1, 3] y lista2 =[5,9,7], lista1 deberá quedar como [8,5,1,9,3,7]

"""

x=[1,2,3,11,22,33]
y=[4,5,6]

for i in range(len(y)):
    x[i*2+1:i*2+1]=[y[i]]

print(x)