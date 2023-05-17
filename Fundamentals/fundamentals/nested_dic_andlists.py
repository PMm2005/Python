x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Bryant', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

def iterateDictionary(students):
    for dictionary in students:
        for key, value in dictionary.items():
            print(key, value)

students = [
    {'name': 'John', 'last name': 'Rosales'},
    {'name': 'Emma', 'last name': 'Watson'},
    {'name': 'Michael', 'last name': 'Tonel'},
]

iterateDictionary(students)

def iterateDictionary2(key_name, students):
    for dictionary in students:
        if key_name in dictionary:
            print(dictionary[key_name])

iterateDictionary2('name',students)
iterateDictionary2('last name',students)

def printInfo(dojo):
    for key, value in dojo.items():
        print(f"Key: {key}, Size: {len(value)}")
        for item in value:
            print(item)
        print()
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)