
class Function():

    def calcular_imc(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            imc = weight / (height * height)

            if imc == "":
                self.saida_label.configure(text="Insira os dados")
            if imc < 18.5:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta abaixo do peso"
                self.saida_label.configure(text=texto_saida)

            elif imc < 25:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta com peso normal"
                self.saida_label.configure(text=texto_saida)
            elif imc < 30:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta acima do peso"
                self.saida_label.configure(text=texto_saida)
            elif imc < 40:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta com obesidade"
                self.saida_label.configure(text=texto_saida)

            else:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta com obesidade morbida"
                self.saida_label.configure(text=texto_saida)

        except ValueError:

            self.saida_label.configure(text="Insira os dados certos")




