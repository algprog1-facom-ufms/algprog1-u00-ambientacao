# 2. Primeiros passos com GitHub

O GitHub é uma plataforma para hospedar e organizar projetos e arquivos. É usado por
milhões de desenvolvedores no mundo todo. Na disciplina, ele será o lugar onde ficam os
materiais **e** o seu trabalho: cada atividade é um repositório só seu.

## 1. Criar sua conta

Se ainda não possui uma conta, acesse [github.com/signup](https://github.com/signup).
Utilize um endereço de e-mail que você consiga acessar e conclua a confirmação
solicitada pelo GitHub.

Escolha um **username** que seja fácil de identificar e compartilhar com o professor.

> 💡 Essa conta pode acompanhar você por toda a carreira — um portfólio de projetos no
> GitHub é valorizado em estágios e empregos. Escolha um username profissional.

## 2. Identificar seu perfil

Seu perfil estará disponível em um endereço semelhante a:

`https://github.com/seu-username`

O username é diferente do nome de exibição do perfil. É o identificador que será
utilizado no cadastro da turma.

## 3. Conhecer um repositório

Um **repositório** (*repository*, ou *repo*) é um espaço para armazenar os arquivos de
um projeto **e todo o histórico de alterações** desses arquivos. Neste curso, os
repositórios conterão:

- materiais e exemplos;
- enunciados de atividades;
- arquivos de código Python;
- instruções e documentação (arquivos `.md`).

Ao abrir um repositório no navegador, você vê a lista de arquivos e pastas e, logo
abaixo, o conteúdo do arquivo `README.md`, que funciona como a "capa" do projeto.

> 📝 Os arquivos `.md` são escritos em **Markdown**, uma forma simples de formatar texto:
> `# Título`, `**negrito**`, `- item de lista`. O GitHub exibe esses arquivos já
> formatados. Você vai praticar no [desafio 03](../05-desafios/README.md).

## 4. O que é um commit?

Um **commit** registra um conjunto de alterações feitas nos arquivos de um repositório,
com uma mensagem que descreve o que foi feito. Pense nele como um "ponto de
salvamento" identificado de uma etapa do trabalho.

```
commit 3  "Resolve atividade 02"        ← mais recente
commit 2  "Preenche ficha do ambiente"
commit 1  "Código inicial da unidade"   ← criado quando você aceitou a atividade
```

Com os commits é possível ver **o que mudou, quando e por quê** — e voltar a uma
versão anterior se algo der errado.

## 5. O que é um push?

O commit fica registrado **no seu computador**. O **push** envia os commits para o
GitHub. Só depois do push o professor (e a correção automática) enxerga o seu trabalho.

```
Seu computador                         GitHub
  editar → salvar → commit  ── push ──▶  repositório da atividade
```

## 6. Cuidados com a conta

- Nunca compartilhe sua senha.
- Nunca publique tokens de acesso.
- Ative a **autenticação em dois fatores (2FA)**: em **Settings → Password and
  authentication**. O GitHub exige 2FA para quem contribui com código.
- Guarde os **códigos de recuperação** em local seguro — sem eles, perder o celular pode
  significar perder a conta.
- Confira se está utilizando a conta correta antes de trabalhar em uma atividade.

> **Importante:** a disciplina **nunca** solicitará sua senha, token de acesso ou
> códigos de autenticação.

## 7. Benefícios para estudantes (opcional)

O [GitHub Education](https://education.github.com/students) oferece gratuitamente a
estudantes verificados ferramentas como o GitHub Copilot e o GitHub Codespaces. A
verificação usa o seu e-mail institucional ou um comprovante de matrícula. Antes de
usar o Copilot nas atividades, leia as regras do [guia 7](07-ia-e-integridade.md).

## Verificação

- [ ] Consigo entrar na minha conta GitHub.
- [ ] Sei localizar meu username.
- [ ] Ativei a autenticação em dois fatores.
- [ ] Sei explicar a diferença entre **commit** e **push**.
- [ ] Sei identificar a lista de arquivos e o README de um repositório.

> O cadastro dos estudantes no Classroom 50 será orientado pelo professor no momento
> indicado.
