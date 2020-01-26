import pandas as pd

filepaths = ['Class_Routine_Fall_19.xlsx', 'Class_Routine_Fall_2017.xlsx', 'Class_Routine_Fall_2018.xlsx', 'Class_Routine_Spring_2018.xlsx', 'Class_Routine_Spring_2019.xlsx', 'Class_Routine_Spring_2020.xlsx', 'Class_Routine_Summer_2017.xlsx', 'Class_Routine_Summer_2018.xlsx', 'Class_Routine_Summer_2019.xlsx']

init = True
import numpy as np

for filepath in filepaths:
    df = pd.read_excel(filepath)
    if (init):
        courses = df['Course'].values
        init = False
    else:
        course = df['Course'].values
        courses = np.hstack((courses, course))
        del course

courses = np.unique(courses)
courseCodes = []

for course in courses:
    if(len(course) <= 6):
        if('ETE' in course):
            courseCodes.append(course)
            print(course)

#courseCodes = ['ETE101', 'ETE103', 'ETE105', 'ETE107', 'ETE207', 'ETE212', 'ETE214', 'ETE216', 'ETE219', 'ETE282', 'ETE302', 'ETE310', 'ETE311', 'ETE312', 'ETE314', 'ETE316', 'ETE322', 'ETE350', 'ETE399', 'ETE401', 'ETE403', 'ETE420', 'ETE430', 'ETE441', 'ETE442', 'ETE444', 'ETE450', 'ETE452', 'ETE456', 'ETE461', 'ETE463', 'ETE465', 'ETE470', 'ETE472', 'ETE475']
