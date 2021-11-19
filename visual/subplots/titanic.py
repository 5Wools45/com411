import csv
import matplotlib.pyplot as plt

def read_data():
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        data = {'survived': [], 'sex': [], 'age': [], 'fare': []}
        ## add survived values to dict
        for record in csv_reader:
            if record[1] is None:
                pass
            elif record[1] == 0:
                pass
            else:
                data['survived'].append(record[1])
        ## add sex to values in dict
        for record in csv_reader:
            if record[15] is None:
                pass
            elif record[15] == 0:
                data['sex'].append('male')
            else:
                data['sex'].append('female')
        ## add age to values in dict
        for record in csv_reader:
            if record[4] is None:
                pass
            else:
                data['age'].append(record[4])
        ## add fare as a float to values in dict
        for record in csv_reader:
            if record[8] is None:
                pass
            else:
                data['fare'].append(round(record[8], 2))
        print(data)
        return data


read_data()

