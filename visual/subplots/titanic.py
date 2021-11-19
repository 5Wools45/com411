import csv
import matplotlib.pyplot as plt

def read_data():
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        data = {'survived': [], 'sex': [], 'age': [], 'fare': []}
        ## add survived values to dict
        gender = ['male', 'female']
        for record in csv_reader:
            if record[1].strip() != "" and record[14] != "" and record[4].strip() != "" and record[8].strip() != "":

                data['survived'].append(record[1].strip())
                data['sex'].append(gender[int(record[14].strip())])
                data['age'].append(record[4].strip())
                data['fare'].append(round(float(record[8]), 2))
    print(data)
    return data


read_data()

