class ContBancar:
    def __init__(self, titularCont, iban):
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.incercari_activare = 0

    def salut(self):
        print(f'Buna {self.titularCont}!')


    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari gresite {self.incercari_activare}')
        print('-----------------------------------')

    def activareContMiha(self, pin_Miha):
        self.salut()
        self.pin_Miha = 7777
        if pin_Miha == self.pin_Miha:
            print('Card activat.')
            self.activ = True
        else:
            print('PIN gresit.')
            self.incercari_activare += 1


    def activareContCornel(self, pin_Cornel):
        if pin_Cornel == 3333:
            print('Card activat.')
            self.activ = True
        else:
            print('PIN gresit.')
            self.incercari_activare += 1


    def alimentareCont(self, suma_alimentata):
        self.salut()
        self.sold += suma_alimentata
        print(f'Ati alimentat: {suma_alimentata} ')
        print(f'Aveti in cont: {self.sold}')

    def plataCard(self, suma_platita):
        self.salut()
        if suma_platita <= self.sold:
            self.sold -= suma_platita
            print(f'Ati cheltuit: {suma_platita}')
            print(f'Aveti in cont: {self.sold}')
        else:
            print('Fonduri insuficiente.')



