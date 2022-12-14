sonlar = [32, 29, 11, 42, 66, 123, 87, 90]
juft = []
toq = []
for i in sonlar:
    if i%2==0:
        juft.append(i)
    else:
        toq.append(i)
print(f"Bular {juft} juft sonlar")
print(f"Bular  {toq} toq sonlar")