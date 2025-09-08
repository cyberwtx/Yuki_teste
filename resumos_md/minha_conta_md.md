# Resumo detalhado de minha_conta.py

Este arquivo implementa o handler para exibir informações da conta Crunchyroll Premium do usuário.

**Fluxo principal:**
- Quando o usuário clica no botão 👤 Minha Conta, o bot busca no banco de dados as informações completas do login ativo do usuário.
- Se o usuário não tiver assinatura ativa, ele avisa.
- Se a assinatura estiver expirada, ele avisa.
- Se houver assinatura ativa, exibe:
    - Nome do login
    - Email
    - Senha
    - Data de validade (formato DD/MM/AAAA)
    - Dias restantes de assinatura
    - Imagem do login
    - Recomendações de segurança (não alterar senha, tentar novamente se sair da conta)
    - Contato do suporte (link para o dono do bot (Cyber_wTX))
- Utiliza o botão ↩️ Voltar ao Menu para facilitar a navegação do usuário.

**Objetivo:**
Fornecer ao usuário acesso rápido, seguro e detalhado às informações da sua assinatura Crunchyroll Premium, com navegação facilitada e suporte direto.
