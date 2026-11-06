# 4. Instalação do Python

Python é a linguagem de programação que utilizaremos na disciplina. Para executar programas no computador, precisamos instalar o interpretador Python.

## 1. Baixar o Python

Acesse o site oficial:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Baixe uma versão estável do Python 3 compatível com seu sistema operacional.

## 2. Instalar no Windows

1. Execute o instalador baixado do site oficial.
2. Na primeira tela, marque **Add Python to PATH**, se essa opção estiver disponível.
3. Clique em **Install Now**.
4. Aguarde a conclusão da instalação.

Se a opção de adicionar Python ao PATH não aparecer, a instalação ainda poderá ser concluída; nesse caso, será necessário selecionar o interpretador pelo VS Code ou ajustar o PATH posteriormente.

## 3. Instalar no macOS ou Linux

Siga as instruções oficiais para seu sistema operacional. Em algumas distribuições Linux, o Python 3 já está instalado. Evite remover ou substituir a versão de Python utilizada pelo próprio sistema.

## 4. Verificar a instalação

Abra um terminal.

No Windows, tente:

```bash
python --version
```

Se o comando não for reconhecido, tente:

```bash
py --version
```

No macOS ou Linux, tente:

```bash
python3 --version
```

O terminal deverá apresentar uma versão do Python 3.

## 5. Problemas comuns

- **Comando não encontrado:** feche e abra novamente o terminal; confira se a instalação foi concluída e se o Python está no PATH.
- **Mais de uma versão instalada:** não desinstale versões sem orientação. No VS Code, selecione explicitamente o interpretador que será utilizado.
- **Permissão negada:** não execute comandos aleatórios com privilégios de administrador. Consulte o professor ou a documentação oficial.

## Documentação oficial

- [Downloads do Python](https://www.python.org/downloads/)
- [Documentação do Python](https://docs.python.org/3/)

## Verificação

- [ ] Instalei o Python 3.
- [ ] Abri um terminal.
- [ ] Executei o comando de verificação.
- [ ] Consegui identificar a versão instalada.
