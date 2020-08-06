"""
Dictionary {}
key:value
"""

data = {
    "name" : "Rangga",
    "age" : "20",
    "hobby" : "sport"
}
data['dream'] = "athlete"
del data["age"]
print("namanya adalah " + data["name"])

print(data)

for key, value in data.items():
    print(key + " : " + value )