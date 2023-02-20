class Model:
    def __init__(self, *args):
        self.d = dict()

    def query(self, *args, **kwargs):
        self.d.update(kwargs)

    def __str__(self):
        if len(self.d) == 0:
            return f"Model"
        else:
            # print([f"{key} = {value}" for key, value in self.d.items()])
            return 'Model: ' + ', '.join([f"{key} = {value}" for key, value in self.d.items()])


model = Model()
model.query(model.query(id=1, fio='Sergey', old=33))
print(model)
