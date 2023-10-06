# -*- coding: utf-8 -*-
"""
Задача была взята из курса http://cs.mipt.ru/advanced_python/lessons/lab12.html
# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно выполнить замену, а следом
# после стрелки (--->) указан результат замены


"""

# aAc   ---> a!A!c
# aZc   ---> a!Z!c
# aZZc  ---> a!Z!!Z!c
# aBaCa ---> a!B!a!C!a
PATTERN_1 = r"([A-Z])"
REPL_1 = r"!\1!"


# abc    ---> abc
# abbc   ---> abc
# azzzc  ---> azc
# arrrrc ---> arc
# xxxxxx ---> x
PATTERN_2 = r"([a-z])\1*"
REPL_2 = r"\1"


# this is text         ---> this is text
# this is is text      ---> this *is* text
# this is is is text   ---> this *is* text
# this is text text    ---> this is *text*
# this is is text text ---> this *is* *text*
PATTERN_3 = r"(?<=[ ^])([a-z]+)( \1)+"
REPL_3 = r"*\1*"

# one two three ---> two one three
# dog cat wolf  ---> cat dog wolf
# goose car rat ---> goose rat car
PATTERN_4 = r"\b(\w{3}) (\w{3})\b"
REPL_4 = r"\2 \1"
