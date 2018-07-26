def hello(name='lee', age='10'):
    print("hello, " + name)
    print(age +" years old")

name= input("your name:")
age = input("How old are you?")
hello(name,age)
hello(age='30',name='jay')