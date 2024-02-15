from itertools import combinations
from collections import defaultdict

def solution(relation):  
    attribute_num = len(relation[0])
    attribute_index = [i for i in range(attribute_num)]
    keys = []

    for key_num in range(1, attribute_num+1):
        for combi in combinations(attribute_index, key_num):
            min_flag = True
            for key in keys:
                if set(key) <= set(combi):
                    min_flag = False
                    break
            if not min_flag:
                continue
            
            filtered_relation = set()
            for tupl in relation:
                filtered_relation.add(tuple([value for i, value in enumerate(tupl) if i in combi]))
            if len(filtered_relation) == len(relation):
                keys.append(combi)
                
    return len(keys)                
    
    # combination(1~8) 해서
    # 저기서 나온 조합의 부분집합이 이미 답안에 있으면 안되고, 
    # 한 속성에서 같은 값을 가지는 튜플끼리 다른 속성을 비교해서 최소 한 튜플은 속성이 달라야 함,
    # 다른 속성을 비교하고도 거기서도 같은 값을 가지는 튜플이 있으면 또 다른 속성을 비교
    # 최종적으로 마지막 속성까지 비교했을 때는 남는 튜플이 없어야 함
    # 통과한 후보키는 답안에 추가
    
        # 한 속성값 배열을 순회하면서 같은 값을 가지는 튜플의 인덱스끼리 묶어서 배열에 넣음
        # 다음 속성값으로 넘어가서 위에서 얻은 배열 이중순회하면서 같은 값을 가지지 않는 인덱스가 있으면 배열에서 빼고, 플래그 true
        # 플래그 false면 이번 속성값은 실패, true면 다음 속성값으로 넘어가기
        # 속성값 배열을 다 순회했는데 배열에 값이 남아있으면 실패
        # 속성값 배열 다 순회하기 전에 배열에 값이 끝나도 실패
        # => 이거 아닌거 같음....
            
        # combi를 도는건 맞는거 같음.
        # 부분집합을 제거하는걸로 이미 최소성은 만족, 유일성만 판단하면 됨.
        # ->combi에 있는 모든 속성들에 대해 완전히 같은 값을 가지는 튜플이 있는지만 판단하면 됨.