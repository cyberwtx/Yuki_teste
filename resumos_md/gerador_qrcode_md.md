# Resumo detalhado de gerador_qrcode.py

Este arquivo gerencia todo o fluxo de pagamento via Pix para aquisição do Crunchyroll Premium no bot.

**Fluxo principal:**
- Quando o usuário escolhe um login e clica no botão <b>💸 Assinar</b>, o bot inicia o fluxo de pagamento Pix.
- O bot gera um código Pix (copia e cola) exclusivo para o pagamento e exibe uma mensagem com:
    - O valor a ser pago.
    - O código Pix para copiar e colar no app do banco.
    - O tempo de validade do Pix (5 minutos). Após esse tempo, o pagamento expira automaticamente.
    - Um botão <b>❌ Cancelar pagamento</b> para o usuário desistir da compra a qualquer momento.
- O bot monitora o status do pagamento em tempo real:
    - Se o pagamento for aprovado dentro do prazo, o bot libera automaticamente o acesso ao login Crunchyroll Premium e atualiza o banco de dados.
    - Se o pagamento expirar ou for cancelado, o login volta para o estoque e o usuário é informado.
- O usuário recebe mensagens de confirmação e instruções após o pagamento:
    - Mensagem de sucesso: acesso liberado imediatamente e botão <b>👤 Minha Conta</b> para acessar os dados.
    - Mensagem de erro ou expiração: instruções para tentar novamente e botão <b>↩️ Voltar ao Menu</b>.

**Objetivo:**
Automatizar o processo de pagamento e entrega do serviço Crunchyroll Premium de forma segura, rápida e eficiente, garantindo uma experiência fluida para o usuário dentro do bot.
