from aiogram import Bot, Dispatcher, executor, types
import json

API_TOKEN = '6104892713:AAHHeqhRVvHgpwFrMXq8CYBwH9q82L2B3KA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def read_json(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data


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
        await bot.copy_message(chat_id=-1001926317748, message_thread_id=Data["topics"][title], protect_content=True, message_id=message.message_id, from_chat_id=-1001926317748)
    else:
        await bot.send_message(-1001926317748, f"Укажите в файле json номер топика для заказчика: \n{title}!!!!!!")
        return 0
    await message.delete()


if __name__ == '__main__':
    Data = read_json("Bot/db.json")
    executor.start_polling(dp, skip_updates=True)


