# [Gold IV] 뱀 - 3190 

[문제 링크](https://www.acmicpc.net/problem/3190) 

### 성능 요약

메모리: 34208 KB, 시간: 84 ms

### 분류

자료 구조(data_structures), 덱(deque), 구현(implementation), 큐(queue), 시뮬레이션(simulation)

### 문제 설명

<p> 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.</p>

<p>게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.</p>

<p>뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.</p>

<ul>
	<li>먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.</li>
	<li>만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.</li>
	<li>만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.</li>
</ul>

<p>사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.</p>

### 입력 

 <p>첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)</p>

<p>다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.</p>

<p>다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)</p>

<p>다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.</p>

### 출력 

 <p>첫째 줄에 게임이 몇 초에 끝나는지 출력한다.</p>

---

### Solution
```python
# 0,0 에서 처음에는 오른쪽을 향한다. L 왼쪽, O 오른쪽

import sys
input = sys.stdin.readline
from collections import deque

# 뱀 함수, 수빈이 코드 보고 알았는데 뱀은 snake였음 ;
def baam(x, y, idx):
    global second
    # 시작 값 큐에 넣기
    queue = deque([(x, y)])
    arr[x][y] = 2
    
    # 계속 돌린다.
    while True:
        second += 1
        x = x + d[idx][0]
        y = y + d[idx][1]

        if 0 <= x < N and 0 <= y < N:
	    # 이동한 자리가 사과면 사과자리를 뱀의 머리로 바꾸고 큐에 추가
            if arr[x][y] == 1:
                arr[x][y] = 2
                queue.append((x, y))
                
		# 지금 시간과 move리스트의 이동과 같은 시간이 있다면 방향 꺾어주기
                for i in move:
                    if i[0] == second:
                        if i[1] == 'L':
                            idx = (idx - 1) % 4
                            break
                        else:
                            idx = (idx + 1) % 4
                            break
	    
	    # 이동한 자리가 비었다면
            elif arr[x][y] == 0:
	    	# 이동한 자리 뱀의 머리로 바꾸고
                arr[x][y] = 2
                queue.append((x,y))
		# queue의 첫 값을 빼서 arr 꼬리 자리를 빈자리로 만들기
                tail_x, tail_y = queue.popleft()
                arr[tail_x][tail_y] = 0
		
		# 마찬가지로 시간이 같다면 방향 꺾어주기
                for i in move:
                    if i[0] == second:
                        if i[1] == 'L':
                            idx = (idx - 1) % 4
                            break
                        else:
                            idx = (idx + 1) % 4
                            break
	    # 사과도 빈자리도 아니라면 그냥 종료
            else: break
	    
	# x,y가 맵을 벗어나면 종료
        else: break        
	
 # main
# 시작은 초기 값인 오른쪽으로
d = [(0,1), (1,0), (0,-1), (-1,0)] # 우 하 좌 상
    
N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]

# 사과 위치 생성
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

# 이동
L = int(input())

move = []
second = 0

# 초와 방향을 함께 리스트에 넣어준다
for _ in range(L):
    sec, drec = input().split()
    move.append([int(sec), drec])

# 시작 위치와 idx
baam(0,0,0)

print(second)
