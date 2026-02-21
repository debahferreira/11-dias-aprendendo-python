import os, shutil

locais = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".csv"],
    "Executaveis": [".exe", ".deb", ".sh"],
    "Compactados": [".zip", ".rar", ".tar.gz"]
}

def main():

    #imprime qual a pasta em que estamos agora
    caminho = os.getcwd()
    print(caminho)

    #define pasta de onde vai tirar os arquivos
    pasta_origem = 'Pasta Origem'
    caminho_pasta_origem = os.path.join(caminho, pasta_origem)

    #imprime todos os arquivos que tem na pasta em que estamos
    arquivos_pasta = os.listdir(caminho_pasta_origem)
    print(arquivos_pasta)

    #loop que percorre cada pasta, ve se ela ja existe (senão, cria) e adiciona todos os arquivos com as extensoes corretas naquela pasta
    # for pasta, extensoes_permitidas in locais.items():
    #     caminho_mais_pasta = os.path.join(caminho, pasta)
    #     if not os.path.exists(caminho_mais_pasta):
    #         os.mkdir(pasta)
    #     for arquivo in arquivos_pasta:
    #         caminho_arquivo_antes = os.path.join(caminho_pasta_origem, arquivo)
    #         nome_arquivo, extensao = os.path.splitext(arquivo)
    #         if extensao in extensoes_permitidas:
    #             caminho_arquivo_depois = os.path.join(caminho_mais_pasta, arquivo)
    #             shutil.move(caminho_arquivo_antes, caminho_arquivo_depois)

    #loop que percorre os arquivos, vendo qual extensão eles tem
    for arquivo in arquivos_pasta:
        caminho_arquivo_antes = os.path.join(caminho_pasta_origem, arquivo)
        nome_arquivo, extensao = os.path.splitext(arquivo)
        #loop que verifica se aquela extensão pertence a alguma pasta
        for pasta, extensoes_permitidas in locais.items():
            if extensao in extensoes_permitidas:
                caminho_pasta = os.path.join(caminho, pasta)
                #verifica se a pasta ja existe, senão cria
                if not os.path.exists(caminho_pasta):
                    os.mkdir(caminho_pasta)
                #move o arquivo para a pasta
                caminho_arquivo_depois = os.path.join(caminho_pasta, arquivo)
                shutil.move(caminho_arquivo_antes, caminho_arquivo_depois)

if __name__ == "__main__":
    main()