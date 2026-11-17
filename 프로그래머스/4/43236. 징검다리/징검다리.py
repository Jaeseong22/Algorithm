def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    right = distance
    left = 1
    answer = 0
    
    while right >= left:
        mid = (right+left) // 2
        
        previous = 0
        cnt = 0
        for rock in rocks:
            if rock - previous < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                previous = rock
        if cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
        
    return answer