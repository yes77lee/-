class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self,count=2):
        print(self.name + "가 " + str(count)+"번 앉았네요")

    def roll_over(self):
        print(self.name + "가 굴렀습니다")

my_dog =Dog('will',3)
print(my_dog.name)
print(my_dog.age)
my_dog.sit(5)
my_dog.roll_over()
my_dog.sit()


