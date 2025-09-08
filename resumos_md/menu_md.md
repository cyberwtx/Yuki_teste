# Resumo detalhado de menu.py

Este arquivo implementa o menu principal do bot, exibido ao usuário ao iniciar o comando /start.

**Fluxo principal:**
- Quando o usuário envia /start no privado, o bot exibe uma imagem de boas-vindas e apresenta o menu principal com botões interativos.
- Se o comando /start for usado em grupo, o bot orienta o usuário a acessar o bot no privado e exibe o botão 🤖 Acessar o Bot com link direto.

**Botões exibidos no menu principal:**
- 🟠 Login Crunchyroll: inicia o fluxo de compra ou sorteio de login.
- 👤 Minha Conta: exibe informações do login ativo do usuário.
- 💬 Ajuda: mostra informações de ajuda e perguntas frequentes.
- ▶️ Séries|Filmes|Canais: (em desenvolvimento) para acessar outros conteúdos.

**Botão exibido em grupo:**
- 🤖 Acessar o Bot: link direto para o chat privado do bot.

**Mensagens exibidas:**
- Mensagem de boas-vindas personalizada com o nome do usuário e instrução para escolher uma opção.
- Mensagem especial em grupo orientando a acessar o bot no privado.

**Objetivo:**
Proporcionar uma experiência inicial organizada, intuitiva e visualmente agradável para o usuário acessar os principais recursos do bot, com navegação facilitada pelos botões do menu.
