# 5. VS Code e Git

O **Visual Studio Code (VS Code)** será o editor de código padrão da disciplina. Ele
permite editar programas, executá-los em um terminal integrado e — junto com o
**Git** — registrar e enviar suas alterações para o GitHub.

## Parte A — VS Code

### 1. Baixar e instalar

Acesse o site oficial:

[https://code.visualstudio.com/](https://code.visualstudio.com/)

Baixe a versão adequada ao seu sistema operacional e siga as instruções de instalação.

> No Windows, durante a instalação, marque a opção **Add to PATH** (se aparecer). Ela
> permite abrir o VS Code pelo terminal com o comando `code .`.

### 2. Instalar a extensão Python

1. Abra o VS Code.
2. Selecione o ícone **Extensions** na barra lateral (ou use `Ctrl+Shift+X` no
   Windows/Linux e `Cmd+Shift+X` no macOS).
3. Pesquise por **Python**.
4. Instale a extensão **Python**, publicada pela Microsoft.
5. Se solicitado, permita a instalação de componentes recomendados.

A extensão auxilia na edição, execução e depuração de programas Python. Ela não
substitui a instalação do interpretador Python ([guia 4](04-python.md)).

> 💡 Os repositórios da disciplina já trazem a recomendação dessa extensão: ao abrir um
> deles, o VS Code oferece a instalação automaticamente.

### 3. Criar uma pasta para a disciplina

1. Crie uma pasta no computador chamada `algoritmos-programacao`.
2. É **dentro dela** que você vai clonar o repositório de cada unidade:

```
algoritmos-programacao/
├── <seu repositório da unidade 00>/
├── <seu repositório da unidade 01>/
└── ...
```

O nome exato de cada repositório é criado pelo Classroom 50 e termina com o seu username.

Organizar assim facilita localizar os programas e mantém os materiais da disciplina
separados de outros projetos.

### 4. Selecionar o interpretador Python

1. Abra a paleta de comandos: `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS).
2. Digite `Python: Select Interpreter`.
3. Selecione a instalação do Python 3 que você instalou.
4. Confira se o interpretador selecionado aparece na barra de status.

Se nenhum interpretador aparecer, confira a instalação do Python e reinicie o VS Code.

### 5. Abrir o terminal integrado

No menu, escolha **Terminal → New Terminal**. O terminal será aberto na parte inferior
da janela. Você vai utilizá-lo para executar programas, ler mensagens de erro e usar o
Git.

## Parte B — Git

O **Git** é o programa que, no seu computador, cria os commits e faz o push para o
GitHub. O VS Code usa o Git "por baixo" dos botões da aba **Source Control**.

### 6. Instalar o Git

Abra o terminal e verifique se o Git já está instalado:

```bash
git --version
```

Se aparecer algo como `git version 2.xx`, pule para o passo 7. Caso contrário:

- **Windows:** baixe o instalador em [git-scm.com/downloads](https://git-scm.com/downloads)
  e mantenha as opções padrão. Ele também instala o **Git Credential Manager**, que
  cuida do login no GitHub.
- **macOS:** execute `git --version` — o sistema oferecerá a instalação das
  *Command Line Tools*. Aceite.
- **Linux:** use o gerenciador de pacotes da distribuição (ex.: `sudo apt install git`).

Feche e abra novamente o VS Code depois de instalar.

### 7. Identificar-se para o Git (uma única vez)

Cada commit registra quem o fez. Configure seu nome e o **mesmo e-mail da sua conta
GitHub**:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

Confira com:

```bash
git config --global --list
```

> 💡 Se não quiser expor seu e-mail, o GitHub oferece um endereço do tipo
> `12345+username@users.noreply.github.com` em **Settings → Emails**. Você pode usá-lo
> no lugar do e-mail real.

### 8. Conectar o VS Code à sua conta GitHub

Na primeira vez que você clonar ou fizer push de um repositório privado, o VS Code (ou
o Git Credential Manager) abrirá o navegador pedindo para **autorizar o acesso** à sua
conta. Confira se é a conta correta e autorize.

> ⚠️ Nunca cole sua senha ou um token em arquivos do repositório.

## Documentação oficial

- [Download do VS Code](https://code.visualstudio.com/)
- [Python no VS Code](https://code.visualstudio.com/docs/languages/python)
- [Git no VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [Download do Git](https://git-scm.com/downloads)

## Verificação

- [ ] Instalei o VS Code e a extensão Python da Microsoft.
- [ ] Criei a pasta `algoritmos-programacao`.
- [ ] Selecionei o interpretador Python 3.
- [ ] Consegui abrir o terminal integrado.
- [ ] `git --version` mostra a versão do Git.
- [ ] Configurei `user.name` e `user.email`.
