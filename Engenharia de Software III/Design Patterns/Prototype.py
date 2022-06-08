#Protótipo
#O padrão prototype é um padrão basicamente para objetos clonados.

#Quando usar?
#O protótipo padrão permite copiar objetos existentes e modificá-los da maneira que desejar sem ter o trabalho de criar e configurar um objeto do princípio.

#Ele deve ser usado quando queremos um objeto exatamente igual ou quando o custo de criação de um objeto para grande.

import copy

class carro:
    def __init__(self, name, category='Mountain'):
        self.name = name
        self.category = category


if __name__ == '__main__':
    original_carro = carro('Ford')
    print(original_carro.name)
    print(original_carro.category)

    cloned_carro = copy.deepcopy(original_carro)
    cloned_carro.name = 'Ford2'
    print(cloned_carro.name)
    print(cloned_carro.category)