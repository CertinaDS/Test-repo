import json
data = {
'title': '1',
'text': '2',
'author': '3'
}
class Model:
    value = []
    def Save(value):
        for v in data.values():
            value.append(v)
        print(value)
        with open("Value.json", "w") as file:
            json.dump(value, file)
    Save(value)