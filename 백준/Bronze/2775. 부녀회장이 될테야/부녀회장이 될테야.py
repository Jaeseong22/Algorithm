def solution():
    t = int(input())  # 테스트 케이스 개수 입력
    results = []  # 결과를 저장할 리스트

    for _ in range(t):  
        k = int(input())  # 층 수
        n = int(input())  # 호 수

        x = [i for i in range(1, n+1)]  # 0층의 인원 수 초기화

        for _ in range(k):  # k층까지 계산
            for j in range(1, n):  
                x[j] += x[j-1]  # 현재 호실은 왼쪽 호실 + 이전 층 값

        results.append(x[-1])  # 결과 리스트에 추가

    # 입력을 모두 받은 후 한 번에 출력
    for result in results:
        print(result)

solution()