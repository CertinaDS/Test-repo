import json
data = {
'title': 'заголовок',
'text': 'текст',
'author': 'автор'
}
data_ = list(data.keys())
class Model:
    def Save(data_):
	    with open("data_.json", "w") as file:
		    json.dump(data_, file)
    Save(data_)