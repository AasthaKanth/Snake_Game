with open("data.txt",mode="r") as data:
    score=data.read()
print(score)

high_score=100

with open("data.txt",mode="w") as data:
    data.write(str(high_score))

with open("data.txt",mode="r") as data:
    score=data.read()
print(score)