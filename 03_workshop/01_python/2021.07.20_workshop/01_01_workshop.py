"""
날짜 : 2021.07.20
학습 : SSAFY 01_02_workshop
제목 : 간단한 N의 약수 (SWEA #1933)
문제 :
입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램
을 작성하시오.

입력 : 10
출력 : 1 2 5 10
"""
N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')


"""
[제약 사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
[입력]
입력으로 정수 N이 주어진다.
[출력]
정수 N의 모든 약수를 오름차순으로 출력한다.
[입력 예시]
10
[출력 예시]
1 2 5 10
"""