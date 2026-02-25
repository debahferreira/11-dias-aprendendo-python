#este projeto salva várias vezes os preços de um determinado produto em uma tabela e avisa quando há promoção

import requests
from bs4 import BeautifulSoup

def main():

    sucesso = 0
    i = 3

    #enquanto der erro ao acessar o site, tenta 3 vezes
    while(not sucesso and i > 0):
        #tenta acessar
        try:
            response = requests.get('https://www.ovnivegano.com.br/proteinas', timeout = 8)
            print(response.status_code)

            #se der erro, vai pros except:
            response.raise_for_status()

            #senão, sucesso
            sucesso = 1
            print('Sucesso!')

        except requests.exceptions.Timeout:
            print('Erro: tempo de resposta excedido.')
            i -= 1
        except requests.exceptions.RequestException as e:
            print(f'Erro: {e}')
            i -= 1

    #se tiver sucesso, continua com a lógica:
    if(sucesso):
        #pega dados brutos do site e transforma em uma árvore (parsing)
        soup = BeautifulSoup(response.text, 'html.parser')

        #encontra o preço de um produto específico
        for preco in soup.find_all('span'):
            print(preco)


if __name__ == "__main__":
    main()