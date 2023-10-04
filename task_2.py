# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:07:09 2023

Напишите функцию которая на вход получает строку с гос. номером автомибиля и
выводит к какому типу относится данный гос номер, или возвращает 'Fail!',
если это не гос номер.

Упрощение: на ввод будут подаваться только Тип 1, Тип1А, Тип1Б, Тип 2, Тип 3, Тип 4
(https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5_%D0%B7%D0%BD%D0%B0%D0%BA%D0%B8_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D1%8B%D1%85_%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2_%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8#:~:text=520%C3%97112%20%D0%BC%D0%BC%20%E2%80%94%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D0%BE%D0%B9,%D0%BA%20%D1%83%D1%87%D0%B0%D1%81%D1%82%D0%B8%D1%8E%20%D0%B2%20%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D0%BE%D0%BC%20%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8)
"""


import re


plate_1a_re = re.compile(r"[авекмнорстух]\d{3}[авекмнорстух]{2} \d{2,3}")
plate_1b_re = re.compile(r"[авекмнорстух]{2}\d{3} \d{2,3}")
plate_2_re = re.compile(r"[авекмнорстух]{2}\d{4} \d{2,3}")
plate_3_re = re.compile(r"\d{4}[авекмнорстух]{2} \d{2,3}")
plate_4_re = re.compile(r"\d{4}[авекмнорстух]{2} \d{2,3}")  # ?


number = "aa111 34"


def type_car_nubmber(number):
    type_ = "Тип 1"
    return type_
