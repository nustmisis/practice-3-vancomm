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
REGEXP_1 = ''   # регулярное выражение


# abc    ---> abc
# abbc   ---> abc
# azzzc  ---> azc
# arrrrc ---> arc
# xxxxxx ---> x
REGEXP_2 = '' 


# this is text         ---> this is text
# this is is text      ---> this *is* text
# this is is is text   ---> this *is* text
# this is text text    ---> this is *text*
# this is is text text ---> this *is* *text*
REGEXP_3 = '' 

# one two three ---> two one three
# dog cat wolf  ---> cat dog wolf
# goose car rat ---> goose rat car
REGEXP_4 = '' 


# cat dog                     ---> cat dog
# cat dog cat                 ---> cat dog cat
# dog cat dog cat cat         ---> dog dog
# dog cat dog rat rat cat cat ---> dog dog rat rat
REGEXP_5 = '' 
