import re


def task_number_1():
    with open("task1-en.txt", "r") as f:
        text_1 = f.read()

    word_pattern = r'\b[a-zA-Z]{6}\b|\b[a-zA-Z]{8}\b'
    number_pattern = r'-?\d+\.\d+|-?\d+'
    numbers = re.findall(number_pattern, text_1)
    words = re.findall(word_pattern, text_1)
    print(*numbers)
    print(*words)


def task_number_2():
    with open("task2.html", "r", encoding='utf-8') as f:
        text_2 = f.read()

    pattern_content = r'content\s*=\s*"([^"]*)"'
    link_content = re.findall(pattern_content, text_2)
    print(*link_content)


def task_number_3():
    with open("task3.txt", "r") as f:
        text_3 = f.read()

    pattern_id = 
    pattern_second_name = 
    pattern_mail = 
    pattern_date = 
    pattern_website = 
    

#task_number_1()
#task_number_2()
task_number_3()