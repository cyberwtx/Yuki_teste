# Resumo detalhado de oferta.py

Este arquivo implementa o handler que exibe a oferta Crunchyroll Premium ao usuário no Telegram.

**Fluxo principal:**
- Quando o usuário clica no botão 🟠 Login Crunchyroll (menu principal), o bot exibe a oferta Crunchyroll Premium.
- O bot verifica se há logins disponíveis no banco de dados.
- Se não houver logins disponíveis, o bot busca a próxima data de reposição e exibe uma mensagem informando o usuário sobre a falta de estoque e a previsão de chegada de novos logins.
- Se houver logins disponíveis, o bot calcula o valor do login (padrão ou com desconto, se o usuário for elegível).
- O valor padrão do login é R$ 5,50. Se o usuário tiver desconto ativo, o valor é reduzido em 20% (R$ 4,40).
- O valor original do produto fora do bot é R$ 19,99.
- O bot exibe uma imagem de oferta, o valor do login, a quantidade de vendas realizadas e informações sobre desconto.
- O texto da oferta é formatado em HTML, destacando o preço, economia, chamada para ação e informações de entrega automática.
- O usuário pode escolher entre comprar o login ou tentar o sorteio grátis através dos botões exibidos.

**Botões exibidos ao usuário:**
- 🔄 Escolher login: inicia o fluxo de escolha de login e pagamento.
- 🎁 Tentar grátis: inicia o fluxo do sorteio de login grátis.
- ↩️ Voltar ao Menu: retorna ao menu principal.

**Resumo das principais funções:**
- `calcular_valor_com_desconto(valor_base, desconto_ativo)`: retorna o valor do login com ou sem desconto.
- `montar_texto_oferta(vendas, valor, desconto_ativo)`: monta a mensagem da oferta, incluindo preço, vendas, economia, chamada para ação e informações extras.
- Handler principal: verifica estoque, calcula valores, monta mensagem e exibe a oferta ao usuário.

**Mensagens exibidas:**
- Se não há estoque: "😔 Estoque de logins Premium esgotado por alta demanda!\n\n🚀 Novo login disponível dia XX/XX/XXXX às 9h da manhã. Fique ligado!"
- Se há estoque: mensagem com preço, desconto, vendas, chamada para ação e botões para comprar ou tentar sorteio grátis.

**Objetivo:**
Apresentar de forma clara, atrativa e automatizada a oferta de assinatura Crunchyroll Premium, incentivando a conversão do usuário e facilitando a experiência de compra no bot.
