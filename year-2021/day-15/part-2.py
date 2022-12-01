#!/usr/bin/env python3
#
# --- Day 15: Chiton / Part Two ---
#
# Now that you know how to find low-risk paths in the cave, you can try
# to find your way out.
#
# The entire cave is actually five times larger in both dimensions than you
# thought; the area you originally scanned is just one tile in a 5x5 tile area
# that forms the full map. Your original map tile repeats to the right and
# downward; each time the tile repeats to the right or downward, all of its
# risk levels are 1 higher than the tile immediately up or left of it.
# However, risk levels above 9 wrap back around to 1. So, if your original map
# had some position with a risk level of 8, then that same position on each of
# the 25 total tiles would be as follows:
#   8 9 1 2 3
#   9 1 2 3 4
#   1 2 3 4 5
#   2 3 4 5 6
#   3 4 5 6 7
#
# Each single digit above corresponds to the example position with a value of
# 8 on the top-left tile. Because the full map is actually five times larger
# in both dimensions, that position appears a total of 25 times, once in each
# duplicated tile, with the values shown above.
#
# Here is the full five-times-as-large version of the first example above,
# with the original map in the top left corner highlighted:
#   1163751742.2274862853338597396444961841755517295286
#   1381373672.2492484783351359589446246169155735727126
#   2136511328.3247622439435873354154698446526571955763
#   3694931569.4715142671582625378269373648937148475914
#   7463417111.8574528222968563933317967414442817852555
#   1319128137.2421239248353234135946434524615754563572
#   1359912421.2461123532357223464346833457545794456865
#   3125421639.4236532741534764385264587549637569865174
#   1293138521.2314249632342535174345364628545647573965
#   2311944581.3422155692453326671356443778246755488935
#   22748628533385973964449618417555172952866628316397
#   24924847833513595894462461691557357271266846838237
#   32476224394358733541546984465265719557637682166874
#   47151426715826253782693736489371484759148259586125
#   85745282229685639333179674144428178525553928963666
#   24212392483532341359464345246157545635726865674683
#   24611235323572234643468334575457944568656815567976
#   42365327415347643852645875496375698651748671976285
#   23142496323425351743453646285456475739656758684176
#   34221556924533266713564437782467554889357866599146
#   33859739644496184175551729528666283163977739427418
#   35135958944624616915573572712668468382377957949348
#   43587335415469844652657195576376821668748793277985
#   58262537826937364893714847591482595861259361697236
#   96856393331796741444281785255539289636664139174777
#   35323413594643452461575456357268656746837976785794
#   35722346434683345754579445686568155679767926678187
#   53476438526458754963756986517486719762859782187396
#   34253517434536462854564757396567586841767869795287
#   45332667135644377824675548893578665991468977611257
#   44961841755517295286662831639777394274188841538529
#   46246169155735727126684683823779579493488168151459
#   54698446526571955763768216687487932779859814388196
#   69373648937148475914825958612593616972361472718347
#   17967414442817852555392896366641391747775241285888
#   46434524615754563572686567468379767857948187896815
#   46833457545794456865681556797679266781878137789298
#   64587549637569865174867197628597821873961893298417
#   45364628545647573965675868417678697952878971816398
#   56443778246755488935786659914689776112579188722368
#   55172952866628316397773942741888415385299952649631
#   57357271266846838237795794934881681514599279262561
#   65719557637682166874879327798598143881961925499217
#   71484759148259586125936169723614727183472583829458
#   28178525553928963666413917477752412858886352396999
#   57545635726865674683797678579481878968159298917926
#   57944568656815567976792667818781377892989248891319
#   75698651748671976285978218739618932984172914319528
#   56475739656758684176786979528789718163989182927419
#   67554889357866599146897761125791887223681299833479
#
# Equipped with the full map, you can now find a path from the top left corner
# to the bottom right corner with the lowest total risk:
#   .1.1637517422274862853338597396444961841755517295286
#   .1.3813736722492484783351359589446246169155735727126
#   .2.1365113283247622439435873354154698446526571955763
#   .3.6949315694715142671582625378269373648937148475914
#   .7.4634171118574528222968563933317967414442817852555
#   .1.3191281372421239248353234135946434524615754563572
#   .1.3599124212461123532357223464346833457545794456865
#   .3.1254216394236532741534764385264587549637569865174
#   .1.2931385212314249632342535174345364628545647573965
#   .2.3119445813422155692453326671356443778246755488935
#   .2.2748628533385973964449618417555172952866628316397
#   .2.4924847833513595894462461691557357271266846838237
#   .324.76224394358733541546984465265719557637682166874
#   47.15.1426715826253782693736489371484759148259586125
#   857.4.5282229685639333179674144428178525553928963666
#   242.1.2392483532341359464345246157545635726865674683
#   246.1123532.3572234643468334575457944568656815567976
#   423653274.1.5347643852645875496375698651748671976285
#   231424963.2342.5351743453646285456475739656758684176
#   342215569245.332.66713564437782467554889357866599146
#   33859739644496.1.84175551729528666283163977739427418
#   35135958944624.61.6915573572712668468382377957949348
#   435873354154698.44.652657195576376821668748793277985
#   5826253782693736.4.893714847591482595861259361697236
#   9685639333179674.1.444281785255539289636664139174777
#   3532341359464345.2461.575456357268656746837976785794
#   3572234643468334575.4.579445686568155679767926678187
#   5347643852645875496.3.756986517486719762859782187396
#   3425351743453646285.4564.757396567586841767869795287
#   4533266713564437782467.554.8893578665991468977611257
#   449618417555172952866628.3163.9777394274188841538529
#   462461691557357271266846838.2.3779579493488168151459
#   546984465265719557637682166.8.7487932779859814388196
#   693736489371484759148259586.125.93616972361472718347
#   17967414442817852555392896366.6413.91747775241285888
#   46434524615754563572686567468379.7.67857948187896815
#   46833457545794456865681556797679.26.6781878137789298
#   645875496375698651748671976285978.21.873961893298417
#   4536462854564757396567586841767869.7.952878971816398
#   5644377824675548893578665991468977.6112.579188722368
#   5517295286662831639777394274188841538.5.299952649631
#   5735727126684683823779579493488168151.4.599279262561
#   6571955763768216687487932779859814388.1.961925499217
#   7148475914825958612593616972361472718.34725.83829458
#   28178525553928963666413917477752412858886.3.52396999
#   57545635726865674683797678579481878968159.2.98917926
#   57944568656815567976792667818781377892989.24.8891319
#   756986517486719762859782187396189329841729.1431.9528
#   564757396567586841767869795287897181639891829.2.7419
#   675548893578665991468977611257918872236812998.33479.
#
# The total risk of this path is 315 (the starting position is still never
# entered, so its risk is not counted).
#
# Using the full map, what is the lowest total risk of any path from
# the top left to the bottom right?
#
#
# --- Solution ---
#
# The biggest difference in this part was to implement the data alignment
# in a bigger grid. For such case, the originally prepared algorithm turned
# out to be non-effective, giving result in roughly about 104 minutes.
# Experimentally I found that the implementation of a finding vertex for
# current minimum distance was the bottleneck. Optimizing that part by
# introducing heap reduced the computation time to less than a second.
# Then I discovered that original implementation could be optimized and
# after introducing changes it gave result in about 11 seconds.
# Code below is using a heap implementation of my own – it is a bit slower
# than dedicated Python heapq module, but sufficient enough for my goals
# and my code can still remain import-free (which is my personal challenge).
#

