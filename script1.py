import csv

table =[]
# 3 колонки Id, номер задания(неважно), среднее время выполнения 1 МЗ
pathIn = "data85.csv"
pathOut = "data_out85.csv"

def csv_reader(path):
    check = "Id"
    count = "Count"
    sum = "sum"
    avr = "Avr"
    with open(path, "r", newline='') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if line[0]!=check:
                table.append([check, sum, count, avr])
                check = line[0]
                sum = float(line[2])
                count= 1
                avr = sum / count
            else:
                count+=1
                sum+= float(line[2])

def csv_writer(data, path2):
    with open(path2, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


csv_reader(pathIn)
csv_writer(table, pathOut)

# Что мы имеем на выходе. Крайне низкая дисперсия данных, явный артефакт (при отсекании по 80-му процентилю).
# 100% микрозадания неравноценны по сложности, что я предполагал по умолчанию. Юзеры напротив отличаются по перформансу
# несущественно. Явно работает лгоритм для усреднения сложности для каждого юзера. В таком случае справедливое вознаграждение
# будет равняться среднему в работе алгоритма. Дополнительные поправки не требуются.
# На к-80 среднее 227 секунд на МЗ, это эквивалентно 7.5N оплаты.
# На к-85 отклонения все еще слишком большие чтобы точно установить работу алгоритма.