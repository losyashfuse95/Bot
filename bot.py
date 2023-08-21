from aiogram import Bot, Dispatcher, executor, types
import json
import telebot
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
Telebot = telebot.TeleBot(API_TOKEN)

def read_json(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json(path, data):
        with open(path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

@dp.message_handler()
async def forward(message: types.Message):
    test = message.text
    parts = test.split(" ")
    if len(parts) >= 2:
        smiley = parts[0].strip()
        title = parts[1].strip()
    else:
        await bot.send_message(-1001926317748, "Ошибка при парсинге!!!!!")
        return 0
    if title in Data["topics"]:
        await bot.copy_message(chat_id=-1001926317748, message_thread_id=Data["topics"][title], message_id=message.message_id, from_chat_id=message.chat.id)
    else:
        temp = Telebot.create_forum_topic(chat_id=-1001926317748, name=title)
        Data["topics"][title] = temp.message_thread_id
        write_json("Bot/db.json",Data)
        await bot.copy_message(chat_id=-1001926317748, message_thread_id=Data["topics"][title], message_id=message.message_id, from_chat_id=message.chat.id)
    #await message.delete()


if __name__ == '__main__':
    Data = read_json("Bot/db.json")
    executor.start_polling(dp, skip_updates=True)
    


