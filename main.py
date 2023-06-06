import telebot
from telebot import types

bot = telebot.TeleBot('6165670918:AAHtHBPX-q46JOfC85BwjgcTxR0r-PpXpmQ')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Olá!, {message.from_user.first_name}!\nVocê pode encontrar respostas para suas perguntas usando os comandos listados no menu suspenso à esquerda do campo de mensagem de entrada.',disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['website'])
def website(message):
    bot.send_message(message.chat.id, '⛓ <b>Ecossistemas C-Patex</b> <a href="https://c-patex.com/pt">Website</a>\nPara mais informações, consulte o <a href="https://t.me/cpatexportuguese/4396"><b>F.A.Q</b></a>  👈',disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['withdrawal'])
def withdrawal(message):
    bot.send_message(message.chat.id, '💰 <b>Todas as retiradas</b> são processadas em até 3 horas. Se o seu saque estiver atrasado, entre em contato com o suporte ( detalhes no comando /contact )\nPara mais informações, consulte o <a href="https://t.me/cpatexportuguese/4396"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['fees'])
def fees(message):
    bot.send_message(message.chat.id, '💲 Uma lista detalhada de comissões pode ser encontrada <a href="https://c-patex.com/pt/fees">aqui</a>.\n Para mais informações, consulte o <a href="https://t.me/cpatexportuguese/4396"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['kyc'])
def kyc(message):
    bot.send_message(message.chat.id, '👤 O tempo máximo para verificações é de ~24 horas. Normalmente, porém, os aplicativos são processados muito mais rapidamente.\nPara mais informações, consulte o <a href="https://t.me/cpatexportuguese/4396"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['deposit'])
def deposit(message):  bot.send_message(message.chat.id, '🪙 If your deposit has <b>not been credited</b>, please provide us with detailed transaction details <b> (AMOUNT, VALUE, HASH) </b> to email: 📬 support@c-patex.com\nPara mais informações, consulte o <a href="https://t.me/cpatexportuguese/4396"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['contact'])
def contact(message):   bot.send_message(message.chat.id, 'Você pode nos contatar por e-mail - 📬 support@c-patex.com\n🌐 Crie um ticket de suporte no <a href="https://c-patex.com/pt">Website</a>\n📱 Ou entre em contato com um agente de suporte no <a href="https://t.me/cpatexportuguese">Telegram</a>', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['two_factor_auth'])
def two_factor_auth(message):
    bot.send_message(message.chat.id, '👤 Para desabilitar o 2FA, forneça os dois lados do seu documento (passaporte, carteira de identidade ou carteira de motorista) e 🤳 uma selfie sua segurando o documento e um pedaço de papel com o seguinte texto manuscrito "C-PATEX.COM", data atual e sua assinatura.\nPor favor, envie todas as fotos para nós em support@c-patex.com.\nPara mais informações, consulte o <a href="https://t.me/cpatexportuguese/4396"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['docs'])
def docs(message):
    bot.send_message(message.chat.id, '📝 Link para o <a href="https://c-patex.com/files/pt/wp.pdf?v=1.2"><b>whitepaper</b></a>\n🔩 Link para <a href="https://patex.io/docs/Patex%20Tokenomics.pdf"><b>tokenomics</b></a>', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['socials'])
def socials(message):   bot.send_message(message.chat.id, '📜 <a href="https://linktr.ee/patex_ecosystem"><b>Linktr.ee</b></a>\n \
— <a href="https://www.facebook.com/patexecosystem"><b>Facebook</b></a>\n \
— <a href="https://www.instagram.com/patex_ecosystem/"><b>Instagram</b></a> \n \
— <a href="https://www.youtube.com/channel/UCLmHyM6kZ5bViyh7my6ZkpA"><b>YouTube</b></a> \n \
— <a href="https://medium.com/@patex_ecosystem"><b>Medium</b></a> \n \
— <a href="https://twitter.com/patex_ecosystem"><b>Twitter</b></a> \n \
       \n \
📝<a href="https://linktr.ee/patex_ecosystem"><b>Patex Chats</b></a>\n \
— <a href="https://t.me/cpatexeng"><b>TG Channel (English)</b></a> \n \
— <a href="https://t.me/cpatexexchange"><b>TG Channel (Español / Portuguese)</b></a> \n \
— <a href="https://t.me/cpatexespanol"><b>TG Chat (Español)</b></a> \n \
— <a href="https://t.me/cpatexportuguese"><b>TG Chat (Portuguese)</b></a> \n \
— <a href="https://t.me/+HmW0DJAYl1YzMjAy"><b>TG Chat (English)</b></a> \n \
— <a href="https://t.me/cpatexcis"><b>TG Chat (CIS)</b></a>', disable_web_page_preview=True, parse_mode='HTML')

bot.polling(none_stop=True, interval=1)