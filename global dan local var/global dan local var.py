"""
LOCAL dan GLOBAL var
"""

name = "hilman"

def printName():
    #global name
    name = "chesky"
    print("akses dari dalam " + name)

printName()
print("akses dari luar " + name)