"""
players ["mumu", "soe", "poe", "kai", "mine"]
callings ["kai", "kai", "mine", "mine"]
1. mumu soe kai poe mine
2. mumu kai soe poe mine
3. mumu kai soe mine poe
4. mumu kai mine soe poe
result ["mumu", "kai", "mine", "soe", "poe"]

dic = {1: "mumu",
2: "soe",
3: "poe" -> "kai"
4: "kai" -> "poe"
5: "mine"}

'이름을 key로 하는 것, 순위를 key로 하는 dic이 둘 다 필요함 => 둘 다 관리해 주면 됩니다.'

** 사고과정
일단 calling을 봤어. 백만이야. call 하나당 O[1] 정도로 처리해야겠다.
어떻게든, O[N]이 안 되도록 만들어야겠다.
1번. calling에서 이름이 있으면 그 이름을 기준으로 몇 등인지를 찾아야 해. => 그래야 그 전에 있던 것도 찾을 수 있으니까
이걸 해결하기 위한 자료구조로, dic을 선택함.
** dic 기준으로 봤을 때, 이름을 기준으로 몇 등인지를 찾아야 하므로, key를 이름으로 - value는 등수. (기준 = key)

2번. 그 앞에 있는 등수도 알아야 함.
** 등수를 기준으로 사람이 누군지를 찾아야 하므로, key를 등수로 value를 이름으로.

각 자료구조의 시간복잡도는 알고 있어야 한다. <<

for call in calling:
  call에 해당하는 key 값을 바꿔 준다
  ""call의 key 값을 -1한 애""  => 저장하고
  key를 새로 추가하거나, 삭제하거나만 가능하다

players : n, calling: m 이라면
n + m => / n x m 은 왜아니잉??? => calling이 한번 수행될 때마다 dic이 새로 만들어져야 함
dic 만들어 O(N) => 다 끝난 다음, calling에 대한 수행 O(M) = O(N+M)
"""

def solution(players, callings):
    
    p_to_n = {
    n_to_p = {}
    result = []
    
    for i in range(len(players)):
        player = players[i]
        p_to_n[player] = i
        n_to_p[i] = player
        
        # for player in players: 대신, player = players[i]로 접근해야 함

    for call in callings:
        call_n = p_to_n[call] #순위
        p_call_n = call_n - 1 #전 순위
        p_call_p = n_to_p[p_call_n] #전 순위 선수 이름
        
        p_to_n[call] = p_call_n #person이 key인: 
        n_to_p[call_n] = p_call_p
        p_to_n[p_call_p] = call_n
        n_to_p[p_call_n] = call
        
    for i in sorted(n_to_p):
        # 정렬은 5만 로그 5만 => 로그는 사실 정말 약간 극한까지 밀어붙어도 웬만하면 20을 넘진 않음 5만 x 20 하면? 100만 < 충분?
        # i에는 1,2,3,4로 key 값이 들어감
        result.append(n_to_p[i])
    
    return result
