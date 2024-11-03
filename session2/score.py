id = [1, 2, 3, 4, 5, 6, 7, 8, 9]
name = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isaac"]
score = [3, 7.87, 9.001, 11, 13, 8, 9, 9.2, 8.86]
status = [""] * len(score)

for i in range(len(id)):
    if score[i] < 9:
        score[i] = 9
        status[i] = "faill"
    else:
        status[i] = "passed"

for i in range(len(id)):
    print(f"Name: {name[i]}     Score: {score[i]}    Status: {status[i]}")
