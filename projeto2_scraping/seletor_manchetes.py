#este programa entra no site da CNN, encontra a primeira manchete do dia, e imprime ela no terminal
import requests, time

def main():

    i = 3
    sucesso = 0

    while(not sucesso and i > 0):

        try:
            #tenta acessar o site
            response = requests.get('https://www.cnnbrasil.com.br/', timeout = 10)

            #verifica se a requisição deu certo
            response.raise_for_status()

            #caso sim:
            sucesso = 1
            print('Sucesso!')
            print(response)
        #caso não de certo
        except requests.exceptions.Timeout:
            print('O site demorou muito para responder.')
            time.sleep(5)
            i -= 1
        except requests.exceptions.RequestException as e:
            print(f'Ocorreu um erro: {e}')
            time.sleep(5)
            i -= 1

if __name__ == "__main__":
    main()