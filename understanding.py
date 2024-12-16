import speech_recognition as sr
#import os
#import sys
#import webbrowser
import win32com.client as wincl
import whisper
from difflib import SequenceMatcher
import actions

model = whisper.load_model("small")

name = "Храс"  # Name your AI!

phases = ["Смотрите на видео!", "До свидания!", "Спасибо за просмотр!", "Спасибо.", "Смотрите видео на канале!",
          "До скорого!", "Смотрите на видео.", "Смех", "Редактор субтитров А.Семкин Корректор А.Егорова.","Редактор субтитров Н.Закомолдина", "С вами был Игорь Негода."]

tasks = ["открой браузер", "открой вк", "открой лигу легенд", "напиши", "аыаыауакуа?"]

actions = [actions.openbrowser, actions.openVK, actions.openLOL, actions.other, actions.other, actions.other,
           actions.other]


def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()


def STT(audioname):
    audio = whisper.load_audio(audioname)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    options = whisper.DecodingOptions(language='Russian', fp16=False)  # language='Russian',
    result = whisper.decode(model, mel, options)
    if result.text in phases:
        pass
    else:
        print("Вы сказали: " + result.text)
        makeSomething(result.text)


def makeSomething(text):
    text = \
        text.lower().replace("!", "").replace(".", "").replace(",", "").replace("?", "") \
            .replace("(", "").replace(")", "")
    simi = []
    for task in tasks:
        '''print(text[len(name):])
        if int(similarity(text[len(name):], f" {task}")*100) in range(80, 101):
            actions[tasks.index(task)]()'''
        print(int(similarity(text[len(name):], f" {task}") * 100), "%")
        simi.append(int(similarity(text[len(name):], f" {task}") * 100))
    actions[simi.index(sorted(simi, reverse=True)[0])]() if sorted(simi, reverse=True)[0] in range(80, 101) else None


if __name__ == "__main__":
    STT("output.wav")
    print("Храс is ready to use!")
    print("Вы сказали: " + "Храс, открой браузер")
    makeSomething("Храс, открой браузер")
