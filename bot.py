from aiogram import Bot, Dispatcher, executor, types
import json
from config import API_TOKEN, dst_chat_id, src_chat_id
exit(0)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def read_json(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data
def write_json(path, data):
        with open(path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


@dp.message_handler()
async def forward(message: types.Message):
    if message.chat.id != src_chat_id: return 
    test = message.text
    parts = test.split(" ")
    if len(parts) >= 2:
        smiley = parts[0].strip()
        title = parts[1].strip()
    else:
        await bot.send_message(dst_chat_id, "Ошибка при парсинге!!!!!")
        return 0
    
    if title not in Data["topics"]:
        temp = await bot.create_forum_topic(chat_id=dst_chat_id, name=title)
        Data["topics"][title] = temp.message_thread_id
        write_json("Bot/db.json",Data)
    
    await bot.copy_message(chat_id=dst_chat_id, message_thread_id=Data["topics"][title], message_id=message.message_id, from_chat_id=src_chat_id)
    await message.delete()


if __name__ == '__main__':
    Data = read_json("Bot/db.json")
    executor.start_polling(dp, skip_updates=True)
    


