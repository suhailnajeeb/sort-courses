import pandas as pd
from getCourse import courseDict
import numpy as np

filepaths = ['Class_Routine_Fall_19.xlsx', 'Class_Routine_Fall_2017.xlsx', 'Class_Routine_Fall_2018.xlsx', 'Class_Routine_Spring_2018.xlsx', 'Class_Routine_Spring_2019.xlsx', 'Class_Routine_Spring_2020.xlsx', 'Class_Routine_Summer_2017.xlsx', 'Class_Routine_Summer_2018.xlsx', 'Class_Routine_Summer_2019.xlsx']

for filepath in filepaths:
    df = pd.read_excel(filepath)
    courses = df['Course'].values
    courseCodes = []
    courseNames = []
    for course in courses:
        if(len(course) <= 6):
            if('ETE' in course):
                courseCodes.append(course)
                courseNames.append(courseDict[course])
    df = pd.DataFrame(courseNames, courseCodes)
    df.to_csv('export\\'+ filepath[:-5] + '.csv', header = False)
