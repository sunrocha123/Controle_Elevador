class Elevador (object):
    
    dados_elevador = []
    
    def inicializa(self, capacidade_elevador, total_andares):
        auxiliar = {}
        auxiliar['capacidade_elevador'] = capacidade_elevador
        auxiliar['total_andares'] = total_andares
        auxiliar['quantidade de pessoas no elevador'] = 0
        auxiliar['andar atual'] = 0
        self.dados_elevador.append(auxiliar)
        pass
    
    def entra(self, quantidade_pessoas_entra):
        if (self.dados_elevador[0]['quantidade de pessoas no elevador'] + quantidade_pessoas_entra) <= self.dados_elevador[0]['capacidade_elevador']:
            self.dados_elevador[0]['quantidade de pessoas no elevador'] += quantidade_pessoas_entra
            return f'Entraram {quantidade_pessoas_entra} no elevador :)\n'
        else:
            return 'Desculpe, o elevador está cheio :(\nPor gentileza, espere o próximo\n'
        pass

    def sai(self, quantidade_pessoas_sai):
        if (self.dados_elevador[0]['quantidade de pessoas no elevador'] - quantidade_pessoas_sai) >= 0:
            self.dados_elevador[0]['quantidade de pessoas no elevador'] -= quantidade_pessoas_sai
            return f'Sairam {quantidade_pessoas_sai} do elevador :)\n'
        else:
            return 'Desculpe, a quantidade informada é maior do que a quantidade de pessoas que temos no elevador.\nNesse caso, não poderemos seguir com tal ação :(\n'
        pass
    
    def sobe(self, andar_sobe):
        if self.dados_elevador[0]['andar atual'] == self.dados_elevador[0]['total_andares'] or andar_sobe > self.dados_elevador[0]['total_andares']:
            return 'Desculpe, já estamos no último andar do prédio :(\nPor gentileza, revalidar sua escolha!\n'
        else:
            self.dados_elevador[0]['andar atual'] = andar_sobe
            return f'Elevador a caminho do {andar_sobe}º andar.\nChegamos no andar desejado :)\n'
        pass
    
    def desce(self, andar_desce):
        if self.dados_elevador[0]['andar atual'] == 0:
           return 'Desculpe, já estamos no térreo :(\nPor gentileza, revalidar sua escolha!\n'
        else:
           self.dados_elevador[0]['andar atual'] = andar_desce
           return f'Elevador a caminho do {andar_desce}º andar.\nChegamos no andar desejado :)\n'
        pass

if __name__ == '__main__':

    def menu():
        print(f'MENU\n'
              f'1. Entra\n'
              f'2. Sai\n'
              f'3. Sobe\n'
              f'4. Desce\n'
              f'5. Sair\n')

    print(f'--------------------\n'
          f'CONTROLADOR ELEVADOR\n'
          f'--------------------\n'
          f'Bem-vindo a nossa ferramenta de controle de elevador :)\n')

    objeto_Elevador = Elevador()

    capacidade_elevador = int(input('Digite a capacidade do elevador: '))
    total_andares = int((input('Digite o total de andares do prédio: ')))
    objeto_Elevador.inicializa(capacidade_elevador, total_andares)
    print('Dados cadastrados com sucesso! :)\n')

    while True:
        menu()

        while True:
            escolha_opcao = int(input('Digite uma opção (1 - 5): '))
            if int(escolha_opcao) <= 0 or int(escolha_opcao) > 5:
                print('Opção inválida! Por gentileza, digite novamente.')
            else:
                print()
                break

        if escolha_opcao == 1:
            quantidade_pessoas_entra = int(input('Digite a quantidade de pessoas que entrarão no elevador: '))
            print(objeto_Elevador.entra(quantidade_pessoas_entra))
            pass
        elif escolha_opcao == 2:
            quantidade_pessoas_sai = int(input('Digite a quantidade de pessoas que sairão do elevador: '))
            print(objeto_Elevador.sai(quantidade_pessoas_sai))         
            pass
        elif escolha_opcao == 3:
            andar_sobe = int(input('Digite o andar que queira subir: '))
            print(objeto_Elevador.sobe(andar_sobe))
            pass
        elif escolha_opcao == 4:
            andar_desce = int(input('Digite o andar que queira descer: '))
            print(objeto_Elevador.desce(andar_desce))
            pass
        else:
            print('Obrigado por usar nossa ferramenta!!!! :)')
            break

        while True:
            validar_uso = input('Deseja realizar outra operação (S/N)? ').title().strip()
            if validar_uso != 'S' and validar_uso != 'Sim' and validar_uso != 'N' and validar_uso != 'Não' and validar_uso != 'Nao':
                print('Opção inválida! Por gentileza, digite novamente')
            else:
                break

        if validar_uso == 'N' or validar_uso == 'Não' or validar_uso == 'Nao':
            print('Obrigado por usar nossa ferramenta!!!! :)')
            break
        print()