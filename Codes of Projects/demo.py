def extract():
    file = open("OOP_Homework.py", "r")
    lst = file.readlines()
    for ls in lst:
        for i in range(1,36):
            if ls.startswith("from") or ls.startswith("import"):
                with open(f"OOP_Folder\\Question {i}.py", "a") as file2:
                    file2.write(str(ls))
    file_name = 0
    for i in lst:
        digit = i
        if i[3:5].isdigit():
            file_name = i[2:5]
            digit = i
        elif i[3:4].isdigit():
            file_name = i[2:4]
            digit = i
        elif i[2:3].isdigit():
            file_name = i[2:3]
            digit = i
        if file_name:
            with open(f"OOP_Folder\\Question {file_name}.py", "a") as fil1:  
                fil1.write(str(digit))
                
                
