from telegram import InlineQueryResultArticle, InputTextMessageContent
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler


zodiacs = {'овен': 'Сегодня день для решительных действий! Вас ждёт успех.',
            'телец': 'Проведите день спокойно, подумайте о будущем. Хороший день для планирования.',
            'близнецы': 'Будьте осторожны с новыми знакомыми, не все они искренни.',
            'рак': 'Сегодня удачный день для улучшения отношений с близкими.',
            'лев': 'Постарайтесь избежать конфликтов на работе, они могут затянуться.',
            'дева': 'Сегодня удачный день для финансовых вложений и покупок.',
            'весы': 'Возможно, вам придется принять важное решение, доверьтесь интуиции.',
            'скорпион': 'Не бойтесь рисковать сегодня, это принесет свои плоды.',
            'стрелец': 'Сегодня отличный день для путешествий и новых впечатлений.',
            'козерог': 'Уделите внимание здоровью, не перегружайте себя на работе.',
            'водолей': 'Вы найдете решение проблемы, которая давно вас беспокоит.',
            'рыбы': 'Сегодня вас ждет приятный сюрприз от близкого человека.'}


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет! Я могу предсказать твою судьбу по знаку зодиака. Напиши свой знак!")


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Напиши свой знай зодиака, и я дам тебе предсказание!")


def zodiac_prediction(update, context):
    text = update.message.text.lower() 
    zodiac = zodiacs.get(text)
    if zodiac:
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Твоё предсказание для {text}: {zodiac}")   
    else:
        text = ",".join(zodiacs.keys())
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Не могу понять ваш знак зодиака, выберите знак из представленных: {text}")


def main():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    prediction_handler = MessageHandler(Filters.text & (~Filters.command), zodiac_prediction)
    dispatcher.add_handler(prediction_handler)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()


if __name__ == "__main__":
    main()
