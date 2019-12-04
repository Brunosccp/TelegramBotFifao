from enums import Converter

class Player:

    overall: int   
    age: int
    position: int
    preferredFoot: int

    def fill(self, sender, step):
        converter = Converter()

        if step == 1:
            self.overall = int(sender)
        elif step == 2:
            self.age = int(sender)
        elif step == 3:
            self.position = converter.convertPosition(sender)
        elif step == 4:
            self.preferredFoot = converter.convertPreferredFoot(sender)