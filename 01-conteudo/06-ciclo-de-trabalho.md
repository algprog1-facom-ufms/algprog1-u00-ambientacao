# 6. O ciclo de trabalho de cada atividade

Toda atividade da disciplina segue o mesmo ciclo. Aprenda-o bem agora — ele se repete
em todas as unidades.

```
 ┌──────────┐   ┌────────┐   ┌──────────┐   ┌────────┐   ┌──────┐   ┌───────────┐
 │ 1 Clonar │ → │2 Editar│ → │3 Executar│ → │4 Commit│ → │5 Push│ → │6 Conferir │
 └──────────┘   └────────┘   └──────────┘   └────────┘   └──────┘   └───────────┘
   uma vez          ↑______________________________________________________|
                                 repita quantas vezes quiser
```

## 1. Clonar (uma vez por unidade)

**Clonar** é baixar uma cópia do repositório para o seu computador, já conectada ao
GitHub.

**Pelo VS Code**

1. No GitHub, abra o seu repositório da atividade, clique no botão verde **Code** e copie
   o endereço HTTPS.
2. No VS Code, abra a paleta (`Ctrl+Shift+P` / `Cmd+Shift+P`) e escolha **Git: Clone**.
3. Cole o endereço e escolha a pasta `algoritmos-programacao` como destino.
4. Quando o VS Code perguntar, clique em **Open** para abrir o repositório clonado.

**Pelo terminal**

```bash
cd algoritmos-programacao
git clone <endereço-do-seu-repositório>
cd <nome-do-seu-repositório>
code .
```

## 2. Editar

Abra o arquivo da atividade, leia o enunciado no topo e escreva sua solução abaixo do
`TODO`. Salve com `Ctrl+S` / `Cmd+S`.

> 💡 Ative **File → Auto Save** para não esquecer de salvar.

## 3. Executar

Sempre a partir da **pasta raiz** do repositório, no terminal integrado:

```bash
python 04-atividades/atividade02_primeiro_commit.py
```

(no macOS/Linux, `python3`). Compare a saída com o exemplo do enunciado.

## 4. Commit

**Pelo VS Code:** abra a aba **Source Control** (ícone de ramificação na barra lateral,
ou `Ctrl+Shift+G`). Os arquivos alterados aparecem listados.

1. Escreva uma mensagem curta no campo **Message**.
2. Clique em **Commit**. Se o VS Code perguntar se deseja incluir todas as alterações
   (*stage all changes*), responda **Yes**.

**Pelo terminal:**

```bash
git add .
git commit -m "Resolve atividade 02"
```

### Boas mensagens de commit

A mensagem deve dizer **o que** foi feito, de forma que você entenda daqui a um mês.

| ✅ Boa | ❌ Ruim |
|---|---|
| `Resolve atividade 02` | `aaa` |
| `Corrige acento na saída da atividade 05` | `mudanças` |
| `Preenche ficha do ambiente` | `commit` |
| `Adiciona desafio 01 (apresentação)` | `final agora vai` |

## 5. Push

**Pelo VS Code:** clique em **Sync Changes** (ou nos três pontos `...` → **Push**) na aba
Source Control.

**Pelo terminal:**

```bash
git push
```

## 6. Conferir o resultado

No navegador, abra o seu repositório:

1. Aba **Actions**: aguarde a execução terminar (cerca de 1 minuto).
2. **Releases** (coluna à direita da página inicial): abra a mais recente e veja a
   tabela PASS/FAIL.
3. Algum teste falhou? Volte ao passo 2, corrija, e faça novo commit + push.

## Problemas comuns

| Mensagem ou situação | O que fazer |
|---|---|
| `python: command not found` / `'python' não é reconhecido` | Use `python3` (macOS/Linux) ou `py` (Windows). Veja o [guia 4](04-python.md). |
| `can't open file ... No such file or directory` | Você não está na pasta raiz do repositório. Use `cd` até ela ou reabra a pasta no VS Code. |
| `Author identity unknown` | Faltou configurar `user.name` e `user.email` ([guia 5](05-vscode-e-git.md), passo 7). |
| `rejected ... fetch first` no push | O repositório no GitHub tem commits que você não tem. Execute `git pull` e depois `git push`. |
| `Permission denied` / `Repository not found` | Você está conectado(a) com outra conta, ou o repositório não é o seu. Confira a conta no GitHub. |
| Fiz commit, mas nada mudou no GitHub | Faltou o **push**. |

## Verificação

- [ ] Clonei o meu repositório desta unidade.
- [ ] Executei um programa a partir da pasta raiz.
- [ ] Fiz um commit com uma mensagem descritiva.
- [ ] Fiz push e encontrei o resultado em **Releases**.
