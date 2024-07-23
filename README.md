# WiseOwl

WiseOwl é uma aplicação em Python que monitora os cliques do mouse e registra a janela ativa no momento do clique. Este log é salvo em um arquivo .txt selecionado pelo usuário. A aplicação é executada em segundo plano na barra de tarefas, representada por um ícone de coruja.

## Funcionalidades

- **Monitoramento de cliques do mouse:** Registra a data, hora, coordenadas do clique, qual botão do mouse clicado e a janela ativa no momento do clique. <br><br>Exemplo: 22-07-2024 22:06:55 - Click: 143, 23, Button.left, Window: WiseOwl.py - WiseOwl - Visual Studio Code <br><br>
- **Execução em segundo plano:** A aplicação é minimizada para a barra de tarefas, onde pode ser controlada através de um menu de ícone.
- **Log em arquivo .txt:** Os logs são salvos em um arquivo .txt selecionado pelo usuário.

## Como usar

1. Clone o repositório ou faça o download do código-fonte.
2. Garanta que você tenha o Python instalado.
3. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```
4. Execute o script Python:
    ```sh
    python WiseOwl.py
    ```
5. Escolha o caminho para o arquivo de log quando solicitado.
6. O ícone da coruja aparecerá na barra de tarefas. Clique com o botão direito no ícone para iniciar/parar o monitoramento, ou para sair do programa.

## Gerando o Executável

Para gerar um executável standalone, utilize o PyInstaller com o comando:

```sh
pyinstaller --onefile --noconsole --icon=coruja.ico --add-data "coruja.ico;." WiseOwl.py
```

#### Crédito da imagem:
A imagem da coruja foi encontrada no seguinte link:
(<a href="https://www.flaticon.com/br/icones-gratis/coruja" title="coruja ícones">Coruja ícones criados por Smashicons - Flaticon</a>)

### Desenvolvimento:

- [Vitor Luz](https://github.com/luz-vitor)

Obrigado!
 
