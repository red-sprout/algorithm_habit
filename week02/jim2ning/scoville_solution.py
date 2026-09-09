"""
모든 음식의 지수를 K 이상으로 만들고 싶음
스코빌 지수가 가장 낮은 2개의 음식을 
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복해서 섞는다
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없으면, -1를 리턴

정렬되는 상태가 유지 + 업데이트 계속되니 = heapq

1. heapq에 scovile을 넣고
2. 가장 작은 1,2 번째를 저장하는 값
3. 섞어서, 다시 heapq에 넣기 
4. 이걸 계속 반복할 때마다 cnt
5. 모든 값이 k 이상이어야 함. => heapq에 맨 앞에 있는 게 k보다 이상인지. => while문으로 쓰고, break 조건에 맞으면 종료하고 return
while이 끝나는 조건: 
6. heapq에 있는 게 2개 이상. <= 1개일 경우
-> 또 남은 1개가 k이상이 아닐 경우 -1 
"""

import heapq

def solution(scoville, K):
    
    answer = 0
    update_s = 0
    
    heapq.heapify(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        else:
            answer += 1
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)
    
    if scoville[0] >= K:
        return answer
    else:
        return -1
    
