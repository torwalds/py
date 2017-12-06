import csv

i = 0

dbvalues = []
database = "c:\\files\\project_master\\log.csv"

with open(database) as db:
    ejectdata = csv.reader(db)
    header = next(ejectdata)
    for row in ejectdata:
        try:
            dbvalues.append(row[1])
            i = i + 1
        except IndexError:
            break
print(dbvalues)