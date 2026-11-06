# Unidade 00 — Ambientação

**Algoritmos e Programação I** · Python · GitHub · VS Code · Classroom 50

Bem-vindo(a) à disciplina! Antes de começar a programar, você vai entender **como a
disciplina funciona**, preparar o seu computador (Python, VS Code e Git) e fazer o
caminho completo de uma entrega: abrir este repositório, alterar um arquivo, fazer
`commit` + `push` e ver a correção automática acontecer.

Tudo o que você fizer aqui será repetido em todas as unidades. Por isso, esta unidade
vale como um **ensaio geral**: errar agora é barato e ajuda muito depois.

---

## 🎯 Objetivos de aprendizagem

Ao final desta unidade, você será capaz de:

1. Explicar como a disciplina está organizada (unidades, roteiro de estudo, PRIMM, avaliação).
2. Usar sua conta no GitHub com segurança e reconhecer **repositório**, **commit** e **push**.
3. Entender como as atividades chegam e são corrigidas pelo **Classroom 50**.
4. Instalar e verificar o **Python 3**, o **VS Code** e o **Git**.
5. Abrir um repositório no VS Code, **executar** um programa Python e **enviar** alterações.
6. Ler o resultado da correção automática (**Releases**, **Actions**) e o **PR de Feedback**.
7. Conhecer as regras de uso de **Inteligência Artificial** na disciplina.

---

## 🗺️ Roteiro de estudo (siga nesta ordem)

| Passo | Pasta | O que fazer | Tempo estimado |
|:---:|---|---|:---:|
| 1 | [`01-conteudo/`](01-conteudo/) | Ler os 7 guias (disciplina, GitHub, Classroom 50, Python, VS Code e Git, ciclo de trabalho, IA) e instalar as ferramentas | 2h |
| 2 | [`02-exemplos/`](02-exemplos/) | Executar os programas de exemplo e verificar o ambiente | 20 min |
| 3 | [`03-primm/`](03-primm/) | Fazer a sequência PRIMM com o seu primeiro programa | 40 min |
| 4 | [`04-atividades/`](04-atividades/) | Resolver as 6 atividades de ambientação | 1h |
| 5 | [`05-desafios/`](05-desafios/) | Resolver os 3 desafios | 40 min |
| 6 | [`06-autoavaliacao/`](06-autoavaliacao/) | Responder o questionário e a reflexão | 20 min |

> 💡 Se a instalação travar em algum passo, não desista da unidade: abra uma **Issue**
> neste repositório descrevendo o problema (com o print da mensagem de erro) e
> continue lendo o conteúdo enquanto aguarda ajuda.

---

## 🛠️ Como trabalhar neste repositório

> Os passos abaixo estão explicados com calma em
> [`01-conteudo/06-ciclo-de-trabalho.md`](01-conteudo/06-ciclo-de-trabalho.md).

### 1. Abra no VS Code

```bash
git clone <endereço-do-seu-repositório>
cd <nome-do-seu-repositório>
code .
```

> Ao abrir, o VS Code vai sugerir a extensão **Python** (Microsoft). Instale-a.

### 2. Execute um programa

No terminal do VS Code (menu **Terminal → New Terminal**), a partir da pasta raiz:

```bash
python 02-exemplos/ex01_hello.py
```

> No Linux/macOS pode ser necessário usar `python3` no lugar de `python`.

### 3. Resolva as atividades

Cada arquivo em `03-primm/`, `04-atividades/` e `05-desafios/` contém o enunciado
no topo e um espaço marcado com `TODO` onde você deve trabalhar.

⚠️ **Não renomeie nem mova os arquivos** — a correção automática procura por eles
exatamente nesses caminhos.

### 4. Envie (commit + push)

```bash
git add .
git commit -m "Resolve atividade 01"
git push
```

Você pode (e deve!) enviar várias vezes. **Cada `push` dispara a correção automática.**

---

## ✅ Correção automática e feedback

- A cada `push`, o Classroom 50 executa seus programas e confere os arquivos pedidos.
- O resultado aparece em **Releases** (tabela PASS/FAIL por teste) e na aba **Actions**.
- Na aba **Pull requests** existe um PR chamado **Feedback**. É lá que o professor
  comenta seu trabalho. **Não feche nem faça merge desse PR.**

> 💡 Dica: siga **exatamente** os textos pedidos nos enunciados (acentos, pontuação e
> letras maiúsculas). Para o computador, `Olá, mundo!` e `ola mundo` são diferentes.

### Distribuição da pontuação

| Bloco | Pontos |
|---|:---:|
| 03 – PRIMM (Modificar + Criar) | 20 |
| 04 – Atividades (6) | 55 |
| 05 – Desafios (3) | 25 |
| **Total** | **100** |

O questionário de autoavaliação não vale nota automática, mas é parte da entrega.

---

## 📁 Estrutura

```
.
├── README.md
├── 01-conteudo/        Guias: disciplina, GitHub, Classroom 50, instalação e uso das ferramentas
├── 02-exemplos/        Programas para executar e verificar o ambiente
├── 03-primm/           Sequência Predict–Run–Investigate–Modify–Make
├── 04-atividades/      Atividades de ambientação
├── 05-desafios/        Problemas para resolução autônoma
└── 06-autoavaliacao/   Questões de revisão e reflexão
```

---

Dúvidas? Abra uma **Issue** neste repositório ou comente no Pull Request de Feedback.
