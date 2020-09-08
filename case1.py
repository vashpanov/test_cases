# Напишите функцию, которая принимает на вход строку и переставляет в ней слова в обратном порядке: например, «мама мыла
# раму» превращает в «раму мыла мама».

inp = "мама мыла раму"

def reverseList (str):
    arr = str.split(" ")
    reverseList= " ".join(list(reversed(arr)))
    return reverseList

reverseList(inp)