"""
Project 5: Generate the fictional student dataset.

Run:
    python create_dataset.py
"""

import csv

columns = ['Student ID', 'Department', 'Level', 'Attendance Percentage', 'Average Examination Score']
students = [['24/15591', 'Biochemistry', 400, 79, 70], ['24/14273', 'Mathematics', 200, 81, 88], ['24/15140', 'Criminology', 300, 92, 92], ['24/13722', 'Public Health Science', 400, 95, 96], ['24/13487', 'Broadcasting', 100, 76, 94], ['24/13227', 'Architecture', 300, 98, 86], ['24/15495', 'Law', 200, 84, 82], ['24/15334', 'Human Anatomy', 200, 96, 83], ['24/14628', 'Industrial chemistry', 400, 91, 59], ['24/15782', 'Data Science', 200, 66, 91], ['24/13639', 'Microbiology', 100, 97, 85], ['24/15336', 'Software Engineering', 100, 87, 79], ['24/15874', 'Nursing', 200, 71, 80], ['24/15269', 'Mass communication', 400, 85, 62], ['24/13138', 'Human Physiology', 300, 89, 89], ['24/13207', 'Political Science', 100, 93, 68], ['24/14905', 'Accounting', 100, 68, 75], ['24/14350', 'Psychology', 300, 90, 64], ['24/13676', 'Cyber Security', 400, 74, 77], ['24/14366', 'Computer Science', 300, 88, 73]]

with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(students)

print(f"Created student_dataset.csv with {len(students)} fictional student records.")
