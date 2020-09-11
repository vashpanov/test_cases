# На вход приходит большой файл (в оперативную память не влезет). Создайте новый файл, удалив в исходном повторяющиеся
# строки. Порядок строк в выходном файле не важен.

import pandas as pd

input = 'input.txt'
output = 'output.txt'
arr = []
chunker = pd.read_table(input, chunksize=1000)

for chunk in chunker:
    chunkArr = chunk.to_numpy()
    print(chunk.info(memory_usage='deep'))
    for i in range(len(chunkArr)):
        if not chunkArr[i] in arr:
            arr.append(chunkArr[i].tolist()[0])
            print(arr)
writer = open(output, "w")

def mem_usage(pandas_obj):
    if isinstance(pandas_obj,pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2
    return "{:03.2f} MB".format(usage_mb)




for i in range(len(arr)):
    writer.write(arr[i] + "\n")
writer.close()
