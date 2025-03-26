''' [리스트1] 토익 점수 분석기
    => 1차원 리스트 2개: 토익 점수 리스트, 빈도수 리스트'''

def frequency(toeicScore):  # 각 점수대에 몇 명이 있는지 계산
    # 0~99점, 100점대, 200점대, ... 900점대
    counter = [0,0,0,0,0,0,0,0,0,0]
    # 375점: 3번방, 534점: 5번방, 975점: 9번방
    for jumsu in toeicScore:
        no = jumsu // 100
        counter[no] += 1
    return counter

def max_freq(counter):
    max = 0
    BaseJumsu = 0
    n = len(counter)
    for i in range(n):  # 총 인원수
        if max < counter[i]:
            max = counter[i]
            BaseJumsu = i * 100
    return BaseJumsu, max

toeicScore = [510, 630, 750, 580, 620, 805, 930, 650, 840, 670]
counter = frequency(toeicScore)

print("-" * 50)
print(toeicScore)
print("-" * 50)
BaseJumsu, maxCount = max_freq(counter) # 많은 점수대, 인원수
print("토익 점수 중 가장 많은 점수대 = %d점대, 인원수 = %d명" %(BaseJumsu, maxCount))