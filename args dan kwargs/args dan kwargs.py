"""
*Args **kwargs
"""

def printData(*args):
    for name in args:
        print(name)

printData('hilman', 'yasman', 'mona', 'arki')

def printData1(**kwargs):
    for key, value in kwargs.items():
        print(key + "- " + value)

printData1(name ='hilman',age = '20', hobby ='nyanyi')
