# На вход приходит большой файл (в оперативную память не влезет). Создайте новый файл, удалив в исходном повторяющиеся
# строки. Порядок строк в выходном файле не важен.

import pandas as pd

input = 'input.txt'
output = 'output.txt'
arr=[]
chunker = pd.read_table(input, chunksize=10000)

for chunk in chunker:
    chunkArr=chunk.to_numpy()
    for i in range(len(chunkArr)):
        if not chunkArr[i] in arr:
            arr.append(chunkArr[i].tolist()[0])
            print(arr)
writer = open(output, "w")

for i in range(len(arr)):
    writer.write(arr[i]+"\n")
writer.close()