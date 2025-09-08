# Resumo detalhado de status.py

Este arquivo implementa o comando /status, que exibe informações sobre o funcionamento do bot e estatísticas do sistema.

Fluxo principal:
- O usuário envia o comando /status no chat.
- O bot testa a conexão com o banco de dados antes de exibir as informações.
- O bot calcula o uptime (tempo online) desde o último start, o ping (tempo de resposta), a quantidade de logins disponíveis, o total de vendas e a versão do bot.
- As informações são exibidas em uma mensagem formatada, incluindo o nome do dono do bot e um link para contato.
- Em caso de erro ao acessar o banco de dados, o bot exibe uma mensagem de erro detalhada para o usuário.

Informações exibidas ao usuário:
- Uptime do bot (tempo online em dias, horas, minutos e segundos)
- Ping (tempo de resposta em milissegundos)
- Logins disponíveis
- Vendas totais
- Versão do bot
- Nome e contato do dono do bot

Mensagens exibidas:
- Mensagem de status com todos os dados acima quando tudo está funcionando normalmente.
- Mensagem de erro detalhada caso haja problema ao acessar o banco de dados.

Objetivo:
Fornecer transparência e monitoramento do funcionamento do bot para administradores e usuários, facilitando o diagnóstico de problemas e o acompanhamento do desempenho do sistema.
