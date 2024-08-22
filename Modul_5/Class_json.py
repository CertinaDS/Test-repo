import json
data = {
'title': '1',
'text': '2',
'author': '3'
}
class Model:
    value = []
    def Save(value):
        for k,v in data.items():
            value.append(v)
        with open("Value.json", "w") as file:
            json.dump(value, file)
    Save(value)