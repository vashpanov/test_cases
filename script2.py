import csv

table =[]
# 3 колонки: Id юзера, Id документа, успех/не успех
pathIn = "data_task3.csv"
pathOut = "data_task32.csv"

def csv_reader(path):
    check = "Id"
    count = "Correct"
    countAll = "Attempts"
    with open(path, "r", newline='') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if line[0]!=check:
                table.append([check, count, countAll])
                check = line[0]
                count = 0
                countAll= 1
                if line[2]=='1':
                    count=count+1
            else:
                countAll+=1
                if line[2]=='1':
                    count=count+1

def csv_writer(data, path2):
    with open(path2, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


csv_reader(pathIn)
csv_writer(table, pathOut)