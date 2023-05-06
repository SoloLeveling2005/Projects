import editdistance

str1 = "удали цель"
str2 = "удали мою цель"

distance = editdistance.eval(str1, str2)
print(distance)