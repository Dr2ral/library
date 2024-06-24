from pprint import pprint
class Myclass:
    def __init__(self):
        self.obj = 42

    def introspection_info(self, obj):
        self.obj = obj
        print(self.obj)
        print(self.obj.__name__)



res = Myclass()
#print(dir(res))
#print(getattr(res, 'obj'))
#print(type(res.obj))
#print(dir(res.obj))
#print(dir(res.introspection_info))
#print(type(res))


val_list = [type(res.obj),dir(res.obj), id(res), hasattr(res, 'attr') ]
key_list = ['type', 'attributes', 'id', 'hasattr']

pprint(dict(zip(key_list, val_list)))

