def solution(arr):
    
    result = []
    for i in arr:
        if not result: 
            result.append(i)
            continue
        elif result and result[-1] != i:
            result.append(i)
    
    return result