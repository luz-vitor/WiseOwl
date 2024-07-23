# WiseOwl

WiseOwl é uma aplicação em Python que monitora os cliques do mouse e registra a janela ativa no momento do clique. Este log é salvo em um arquivo .txt selecionado pelo usuário. A aplicação é executada em segundo plano na barra de tarefas, utilizando um ícone de coruja.

## Funcionalidades

- **Monitoramento de cliques do mouse:** Registra as coordenadas do clique e a janela ativa no momento do clique.
- **Execução em segundo plano:** A aplicação é minimizada para a barra de tarefas, onde pode ser controlada através de um menu de ícone.
- **Log em arquivo .txt:** Os logs são salvos em um arquivo .txt selecionado pelo usuário.

## Como usar

1. Clone o repositório ou faça o download do código-fonte.
2. Garanta que você tenha o Python 3.x instalado.
3. Instale as dependências necessárias:
    ```sh
    pip install pygetwindow pynput pystray Pillow
    ```
4. Execute o script Python:
    ```sh
    python WiseOwl.py
    ```
5. Escolha o caminho para o arquivo de log quando solicitado.
6. O ícone da coruja aparecerá na barra de tarefas. Clique com o botão direito no ícone para iniciar ou parar o monitoramento, ou para sair do programa.

## Gerando o Executável

Para gerar um executável standalone, utilize o PyInstaller com o comando:

```sh
pyinstaller --onefile --noconsole --icon=coruja.ico --add-data "coruja.ico;." WiseOwl.py
