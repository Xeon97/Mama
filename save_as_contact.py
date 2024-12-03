
from telethon import events
from telethon.tl.functions.contacts import AddContactRequest

# Название модуля
MODULE_NAME = "SaveAsContact"
COMMAND = "%nikcn"

@bot.on(events.NewMessage(pattern=f"^{COMMAND} (.+)$"))
async def save_as_contact(event):
    # Проверка, является ли сообщение ответом
    if not event.is_reply:
        await event.reply("Пожалуйста, ответьте на сообщение пользователя, которого хотите сохранить в контакты.")
        return

    # Получаем имя из команды
    new_name = event.pattern_match.group(1)

    # Получаем ID пользователя из ответа
    reply_message = await event.get_reply_message()
    user = await event.client.get_entity(reply_message.sender_id)

    try:
        # Добавляем пользователя в контакты
        await event.client(AddContactRequest(
            id=user.id,
            first_name=new_name,
            last_name="",
            phone="",
            add_phone_privacy_exception=False
        ))
        await event.reply(f"Пользователь {new_name} успешно добавлен в контакты.")
    except Exception as e:
        await event.reply(f"Не удалось добавить пользователя в контакты: {e}")

# Регистрация модуля
def __init__(hikka):
    hikka.register_module(MODULE_NAME, "Модуль для сохранения контактов через команду.")
