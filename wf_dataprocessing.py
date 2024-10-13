import pandas as pd
import csv

#This will contain the code associated with data munging.
#Executing it will generate a set of processed data les.

__author__ = "Carlos Rodriguez"
__date__ = "10/15/24"
__assignment = "SER494: Project Munging"

def process_chicken(data):
    list = []
    count = 0
    chicken = data.iloc[9:20, 1:]
    for index, row in chicken.iterrows():
        for col in chicken.columns:
            if pd.isna(row[col]):
                value = -10
            else:
                value = row[col]
            count += 1
            list.append(value)
            #print(f"Value: {value}")
            #print(count)
    return list
    pass


def process_electricity(data):
    list = []
    count = 0
    electricity = data.iloc[9:20, 1:]
    for index, row in electricity.iterrows():
        for col in electricity.columns:
            if pd.isna(row[col]):
                value = -10
            else:
                value = row[col]
            count += 1
            list.append(value)
            #print(f"Value: {value}")
            #print(count)
    return list
    pass


def process_gasoline(data):
    list = []
    count = 0
    gasoline = data.iloc[9:20, 1:]
    for index, row in gasoline.iterrows():
        for col in gasoline.columns:
            if pd.isna(row[col]):
                value = -10
            else:
                value = row[col]
            count += 1
            list.append(value)
            #print(f"Value: {value}")
            #print(count)
    return list
    pass


def process_inflation(data):
    list = []
    count = 0
    inflation = data.iloc[11:23,1:-2]
    for index, row in inflation.iterrows():
        for col in inflation.columns:
            if pd.isna(row[col]):
                value = -10
            else:
                value = row[col]
            count +=1
            list.append(value)
            #print(f"Value: {value}")
            #print(count)
    return list
    pass

def process_confindence(input_filename):
    list = [-10,-10,-10,-10,-10,-10,-10,-10]
    with open(input_filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) > 1:
                if (row[1] != "OECD"):
                    list.append(float(row[1]))

    if(len(list) != 132):
        num = 132-len(list)
        for i in range(num):
            list.append(-10)
    return list
    pass


if __name__ == '__main__':

    new_df = pd.DataFrame()

    data0 = pd.read_excel('data_original/chicken-report.xlsx')
    list0 = process_chicken(data0)

    data1 = pd.read_excel('data_original/electricity-report.xlsx')
    list1 = process_electricity(data1)

    data2 = pd.read_excel('data_original/gasoline-report.xlsx')
    list2 = process_gasoline(data2)

    data3 = pd.read_excel('data_original/inflation-report.xlsx')
    list3 = process_inflation(data3)

    data4 = "data_original/confidence-report.csv"
    list4 = process_confindence(data4)

    date_list = (pd.date_range(start='2014-01-01', end='2024-12-31', freq='ME')).tolist()
    new_df = pd.DataFrame({
        'dates': date_list,
        'chicken': list0,
        'electricity': list1,
        'gasoline': list2,
        'inflation': list3,
        'confidence': list4
    })
    file = "data_processed/all.csv"
    new_df.to_csv(file, index=False)
