"""
날짜 : 2021.08.15
학습 : SWEA D4
제목 : 5432 쇠막대기 자르기
문제 :
여러 개의 쇠막대기를 레이저로 절단하려고 한다.
효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.
쇠막대기와 레이저의 배치는 다음 조건을 만족한다.
 - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
 - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
 - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
 - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
아래 그림은 위 조건을 만족하는 예를 보여준다.
수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향이다.

이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.
1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 “()” 으로 표현된다. 또한, 모든 “()”는 반드시 레이저를 표현한다.
2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현된다.

위 예의 괄호 표현은 그림 위에 주어져 있다.
쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고,
이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.
쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.
2   //전체 TC 개수
()(((()())(())()))(())  //첫 번째 TC
(((()(()()))(())()))(()())	//두 번째 TC

[출력]
각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 잘려진 조각의 총 개수를 출력한다.
#1 17   //첫 번째 TC의 출력
#2 24	//두 번째 TC의 출력

"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    N = int(input()) #노선 갯수
    empty_lst = [[0] * 5001 for _ in range(N)] #5천개의 정류장 노선 수 만큼

    for n in range(N):
        route_start, route_end = map(int, input().split()) # n번 노선 정류장 처음과 끝

        for i in range(route_start, route_end+1):
            empty_lst[n][i] += 1 #n번 노선 다니는 정류장을 1로 바꾸기

    cp_stop = int(input()) #비교 할 노선 갯수
    result = [] #최종 값 저장
    # cnt_stop = [0] * 5001  # n번 노선이 cp_stop을 지나면 카운트 할 리스트 이거 여기있으면 초기화 안되서 중복 값이 들어가면 지랄남

    for stop in range(cp_stop): #cp_stop 만큼 no_stop input 받아오기
        cnt_stop = [0] * 5001  # n번 노선이 cp_stop을 지나면 카운트 할 리스트
        no_stop = int(input()) #비교 할 노선 번호

        for i in range(N): #노선 번호 가지고 오기
            if empty_lst[i][no_stop] == 1: #i번 노선에 no_stop이 지나가면
                cnt_stop[no_stop] += 1 # cnt_stop에 카운트

        result += [cnt_stop[no_stop]] #12개 중 5개 맞음.. 왜 ???

    # for i in range(5001): #0 제외 하고 result에 넣기 #0개 맞음 no_stop이 노선 안에 안지나가면 0 출력 해야함
    #     if cnt_stop[i] != 0:
    #         result += [cnt_stop[i]]

    print('#{}'.format(tc), end=' ')
    print(*result)


