#este programa entra no site da CNN, encontra as manchetes do dia e imprime a lista de manchetes no terminal
import requests, time
from bs4 import BeautifulSoup


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

    #se conseguiu acessar o site
    if(sucesso):
        #acessa o conteudo 
        soup = BeautifulSoup(response.text, 'html.parser')
        #cria uma lista de títulos
        titulos = soup.find_all('h2')

        #imprime os titulos da lista
        print('\nLista de manchetes do dia:')
        for indice, titulo in enumerate(titulos):
            print(indice + 1, titulo.text.strip())


if __name__ == "__main__":
    main()