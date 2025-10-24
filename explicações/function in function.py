'''
def create_multiplication(multiplicator):
    def multiplicator(number):
        return multiplicator * number
    return multiplicator

isso permite com que meu codigo fique muito mais legivel e de facil
entendimento, por exemplo, olha parte do print:

duplicate = create_multiplication(2) dois vai fazer o n vezes 2
triplicate = create_multiplication(3) tres vai fazer o n vezes 3
quadriplicate = cretae_multiplication(4) quatro vai fazer o n vezes 4
'''
