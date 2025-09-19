d1 = {"a": "1", "b": "2"}
d2 = {"b": "3", "c": "4"}

print("Keys:", list(d1.keys()))
print("Values:", list(d1.values()))
print("Items:", list(d1.items()))
print("Merged:", {**d1, **d2})

