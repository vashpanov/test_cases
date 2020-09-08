# Напишите функцию, сериализующую бинарное дерево в JSON.

# Предположим что дерево пришло в виде обычной двоичной кучи такой формат удобен для быстрого встраивания элементов и
# хранения заполненных деревьев. Неудобен при большом размере и большом числе пустых ячеек. Я использую похожий формат
# в своем текущем проекте, но по причине того что такое построение позволяет дерево не хранить, а калькулировать походу.

import math
import json
inp = ["0","1","1","2","2","2","2","3","3","3","3","3","3","3","3"]
depth = int(math.log2(len(inp)) + 1)

def TreeInToJSON(input):
    input.insert(0, "start")
    if len(input)< 2**depth-1:
        for i in range((2**depth-1)-len(input)):
            input.append('')
    return json.dumps(rec(1))

def rec(node):
    if inp[node] == '':
        return
    if node > (depth - 1) ** 2 - 2:
        return inp[node]
    return {inp[node]: [rec(2 * node), rec(2 * node + 1)]}

print(TreeInToJSON(inp))
