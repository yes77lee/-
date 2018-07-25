person={'name':'lee','address':'cheonan','email':'yslee@naver.com'}
print(person)
print(person['name'].title())
print(person['email'])
person['name']='jay'
print(person.items())
for key, value in person.items():
    print("\nkey \\ " + "'"+key+"'")
    print('value \\"'+ value+'"')

