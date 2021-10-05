import logging
import telegram
from telegram import *
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
  menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

def start(update: Update, context: CallbackContext):
  print(update.message.chat.first_name)
  menu_list = ['Join Us']
  button_list = []
  for each in menu_list:
     button_list.append(InlineKeyboardButton(each, callback_data = each))
  reply_markup=InlineKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows
  update.message.reply_text(text='Welcome to CascAid',reply_markup=reply_markup)

def menu_callback(update: Update, context: CallbackContext):
    if update.callback_query.data == 'Join Us':
      contact_keyboard = telegram.KeyboardButton(text="Click here to send your Phone number",request_contact=True)
      reply_markup = telegram.ReplyKeyboardMarkup([[ contact_keyboard ]])
      update.callback_query.answer()
      update.callback_query.message.reply_text("Send Your Phone Number to Let us connect to you. ", reply_markup=reply_markup)    
      

def get_contact(update: Update, context: CallbackContext):
    login_url = LoginUrl(url=f"https://www.gautham.games/register/?org=RR&chat_id={update.message.chat.id}&phone_number={update.message.contact.phone_number}",bot_username='my_566bot',request_write_access=True)
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Signup',login_url=login_url)]])
    update.message.reply_text(text='Click below ',reply_markup=reply_markup)

###########
from time import sleep
def tes(update: Update, context: CallbackContext):
  print(update.message.chat.first_name)
  name = list('Hello, '+update.message.chat.first_name)
  msg = name[0]
  update.message.reply_text(msg)
  for letter in name[1:]:
    msg += letter
    if letter==' ':
      continue
    context.bot.editMessageText(chat_id=update.message.chat_id,
                                message_id=str(int(update.message.message_id)+1), 
                                text=msg)

def test(update: Update, context: CallbackContext):
  #update.message.reply_text(text='<a href="tg://settings/chat_settings">Chat settings</a>',parse_mode='HTML')
  update.message.reply_text(text='<a href="skype:LOGIN?call">Call on the skype user</a>',parse_mode='html')

def main()->None:
    updater = Updater("TelegramAPI_key",use_context=True)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.contact, get_contact))
    dispatcher.add_handler(CallbackQueryHandler(menu_callback))
    #########
    #dispatcher.add_handler(CommandHandler('start', test))
    

    updater.start_polling()
    updater.idle()

main()
