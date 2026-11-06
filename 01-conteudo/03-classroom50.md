# 3. Como funcionam as atividades no Classroom 50

O **Classroom 50** é a ferramenta que distribui as atividades e as corrige
automaticamente. Ele funciona inteiramente dentro do GitHub: você não precisa criar
outra conta.

## 1. Aceitar a atividade

Para cada unidade, o professor divulgará um **link de aceite**.

1. Abra o link estando conectado(a) à sua conta GitHub.
2. Confirme o aceite.
3. O Classroom 50 cria um **repositório só seu**, privado, com uma cópia de todos os
   arquivos da unidade.

Somente você e a equipe da disciplina conseguem ver esse repositório.

> 💡 Guarde o endereço do seu repositório. É nele que você vai trabalhar a unidade
> inteira — clone-o no VS Code seguindo o [guia 6](06-ciclo-de-trabalho.md).

## 2. As partes do seu repositório

| Onde | O que você encontra |
|---|---|
| **Code** (página inicial) | Os arquivos da unidade e o `README.md` com o roteiro |
| **Actions** | A execução da correção automática a cada `push` (🟡 rodando, ✅ concluída, ❌ erro) |
| **Releases** | O resultado de cada envio: a tabela **PASS/FAIL** de cada teste e a pontuação |
| **Pull requests → Feedback** | Os comentários do professor sobre o seu trabalho, linha a linha |
| **Issues** | O lugar para registrar dúvidas e problemas sobre a unidade |

## 3. A correção automática

A cada `push`:

1. O Classroom 50 executa os seus programas com algumas entradas de teste.
2. Cada teste compara a saída do seu programa com a saída esperada.
3. O resultado aparece em **Releases** como uma tabela, por exemplo:

| Teste | Resultado |
|---|:-:|
| A02: mensagem do primeiro commit | ✅ PASS |
| A05: programa executa sem erro | ❌ FAIL |

O teste mostra **o nome** do que está sendo verificado, mas não a resposta. Se um teste
falhar, releia o enunciado e compare a saída do seu programa caractere por caractere.

> ⚠️ Os testes usam **entradas diferentes** das do exemplo do enunciado. Um programa que
> apenas copia a saída do exemplo não passa.

## 4. O Pull Request de Feedback

Na aba **Pull requests** existe um PR chamado **Feedback**. Ele mostra tudo o que você
alterou desde o código inicial, e é ali que o professor deixa comentários.

- **Não feche** e **não faça merge** desse PR.
- Você pode responder aos comentários e fazer perguntas ali, mencionando o professor.

## 5. Regras que evitam perder pontos

- Não renomeie nem mova arquivos: os testes procuram cada um em um caminho fixo.
- Não apague o enunciado nem o comentário `TODO` dos arquivos.
- Faça `push` antes do prazo. O que não foi enviado não é corrigido.
- Confira o resultado em **Releases** depois de cada envio.

## Verificação

- [ ] Sei o que acontece quando aceito o link de uma atividade.
- [ ] Sei onde ver o resultado da correção automática (Releases e Actions).
- [ ] Sei onde o professor comenta o meu trabalho (PR de Feedback).
- [ ] Sei onde registrar uma dúvida (Issues).
