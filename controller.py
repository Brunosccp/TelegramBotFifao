from enums import Converter

class Controller:
    
    step: int = 0

    def nextStep(self):
        self.step += 1

    def getText(self, sender):
        textos = []

        if not self.answerIsValid(sender):
            return None

        if self.step == 0:
            textos.append("Olá, eu sou o Jaime, o seu olheiro do Fifão")
            textos.append("Sou capaz de saber o preço de qualquer futuro jogador, seja ele o novo Messi ou o novo Ibson!")
            textos.append("Qual é o overall do seu jogador, meu consagrado?")

            return textos
        if self.step == 1:
            
            overall: int = int(sender)

            if overall >= 85:
                textos.append("Porra, " + sender + " de overall?")
                textos.append("Esse é craque, hein")
            elif overall >= 70:
                textos.append("Hm, então " + sender + " de overall")
                textos.append("Vamos ver se tem futuro")
            else:
                textos.append("Só " + sender + "?")
                textos.append("Esse é perna de pau, hein")

            textos.append("Qual a idade do seu jogador?")

            return textos
        if self.step == 2:

            age: int = int(sender)

            if age >= 34:
                textos.append("Putz, " + sender + " anos?")
                textos.append("Esse ai ta acabado")
            
            elif age >= 21:
                textos.append(sender + " anos? Saquei...")
            
            elif age >= 16:
                textos.append("Só " + sender + " aninhos?")
                textos.append("Menino inocente ainda, nunca comeu um...")
                textos.append("Bolo de fubá")

            textos.append("Agora me diz, qual a posição dele?")

            return textos
        if self.step == 3:
            textos.append("Bom, bom")
            textos.append("Agora pra fechar, ele é canhoto ou destro?")

            return textos
        if self.step == 4:
            try:
                preferredFoot = str(sender).lower()
            except ValueError:
                return

            if preferredFoot == "destro":
                textos.append("Destro né, padrão então")
            elif preferredFoot == "canhoto":
                textos.append("Opa, canhotinho normalmente é bom!")

            textos.append("Agora me da um tempo pra pensar...")

            return textos
            
    def answerIsValid(self, sender):

        converter = Converter()

        if self.step == 1:
            try:
                overall: int = int(sender)

                if overall > 99:
                    return False
                elif overall <= 0:
                    return False
                else: 
                    return True

            except ValueError:
                return False

        if self.step == 2:
            try:
                age = int(sender)

                if age < 16:
                    return False

                return True
            except ValueError:
                return False

        if self.step == 3:
            try:
                position = str(sender).upper()
                if not converter.checkPosition(position):
                    return False

                return True
            except ValueError:
                return False

        if self.step == 4:
            try:
                preferredFoot = str(sender).lower()

                if preferredFoot == "destro" or preferredFoot == "canhoto":
                    return True

                return False
            except ValueError:
                return False

        else:
            return True
        
                
                

        
            
        
        