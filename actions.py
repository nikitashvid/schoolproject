import webbrowser
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

def openbrowser():
    url = 'https://www.google.ru/'
    webbrowser.open(url)
    print("Task complited.")


def openVK():
    url = 'https://vk.com/feed'
    webbrowser.open(url)
    print("Task complited.")


def openLOL():
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Riot Games\\League of Legends")
    print("Task complited.")


def other():
    print("Task complited111.")

def writereeky(mess):
    Token = 'vk1.a.5jssnbqEZwjQq1HFTwgOzKkPwJdYJ-c7ew87rwzpPAEXo8Ej--xvAMgkLZnCGMwzV_bEOaeclKi8x-2P4qzT4jeB9FERI7F0GTGXkRRCD5zlJo5g4hCL4b8HqJ95JdquRTAADBho5F_q3Hqi5uTCNNhgJsFSigOpZve4iAKd_nEgGX8ZjRHVlJPNRUsxH9jn7GcRNKwXsQTHe9Ur7aCv7A'
    user_id = 588061506
    random_id = random.randint(0, 588061505)
    vk_session = vk_api.VkApi(token=Token)
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    vk.messages.send(user_id=user_id, random_id=random_id, message=mess)
    user = vk.users.get(user_id=user_id)
    print(f"Отправка '{mess}' пользователю {user[0]['first_name'] + ' ' + user[0]['last_name']}")

if __name__ == "__main__":
    writereeky("hi")
