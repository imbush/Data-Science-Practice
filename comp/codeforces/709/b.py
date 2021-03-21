t = int(input())
output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    incr = True
    unable = False
    m_found = False
    c_found = False
    mc_diff_found = False
    for i in range(1, len(a)):
        if m_found:
            if a[i] >= m:
                unable = True
                break
            if a[i] < a[i-1]:
                if a[i] != a[i-1] - m + c:
                    unable = True
                    break
                incr = False
        elif c_found:
            if a[i] >= a[i-1]:
                if c != a[i] - a[i-1]:
                    unable = True
                    break
            else:
                incr = False
                m_found = True
                m = a[i-1] - a[i] + c
                if m <= max(a):
                    unable = True
                    break
        elif mc_diff_found:
            if a[i] >= a[i-1]:
                c_found = True
                m_found = True
                c = a[i] - a[i-1]
                m = c + mc_diff
                if m <= max(a):
                    unable = True
                    break
            else:
                incr = False
                if a[i-1] - a[i] != mc_diff:
                    unable = True
                    break
        else:
            if a[i] >= a[i-1]:
                c_found = True
                c = a[i] - a[i-1]
            else:
                incr = False
                mc_diff_found = True
                mc_diff = a[i-1] - a[i]

    if unable:
        output.append([-1])
    elif incr:
        output.append([0])
    elif m_found:
        output.append([m, c])
    else:
        output.append([0])
for out in output:
    print(*out)
