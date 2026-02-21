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
