# services/atendimento.py
from aiogram import Router, F
from aiogram.types import Message
import aiohttp
import os
from services.config import GROUP_ID, NLP_KEY, BOT_URL, OWNER_ID
from collections import defaultdict, deque
from aiogram.enums import ChatType

atendimento_router = Router()

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={NLP_KEY}"

_md_cache = {}

async def get_md_content(md_filename: str) -> str:
    if md_filename in _md_cache:
        return _md_cache[md_filename]
    pasta = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resumos_md")
    caminho = os.path.join(pasta, md_filename)
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read().replace("{BOT_URL}", BOT_URL)
                _md_cache[md_filename] = conteudo
                return conteudo
        except Exception:
            return ""
    return ""

async def get_resumos_md_content() -> str:
    if "resumos_md" in _md_cache:
        return _md_cache["resumos_md"]
    pasta = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resumos_md")
    textos = []
    if os.path.exists(pasta):
        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.endswith(".md") and not nome_arquivo.startswith("yuki_"):
                caminho = os.path.join(pasta, nome_arquivo)
                try:
                    with open(caminho, "r", encoding="utf-8") as f:
                        textos.append(f"\n===== [RESUMO: {nome_arquivo}] =====\n" + f.read())
                except Exception:
                    pass
    resumos_texto = "\n".join(textos)
    _md_cache["resumos_md"] = resumos_texto
    return resumos_texto

keywords = [
    "yuki", "bot", "login", "crunchyroll", "sorteio", "desconto", "pix", "pagamento", "ajuda", "suporte", "ajudar", "quanto custa", "quanto é", "é verdade", "funciona mesmo",
    "regras", "banimento", "validade", "preço", "valor", "grupo", "assinar", "comprar", "logar", "de graça", "é grátis", "minha conta", "confiável", "anime", "animes", "manga", "doramas",
    # Nomes de serviços de streaming para detectar vendas proibidas
    "netflix", "disney", "prime", "primevideo", "prime video", "hbo", "hbo max", "globoplay", "paramount",
    "star+", "star plus", "starplus", "iptv", "spotify", "deezer", "apple tv", "appletv", "telecine",
    "tele cine", "looke", "now", "claro tv", "directv", "directv go", "directvgo", "amazon video",
    "amazon prime", "amazonprime", "streaming", "login premium", "login compartilhado", "login barato"
]

OWNER_ID = int(OWNER_ID)

# Contexto de conversa por usuário (últimas 5 interações)
user_contexts = defaultdict(lambda: deque(maxlen=10))

# Função para montar o contexto do usuário
async def get_user_context(user_id):
    ctx = user_contexts[user_id]
    if not ctx:
        return ""
    return "\n".join(ctx)

# Função para adicionar interação ao contexto
async def add_to_user_context(user_id, user_msg, bot_msg):
    user_contexts[user_id].append(f"Usuário: {user_msg}")
    user_contexts[user_id].append(f"Yuki: {bot_msg}")

# Modifique get_gemini_response para receber contexto opcional
async def get_gemini_response(message: str, prompt_file: str, context: str = "") -> str:
    prompt_md = await get_md_content(prompt_file)
    resumos_md = await get_resumos_md_content()
    if context:
        prompt = f"{prompt_md}\n\n================ [BASE DE CONHECIMENTO DO SISTEMA] ================\n{resumos_md}\n\n[CONVERSA ANTERIOR]\n{context}\n\nUsuário: {message}"
    else:
        prompt = f"{prompt_md}\n\n================ [BASE DE CONHECIMENTO DO SISTEMA] ================\n{resumos_md}\n\nUsuário: {message}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    async with aiohttp.ClientSession() as session:
        async with session.post(GEMINI_API_URL, headers=headers, json=data) as resp:
            if resp.status == 200:
                try:
                    result = await resp.json()
                    return result["candidates"][0]["content"]["parts"][0]["text"].strip()
                except Exception:
                    return "[ERRO] Resposta inesperada da IA."
            else:
                return f"[ERRO] Falha ao acessar Gemini: {resp.status}"

def remove_backticks(text: str) -> str:
    """Remove todos os caracteres de crase (`) da mensagem."""
    return text.replace("`", "")

# --- ROTEADOR PARA CHATS PRIVADOS ---
private_router = Router()
private_router.message.filter(lambda m: m.chat.type == ChatType.PRIVATE)

