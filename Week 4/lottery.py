def fast_count_segments(ranges, points):
    cnt = [0] * len(points)
    
    vec = []
    point_to_counts = {}
    
    for start, end in ranges:
        vec.append((start, 0))
        vec.append((end, 2))
    
    for i in points:
        vec.append((i, 1))
    
    vec.sort(key=lambda x: (x[0], x[1]))
    
    count = 0
    
    for i in vec:
        if i[1] == 0:
            count += 1
        elif i[1] == 2:
            count -= 1
        else:
            point_to_counts[i[0]] = count
    
    for i in range(len(points)):
        cnt[i] = point_to_counts[points[i]]
    
    return cnt

if __name__ == "__main__":
    n, m = map(int, input().split())
    ranges = []
    
    for _ in range(n):
        start, end = map(int, input().split())
        if start <= end:
            ranges.append((start, end))
    
    points = list(map(int, input().split()))
    
    cnt1 = fast_count_segments(ranges, points)
    
    for val in cnt1:
        print(val, end=" ")
