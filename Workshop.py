def ahoj():
    print('Ahoj!')
    print('Ako sa mas?')

ahoj()
def ahoj(meno):
    if meno == 'Ola':
        print('Ahoj Ola!')
    elif meno == 'Sona':
        print('Ahoj Sona!')
    else:
        print('Ahoj neznama!')

ahoj("Andrea")
def ahoj(meno):
    print('Ahoj ' + meno + '!')

ahoj("Andrea")
dievcata = ['Katka', 'Kika', 'Zuza', 'Ola', 'Ty']
def ahoj(meno):
    print('Ahoj ' + meno + '!')

dievcata = ['Katka', 'Kika', 'Zuza', 'Ola', 'Ty']
for meno in dievcata:
    ahoj(meno)
    print('Dalsie dievca')
for i in range(1, 6):
    print(i)