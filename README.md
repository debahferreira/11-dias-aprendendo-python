# 11 Dias Aprendendo Python

Estou indo para o segundo ano de faculdade e percebi que aprender python é importantíssimo para a minha jornada.
Por isso, com o auxílio do Gemini, por 11 dias (antes das minhas aulas voltarem),
vou desenvolver meus primeiros projetos de python, com a finalidade de aprender o máximo possível.

# 🚀 Projeto 1: Organizador Automático de Arquivos

Este script automatiza a organização de pastas, movendo arquivos para diretórios específicos com base em suas extensões. É o meu primeiro projeto prático focado em **automação de tarefas repetitivas** e manipulação de sistemas de arquivos.

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Biblioteca Principal:** `os` (Interface com o Sistema Operacional)
* **IDE:** Visual Studio Code
* **Sistema Operacional:** Linux (Ubuntu/Debian)

### 📂 Funcionalidades
* **Identificação Automática:** O script mapeia extensões como `.zip`, `.rar`, e `.tar.gz` para pastas específicas como "Compactados".
* **Criação Dinâmica:** Verifica se as pastas de destino já existem; caso contrário, cria-as automaticamente usando `os.mkdir`.
* **Gestão de Caminhos:** Utiliza `os.path.join` para garantir a integridade dos caminhos no Linux.

### 💻 Como Executar
1. Certifique-se de ter o Python instalado.
2. Certifique-se de que a pasta com os arquivos que você quer organizar (`Pasta Origem`) está dentro de outra pasta (`test_env`).
3. Copie e cole o script dentro de `test_env`.
4. Defina no script o `caminho` para a sua pasta de teste e o `caminho_pasta_origem`.
5. Execute o script via terminal (dentro da pasta `test_env`):
 
   ```bash
   python3 organizador.py

# 🚀 Projeto 2: Automação Scraping de Notícias

Este projeto é um script em Python desenvolvido para automatizar a extração das principais notícias do portal CNN Brasil. O foco principal foi criar um robô resiliente, capaz de lidar com instabilidades de rede através de uma lógica de retentativas e tratamento de exceções.

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Bibliotecas Principais:** `requests` (para realizar as requisições HTTP) e `BeautifulSoup4` (para a análise - parsing - do HTML)
* **Biblioteca Time:** para o gerenciamento de intervalos entre retentativas.
* **IDE:** Visual Studio Code
* **Sistema Operacional:** Linux (Ubuntu/Debian)

### 📂 Funcionalidades
* **Conexão Resiliente:** Implementação de laço `while` para tentar a conexão até 3 vezes em caso de falha.
* **Tratamento de Exceções:** Uso de blocos `try/except` para capturar erros de `Timeout` e `RequestException` do módulo `requests`.
* **Web Scraping Inteligente:** Extração de manchetes utilizando a biblioteca `BeautifulSoup` para navegar no HTML do site.
* **Limpeza de Dados:** Uso de manipulação de strings para remover espaços em branco e caracteres desnecessários dos títulos extraídos.

### 💻 Como Executar
1. Clone o repositório
2. Crie e ative o seu ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Instale as dependências:

   ```bash
   pip install requests beautifulsoup4

4. Execute o script:
 
   ```bash
   python3 seletor_manchetes.py
