import logging

class Calculadora():
    
    def __init__(self):
        print('Pressione "x" caso queira encerrar a calculadora ou "Enter" caso queira continuar.')
        print('#'*80)
        numero1 = int(input("Digite o primeiro número da operação: "))
        print("#"*40)
        numero2 = int(input("Digite o segundo número da operação: "))
        print("#"*40)
        operacao = int(input("Agora escolha a operação desejada: 1 - Soma; 2 - Subtração; 3 - Multiplicação; 4 - Divisão \n"))
        print("#"*90)
        if operacao == 1:
            resultado = self.soma(numero1, numero2)
            logger.info(f"A soma dos numeros {numero1} e {numero2} e igual a {resultado}")
        elif operacao == 2:
            resultado =  self.subtracao(numero1, numero2)
            logger.info(f"A subtracao dos numeros {numero1} e {numero2} e igual a {resultado}")
        elif operacao == 3:
            resultado = self.multiplicacao(numero1, numero2)
            logger.info(f"A multiplicacao dos numeros {numero1} e {numero2} e igual a {resultado}")
        elif operacao == 4:
            resultado = self.divisao(numero1, numero2)
            logger.info(f"A divisao dos numeros {numero1} e {numero2} e igual a {resultado}")
        else:
            logger.error('Opcao invalida.')
            
    def soma(self, numero1, numero2):
        return numero1+numero2

    def subtracao(self, numero1, numero2):
        return numero1-numero2

    def multiplicacao(self, numero1, numero2):
        return numero1*numero2

    def divisao(self, numero1, numero2):
        if(numero2 == 0):
            logger.error(f'{numero1}/{numero2}: Nao existe divisao por zero.')
        else:
            return numero1/numero2
        
if __name__ == '__main__':

    log_format = '%(asctime)s: %(levelname)s: %(filename)s: %(message)s'

    logging.basicConfig(filename='registro_calculadora.log',
                        filemode = 'w',
                        level=logging.DEBUG,
                        format = log_format)

    logger = logging.getLogger('root')

    logger.info("Calculadora iniciada.")
    while True:
        Calculadora()
        if 'x' == input():
            logger.info("Calculadora encerrada.")
            break