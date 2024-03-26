hash = {}
hash["key1"] = "value1"
hash["key2"] = "value2"

print(hash)

print(hash["key1"])  
print(hash["key2"])  

for key, value in hash.items():
    print(f"Key: {key}, Value: {value}")