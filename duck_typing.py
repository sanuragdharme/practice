class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor()

laptop = Laptop()
laptop.code(ide)
