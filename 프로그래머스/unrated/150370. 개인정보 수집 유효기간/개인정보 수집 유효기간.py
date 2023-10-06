def solution(today, terms, privacies):
    answer = []
    dictTerm = {}
    y,m,d = today.split(".")
    y = int(y)
    m = int(m)
    d = int(d)
    
    for i, term in enumerate(terms):
        termType, duration = term.split(" ")
        dictTerm[termType] = int(duration)
        
    for i, pri in enumerate(privacies):
        start, termType = pri.split(" ")
        endY, endM, endD = plusMonth(start, int(dictTerm[termType]))
        print(endY, endM, endD)
        if endY < y or (endY==y and endM < m) or (endY==y and endM==m and endD<d):
            answer.append(i+1)
        
    return answer

def plusMonth(start, plusMonth):
    year, month, day = start.split(".")
    year = int(year)
    month = int(month)
    day = int(day)
    tempMonth = month + plusMonth
    
    if day == 1:
        day = 28
        tempMonth = tempMonth - 1
    else:
        day = day -1
        
    if tempMonth > 12 and tempMonth % 12 != 0:
        year = year + tempMonth // 12
        month = tempMonth % 12
    elif tempMonth > 12 and tempMonth %12 == 0:
        month = 12
        year = year + tempMonth // 12 - 1
    else:
        month = tempMonth if tempMonth != 0 else month
        
        
    return [year, month, day]
        
    