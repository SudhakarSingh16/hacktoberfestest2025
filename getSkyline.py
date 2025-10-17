def getSkyline(build):
    points = []

   
    for b in build:
        points.append(b[0])
        points.append(b[1])

  
    points.sort()

    res = []
    prev = 0

   
    for x in points:
        maxH = 0

       
        for b in build:
            l, r, h = b
            if l <= x < r:
                maxH = max(maxH, h)

        if not res or maxH != prev:
            res.append((x, maxH))
            prev = maxH

    return res

if __name__ == '__main__':
    build = [
        [2, 9, 10],
        [3, 6, 15],
        [5, 12, 12]
    ]

    skyline = getSkyline(build)

    for p in skyline:
        print(f'({p[0]}, {p[1]}) ', end='')

    print()
