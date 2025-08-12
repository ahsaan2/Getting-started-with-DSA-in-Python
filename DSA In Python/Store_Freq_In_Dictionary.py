# Dict store key-value pairs
# empty dict
my_dict = {}

person = {
    "name": "Ahsaan",
    "email": "<EMAIL>",
    "age": 22,
}
# Accessing values
print(person)
print(person["name"])
# Adding values
person["email"] = "ahsaan21@gmil.com"
print(person)

# Removing by key
person.pop("age")
print(person)

# traversing the dict
print("Traversing a dictionary")
for key in person:
    print(key, person[key])

# (1) Store freq in the dict.
# given list of nums,
nums = [5, 6, 7, 7, 1, 1, 9, 1, 1, 5, 5, 9]

freq_dict = {}
for i in range(0, len(nums)):
    #     check if the current value is present in the dict or not
    if nums[i] in freq_dict:
        freq_dict[nums[i]] += 1
    else:
        freq_dict[nums[i]] = 1

# print(freq_dict[1])

for key, value in freq_dict.items():
    print(key, value)

# Method 2
print("Method 2 for freq map:")
nums = [1, 1, 2, 2, 1, 2, 1, 2, 1, 3, 3, 4, 4, 3, 3, 4, 5, 9, 8, 7]
hashMap = {}
for i in range(0, len(nums)):
    # get current value if present, if key is not present in the map return 0
    hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1

for key, value in hashMap.items():
    print(key, value)
