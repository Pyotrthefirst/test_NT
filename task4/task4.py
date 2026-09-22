import sys

data_file=sys.argv[1]
data=[]
with open(data_file, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(int(line.strip()))
data.sort()
closest_in_data = data[len(data) // 2]
moves_sum=0
for x in data:
    moves_sum=moves_sum+abs(x-closest_in_data)
if moves_sum<=20:
    print(moves_sum)
else:
    print('20 ходов недостаточно для приведения всех элементов массива к одному числу')