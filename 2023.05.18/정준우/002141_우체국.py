from sys import stdin


마을의_수 = int(stdin.readline())
마을 = []
전체_인구_수 = 0

for _ in range(마을의_수):
    마을_위치, 인구_수 = map(int, stdin.readline().split())
    마을.append((마을_위치, 인구_수))
    전체_인구_수 += 인구_수

# 정렬 기준은 마을 위치
마을.sort()

# 마을을 모두 오른쪽에 둔 상태로 우체국 놓아보며 시작
우체국_기준_왼쪽_인구 = 0
우체국_기준_오른쪽_인구 = 전체_인구_수 - 마을[0][1]

# 초기값
우체국_놓아볼_위치 = 0
적절한_우체국_위치 = 0
인구_차이 = 우체국_기준_오른쪽_인구 - 우체국_기준_왼쪽_인구

# 우체국을 한 칸씩 오른쪽으로 이동시켜보며 인구 차이 탐색
while 우체국_놓아볼_위치 < 마을의_수 - 1:
    우체국_기준_왼쪽_인구 += 마을[우체국_놓아볼_위치][1]
    우체국_놓아볼_위치 += 1
    우체국_기준_오른쪽_인구 -= 마을[우체국_놓아볼_위치][1]

    # 우체국까지 와야 할 사람이 양쪽 다 적으면 더 적절한 위치?
    if abs(우체국_기준_오른쪽_인구 - 우체국_기준_왼쪽_인구) < 인구_차이:
        적절한_우체국_위치 = 우체국_놓아볼_위치
        인구_차이 = abs(우체국_기준_오른쪽_인구 - 우체국_기준_왼쪽_인구)

print(마을[적절한_우체국_위치][0])