@atendimento_router.message(F.text)
async def group_message_handler(message: Message):
    if message.from_user.is_bot:
        return
    text = message.text.strip()
    text_lower = text.lower()
    # Ignorar comandos que começam com / exceto /yuki
    if text_lower.startswith("/") and not (text_lower.startswith("/yuki") or text_lower.startswith(f"/yuki@")):
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    is_group = str(chat_id) == str(GROUP_ID)
    me = await message.bot.get_me()
    bot_username = f"@{me.username.lower()}"

    # Remove menções do texto para o filtro de keywords
    if message.entities:
        filtered_text = text
        for entity in sorted(message.entities, key=lambda e: -e.offset):
            if entity.type == "mention":
                start = entity.offset
                end = entity.offset + entity.length
                filtered_text = filtered_text[:start] + filtered_text[end:]
        text_for_keywords = filtered_text.lower()
    else:
        text_for_keywords = text_lower

    context = await get_user_context(user_id)

    # OWNER: responde no grupo se for reply, menção, /yuki, ou keyword; no PV sempre responde
    if user_id == OWNER_ID:
        is_reply = message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.is_bot
        mentioned = message.entities and any(e.type == "mention" and bot_username in message.text for e in message.entities)
        starts_with_yuki = text_lower.startswith("/yuki") or text_lower.startswith(f"/yuki@{me.username.lower()}")
        keyword_found = any(kw in text_for_keywords for kw in keywords)
        should_respond = (is_group and (is_reply or mentioned or starts_with_yuki or keyword_found)) or not is_group
        if should_respond:
            resposta_ia = await get_gemini_response(text, "yuki_owner.md", context)
            resposta_ia = remove_backticks(resposta_ia)
            await add_to_user_context(user_id, text, resposta_ia)
            await message.reply(resposta_ia[:4096], parse_mode="Markdown", disable_web_page_preview=True)
        return

    # Usuário comum: só responde no grupo se for reply, menção, /yuki, ou keyword
    if not is_group:
        # No privado, responde gentilmente que só atende no grupo
        grupo_link = "https://t.me/crunchy_gratis"
        resposta = (
            f"Oie! Tudo bem? ૮ ˶´ ᵕˋ ˶ა\n\n"
            f"Eu sou a Yuki, assistente do grupo [Crunchyroll Grátis]({grupo_link})!\n\n"
            f"Minhas funções são todas por lá, então não consigo conversar por aqui, tá bom?\n\n"
            f"Pode me chamar lá no grupo que eu te ajudo! 🥰"
        )
        await message.reply(resposta, parse_mode="Markdown", disable_web_page_preview=True)
        return

    is_reply = message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.is_bot
    mentioned = message.entities and any(e.type == "mention" and bot_username in message.text for e in message.entities)
    starts_with_yuki = text_lower.startswith("/yuki") or text_lower.startswith(f"/yuki@{me.username.lower()}")
    keyword_found = any(kw in text_for_keywords for kw in keywords)
    should_respond = is_reply or mentioned or starts_with_yuki or keyword_found

    if should_respond:
        resposta_ia = await get_gemini_response(text, "yuki_user.md", context)
        resposta_ia = remove_backticks(resposta_ia)
        await add_to_user_context(user_id, text, resposta_ia)
        await message.reply(resposta_ia[:4096], parse_mode="Markdown", disable_web_page_preview=True)
        return
# --- HANDLERS PARA O PRIVATE ROUTER ---
@private_router.message()
async def private_handler(message: Message):
    user_id = message.from_user.id
    if user_id == int(OWNER_ID):
        # OWNER pode conversar normalmente
        context = await get_user_context(user_id)
        resposta_ia = await get_gemini_response(message.text, "yuki_owner.md", context)
        resposta_ia = remove_backticks(resposta_ia)
        await add_to_user_context(user_id, message.text, resposta_ia)
        await message.reply(resposta_ia[:4096], parse_mode="Markdown", disable_web_page_preview=True)
    else:
        grupo_link = "https://t.me/crunchy_gratis"
        resposta = (
            f"Oie! Tudo bem? ૮ ˶´ ᵕˋ ˶ა\n\n"
            f"Eu sou a Yuki, assistente do grupo [Crunchyroll Grátis]({grupo_link})!\n\n"
            f"Minhas funções são todas por lá, então não consigo conversar por aqui, tá bom?\n\n"
            f"Pode me chamar lá no grupo que eu te ajudo! 🥰"
        )
        await message.reply(resposta, parse_mode="Markdown", disable_web_page_preview=True)

