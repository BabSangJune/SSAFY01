"""
날짜 : 2021.08.27
학습 : SWEA D3
제목 : 2805. 농작물 수확하기
문제 :
N X N크기의 농장이 있다.
이 농장에는 이상한 규칙이 있다.
규칙은 다음과 같다.
   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)

   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.

1 X 1크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.
3 X 3크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16 (3 + 2 + 5 + 4 + 2)이다.
5 X 5크기의 농장에서 자라는 농작물의 수확하여 얻을 수 있는 수익은 25 (3 + 2 + 1 + 1 + 2 + 5 + 1 + 1 + 3 + 3 + 2 + 1)이다.
농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.

[제약 사항]
농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)
농작물의 가치는 0~5이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

"""
import sys
sys.stdin = open("2805.txt", 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]

    mid = N // 2
    cnt = 0
    for i in range(0, mid):
        for j in range(mid - i, mid + i + 1):
            cnt += int(arr[i][j])

    for i in range(N):
        cnt += int(arr[mid][i])

    curr = 0
    for i in range(N-1, mid, -1):

        for j in range(mid - curr, mid + curr + 1):
            cnt += int(arr[i][j])

        curr += 1


    # curr = 0
    # for i in range(mid+1, N):
    #     curr +=1
    #     for j in range(0+curr, N-curr):
    #         cnt += int(arr[i][j])

    print('#{} {}'.format(tc, cnt))
