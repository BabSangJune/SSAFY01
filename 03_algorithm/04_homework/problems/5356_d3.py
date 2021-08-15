"""
날짜 : 2021.08.15
학습 : SWEA D4
제목 : 5356 .의석이의 세로로 말해요
문제 :
아직 글을 모르는 의석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.
이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 의석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.
다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다. 아래에 의석이가 칠판에 붙여 만든 단어들의 예가 있다.

A A B C D D
a f z z
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x

만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.

심심해진 의석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.
세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다.
이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.
위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.
그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다.
위에서 의석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:

Aa0aPAf985Bz1EhCz2W3D1gkD6x

칠판에 붙여진 단어들이 주어질 때, 의석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스는 총 다섯 줄로 이루어져 있다.
각 줄에는 길이가 1이상 15이하인 문자열이 주어진다. 각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.
2 //tc수
ABCDE //tc1
abcde
01234
FGHIJ
fghij
AABCDD //tc2
afzz
09121
a8EWg6
P5h3kx
[출력]
각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 의석이가 세로로 읽은 순서대로 글자들을 출력한다.
#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x
"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    empty_lst = [] #빈 리스트
    for i in range(5):
        word_lst = list(input())
        empty_lst += [word_lst] #empty_list에 [word_list] 넣어서 2차원으로 만들기

    result_list = []  # 값 저장 할 빈 리스트
    for j in range(15): #열 값 최고 15개까지
        for i in range(len(empty_lst)): #empty_list에서 가로로 하나씩 가지고 오기
            try:
                result_list.append(empty_lst[i][j])
            except:
                pass
            

    print('#{}'.format(tc), end=' ')
    print(''.join(result_list))
