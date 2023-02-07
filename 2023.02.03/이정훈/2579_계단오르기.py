N = int(input().strip())
stairs = []
for i in range(N):
    stairs.append(int(input().strip()))
best_record = [0] * N

for i in range(N):
    if i == 0:
        best_record[i] = stairs[0]
    elif i == 1:
        best_record[i] = stairs[0] + stairs[1]
    elif i == 2:
        best_record[i] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    else:
        P1 = best_record[i - 3] + stairs[i - 1] + stairs[i]  #바로 전에서 왔으니까 그 전에 점프함
        P2 = best = best_record[i - 2] + stairs[i] #점프했으니까 그 전의 행적은 don't care
        if P1 > P2 :
            best_record[i] = P1

        else:
            best_record[i] = P2

        best_record[i] = best

print(best_record[-1])
