from OOP.ContBancar import ContBancar

cont_Miha = ContBancar('Miha S', 'RO001')
cont_Cornel = ContBancar('Cornel B', 'R0002' )



cont_Miha.activareContMiha(3333)
cont_Cornel.activareContCornel(3333)
cont_Miha.activareContMiha(44444)
cont_Miha.activareContMiha(11111)
cont_Miha.activareContMiha(7777)

cont_Miha.alimentareCont(1000)
cont_Cornel.alimentareCont(1000)

cont_Miha.plataCard(500)
cont_Cornel.plataCard(600)

cont_Miha.interogareSold()
cont_Cornel.interogareSold()



