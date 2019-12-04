
positions = []

class Converter:

    def convertPosition(self, position):
        if not positions.__contains__(position):
            positions.append(position)
        
        for i in range(0,len(positions)):
            if(positions[i] == position):
                return i
            
        return -1

    def checkPosition(self, position):
        print(position)
        print(positions)
        print(positions.__contains__(position))

        if positions.__contains__(position):
            return True
        else:
            return False

    def convertValue(self, stringValue: str):
        numberString = ""
        for s in stringValue:
            if s.isdigit() or s == ".":
                numberString = numberString + s
        
        number = float(numberString)

        if "M" in stringValue:
            return number * 1000000
        elif "K" in stringValue:
            return number * 1000
        else:
            return number

    def convertStringValue(self, value: float):
        intValue = int(value)

        millions = round(intValue / 1000000, 1)
        thousands = round(intValue / 1000, 1)
        
        if(millions > 0):
            return "€" + str(millions) + "M"

        elif(thousands > 0):
            return "€" + str(thousands) + "K"

        else:
            return "€1K"
            

    def convertPreferredFoot(self, preferredFoot: str):
        if preferredFoot == "Right":
            return 0
        else:
            return 1
    