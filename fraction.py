class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

c1=Customer("niloy",26)
c2=Customer("nayan",27)
c3=Customer("piyas",30)

L=[c1,c2,c3] # pass the objects in a list
for i in L:
    print(i.name,i.age)

        