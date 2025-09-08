# Resumo detalhado de sorteio.py

Este arquivo implementa o sistema de sorteio (roleta) para os usuários tentarem ganhar um login Crunchyroll Premium grátis ou desconto.

Fluxo principal:
- O usuário acessa o sorteio clicando no botão "🎁 Tentar grátis" na oferta.
- Para participar, o usuário precisa ter pelo menos 5 mensagens no grupo Crunchyroll Grátis.
- O temppo de espera entre um giro e outro é de 8 horas.
- Se o usuário não cumprir os requisitos, recebe uma mensagem informando quantas mensagens faltam ou quanto tempo deve esperar para tentar novamente.
- Se o usuário já tem um login ativo, recebe uma mensagem informando quantos dias ainda restam de assinatura.
- Se houver logins disponíveis, o usuário pode girar a roleta clicando no botão "🎲 Sortear".
- O sorteio gera um número aleatório de 5 dígitos e apresenta o resultado:
    - 5 dígitos iguais: ganha um login Crunchyroll Premium grátis.
    - 4 dígitos iguais: ganha 20% de desconto na próxima compra.
    - 5 dígitos diferentes: não ganha, pode tentar novamente após o tempo de espera.
- O bot registra a tentativa, entrega o prêmio ou desconto automaticamente e atualiza o banco de dados.
- O usuário pode ver estatísticas do sorteio clicando no botão "📊 Ver Estatísticas".

Botões exibidos ao usuário:
- 🎲 Sortear: gira a roleta e participa do sorteio.
- 📊 Ver Estatísticas: mostra estatísticas de prêmios e descontos distribuídos.
- ↩️ Voltar ao Menu: retorna ao menu principal.
- 👤 Minha Conta: exibido quando o usuário ganha o prêmio, para acessar os dados do login.
- 🔄 Escolher login: exibido quando o usuário ganha desconto, para iniciar a compra com desconto.

Mensagens exibidas:
- Mensagem de introdução explicando as regras do sorteio.
- Mensagem de resultado do sorteio, informando se ganhou prêmio, desconto ou se deve tentar novamente.
- Mensagem de erro ou de requisitos não cumpridos (mensagens ou tempo de espera).
- Mensagem de estatísticas do sorteio.

Objetivo:
Engajar os usuários e oferecer oportunidades de ganhar benefícios, incentivando a participação no grupo e a interação com o bot.
