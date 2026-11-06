# 03 — PRIMM: Meu primeiro programa

**PRIMM** é uma forma de aprender programação **lendo antes de escrever**. São cinco
etapas, sempre nesta ordem:

| Etapa | Em inglês | O que você faz | Arquivo |
|:-:|---|---|---|
| **P** | *Predict* | **Prever** a saída, só lendo o código | `respostas.md` |
| **R** | *Run* | **Executar** e comparar com sua previsão | `respostas.md` |
| **I** | *Investigate* | **Investigar** como cada linha funciona | `respostas.md` |
| **M** | *Modify* | **Modificar** o programa para fazer algo novo | `p4_modificar.py` ✅ |
| **M** | *Make* | **Criar** um programa novo, do zero | `p5_criar.py` ✅ |

✅ = corrigido automaticamente. As etapas P, R e I são registradas em `respostas.md`
e comentadas pelo professor no Pull Request de Feedback.

> 🧠 Não pule a previsão! Errar a previsão e descobrir **por quê** é exatamente o que
> faz você aprender.

> 💾 Faça um **commit depois de cada etapa** (P, R, I, M, M). Assim você pratica o ciclo
> de trabalho e o histórico mostra como o seu raciocínio evoluiu.

---

## O programa

Arquivo: [`p1_programa.py`](p1_programa.py) — **não altere este arquivo.**

```python
# Programa: Meu primeiro programa
print("Olá, mundo!")
print("Estou começando a programar em Python.")
print()
print("Até a próxima aula!")
```

---

## P — Prever (sem executar!)

Leia o programa e responda em `respostas.md`:

1. Quantas instruções `print` existem no programa?
2. Escreva **exatamente** a saída que você espera ver na tela.
3. O que você acha que a instrução `print()`, sem nada entre os parênteses, faz?
4. A primeira linha começa com `#`. Ela aparecerá na tela?

## R — Executar

```bash
python 03-primm/p1_programa.py
```

5. Sua previsão estava correta? Marque o que acertou e o que errou.
6. Se errou alguma coisa, qual foi a surpresa?

## I — Investigar

Responda fazendo **experimentos em uma cópia** (crie um arquivo `rascunho.py` na raiz
do repositório — ele não é enviado ao GitHub):

7. Troque o texto da primeira instrução por outro e execute. O que mudou?
8. Acrescente uma nova instrução `print("...")` no final. Onde o texto apareceu?
9. Troque a ordem das duas primeiras instruções. O que isso mostra sobre a ordem em que
   o Python executa as linhas?
10. Apague as aspas de fechamento de um dos textos e execute. Copie a **primeira linha**
    e a **última linha** da mensagem de erro. Em que linha o Python apontou o problema?

## M — Modificar → `p4_modificar.py`

O arquivo `p4_modificar.py` já contém uma cópia do programa. Altere-o para que:

1. A primeira linha seja **`Olá! Meu nome é <seu primeiro nome ou apelido>.`**
2. A segunda linha seja **`Estou cursando Algoritmos e Programação I.`**
3. A linha em branco continue no mesmo lugar.
4. A última linha seja **`Espero aprender <complete com uma frase sua>`**

Exemplo de execução:

<pre>
Olá! Meu nome é Marina.
Estou cursando Algoritmos e Programação I.

Espero aprender a criar meus próprios programas
</pre>

> Use o nome que preferir. Não inclua informações pessoais que não queira compartilhar.

## M — Criar → `p5_criar.py`

Agora, do zero, crie um programa que exiba o "checklist" do seu ambiente:

<pre>
=== Meu ambiente de programação ===
Python: instalado
VS Code: instalado
Git: instalado
GitHub: conta criada
Pronto(a) para a Unidade 01!
</pre>

> 💡 Dica: são seis instruções `print`, uma para cada linha. Confira acentos,
> dois-pontos e espaços: a correção compara a saída **exatamente**.
