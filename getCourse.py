import pandas as pd
import csv

indexFile = 'courseCodes.txt'

codes = ['ETE101', 'ETE103', 'ETE105', 'ETE107', 'ETE207', 'ETE212', 'ETE214', 'ETE216', 'ETE219', 'ETE282', 'ETE302', 'ETE310', 'ETE311', 'ETE312', 'ETE314', 'ETE316', 'ETE322', 'ETE350', 'ETE399', 'ETE401', 'ETE403', 'ETE420', 'ETE430', 'ETE441', 'ETE442', 'ETE444', 'ETE450', 'ETE452', 'ETE456', 'ETE461', 'ETE463', 'ETE465', 'ETE470', 'ETE472', 'ETE475']
courses = []

df = pd.read_csv(indexFile, delimiter = '\t', header = None)
for course in df.values:
    courses.append(course[0][8:])

courseDict = dict(zip(codes, courses))
