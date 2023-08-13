from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot.database import models


'''===============================================CLIENT KEYBOARDS==============================================='''
#just start button
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🧨Начать🧨')

#2 various if main menu keyboard(admim/client)
main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🛒Корзина🛒').add('🎲Ассортимент🎲').add('🔧Поддержка🔧')
main_menu_admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🛒Корзина🛒').add('🎲Ассортимент🎲').add('🔧Поддержка🔧').add('Администрирование')

#back assortment inlain keyboard(if your cart is empty)
back_to_assortment_inlain_keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='🎲Ассортимент🎲', callback_data='assortment'))   

#assortment inlain keyboard
def dinamic_assortmen_keyboard():
    if len(models.get_all())!= 0:
        assortment_inlain_keyboard = InlineKeyboardMarkup(row_width=1)
        for i in range(len(models.get_all())):
            assortment_inlain_keyboard.add(InlineKeyboardButton(text=models.get_all()[i][0], callback_data=models.get_all()[i][0]))
        return assortment_inlain_keyboard.add(InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'))                                                                    
    else:
        return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'))

#product inlain keyboard(add/back)
product_inlain_menu = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Добавить в корзину', callback_data='add_to_cart'),
                                                        InlineKeyboardButton(text='Назад к ассортименту', callback_data='assortment'))

'''===============================================ADMIN KEYBOARDS==============================================='''
#admin main menu keyboard
admin_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Добавить товар').add('Редактировать товар').add('Удалить товар').add('Назад в меню')


            




