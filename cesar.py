print('===================')
print('Seja bem vindo ao algoritmo de criptografia da turma do 1º01!!!')
print('===================')
chave = 3
caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def criptografar():
    cripto =''
    texto = input('Digite a frase a ser criptografada: ')
    texto=texto.upper()
    for letra in texto:
        if letra in caracteres:
            posicao = caracteres.find(letra)

            # Aplica a cifra de César adicionando a chave
            nova_posicao = (posicao + chave) % len(caracteres)
            letra_criptografada = caracteres[nova_posicao]

            cripto += letra_criptografada
        else:
            cripto += letra  # Mantém caracteres que não estão no alfabeto
    print('\n',cripto)
    repetir()
def descriptografar():
        descripto =''
        texto = input('Digite a frase a ser criptografada: ')
        texto=texto.upper()
        for letra in texto:
            if letra in caracteres:
                posicao = caracteres.find(letra)

            # Aplica a cifra de César adicionando a chave
                nova_posicao = (posicao - chave) % len(caracteres)
                letra_criptografada = caracteres[nova_posicao]

                descripto += letra_criptografada
            else:
                descripto += letra  # Mantém caracteres que não estão no alfabeto
        print('\n', descripto)
        repetir()
def repetir():
    rep = input('''
Deseja criptografar? digite 1.
Deseja descriptografar? digite 2.
Deseja sair? Digite 3.
R:''')
    rep=rep.upper()
    if rep == '1':
        criptografar()
    elif rep == '2':
        descriptografar()
    elif rep == '3':
        ('Tchau!!!')
        print('Programa finalizado!!')
repetir()