INPUT_FILE = 'input.txt'


def heapify(array, index=0):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < len(array) and array[left] < array[smallest]:
        smallest = left

    if right < len(array) and array[right] < array[smallest]:
        smallest = right

    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        heapify(array, smallest)


def heap_pop(array):
    root = array[0]
    array[0] = array[len(array) - 1]
    array.pop()
    heapify(array)
    return root


def heap_push(array, element):
    array.append(element)
    index = len(array) - 1
    parent = (index - 1) // 2

    while index != 0 and array[parent] > array[index]:
        array[index], array[parent] = array[parent], array[index]
        index = parent
        parent = (index - 1) // 2


def wrap(x):
    return (x % 10) + (x // 10)


def main():
    grid = [list(map(int, list(characters)))
            for line in open(INPUT_FILE, 'r')
            for characters in line.strip().split()]

    times_bigger = 5
    bigger_grid = []

    for times_y in range(times_bigger):
        for row in grid:
            new_row = []
            for times_x in range(times_bigger):
                new_row.extend(
                    [wrap(x + times_y + times_x) for x in row]
                )
            bigger_grid.append(new_row)

    grid = bigger_grid

    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    goal = (cols - 1, rows - 1)

    risk_level = sum(grid[0]) + sum(grid[:][-1])  # upper bound

    dist = [[risk_level for x in range(cols)] for y in range(rows)]
    prev = [[None for x in range(cols)] for y in range(rows)]

    dist[start[1]][start[0]] = 0
    Q = [(dist[start[1]][start[0]], start)]

    while Q:
        shortest, (sx, sy) = heap_pop(Q)

        if (sx, sy) == goal:
            break

        for (nx, ny) in ((sx - 1, sy), (sx + 1, sy),
                         (sx, sy - 1), (sx, sy + 1)):
            if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
                continue

            alt = shortest + grid[ny][nx]
            if alt < dist[ny][nx]:
                dist[ny][nx] = alt
                prev[ny][nx] = (sx, sy)
                heap_push(Q, (alt, (nx, ny)))

    risk_level = dist[goal[1]][goal[0]]

    print(risk_level)


if __name__ == '__main__':
    main()