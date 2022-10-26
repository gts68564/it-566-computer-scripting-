import json

class Test:

    def new_roaster(self):
        with open("roaster.json","r+") as rs:
            a = json.load(rs)
            b = {"Title": "new roaster"}
            a.dump(b,rs, indent=2)
        print()

t = Test()