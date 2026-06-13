import json

with open("users.json","r") as f:
    users = json.load(f)
    for user in users:
        print(user["name"])
    for user in users:
        if user["age"] > 18:
            print(user["name"])
    users.append({"id": 4, "name": "David", "age": 22})
with open("users.json","w",encoding="utf-8") as f:
    json.dump(users,f) #不要json.load了
