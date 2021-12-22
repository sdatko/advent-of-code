#!/usr/bin/env python3
#
# Task:
# Now that the initialization procedure is complete, you can reboot
# the reactor.
# Starting with all cubes off, run all of the reboot steps for all cubes
# in the reactor.
# Consider the following reboot steps:
#   on x=-5..47,y=-31..22,z=-19..33
#   on x=-44..5,y=-27..21,z=-14..35
#   on x=-49..-1,y=-11..42,z=-10..38
#   on x=-20..34,y=-40..6,z=-44..1
#   off x=26..39,y=40..50,z=-2..11
#   on x=-41..5,y=-41..6,z=-36..8
#   off x=-43..-33,y=-45..-28,z=7..25
#   on x=-33..15,y=-32..19,z=-34..11
#   off x=35..47,y=-46..-34,z=-11..5
#   on x=-14..36,y=-6..44,z=-16..29
#   on x=-57795..-6158,y=29564..72030,z=20435..90618
#   on x=36731..105352,y=-21140..28532,z=16094..90401
#   on x=30999..107136,y=-53464..15513,z=8553..71215
#   on x=13528..83982,y=-99403..-27377,z=-24141..23996
#   on x=-72682..-12347,y=18159..111354,z=7391..80950
#   on x=-1060..80757,y=-65301..-20884,z=-103788..-16709
#   on x=-83015..-9461,y=-72160..-8347,z=-81239..-26856
#   on x=-52752..22273,y=-49450..9096,z=54442..119054
#   on x=-29982..40483,y=-108474..-28371,z=-24328..38471
#   on x=-4958..62750,y=40422..118853,z=-7672..65583
#   on x=55694..108686,y=-43367..46958,z=-26781..48729
#   on x=-98497..-18186,y=-63569..3412,z=1232..88485
#   on x=-726..56291,y=-62629..13224,z=18033..85226
#   on x=-110886..-34664,y=-81338..-8658,z=8914..63723
#   on x=-55829..24974,y=-16897..54165,z=-121762..-28058
#   on x=-65152..-11147,y=22489..91432,z=-58782..1780
#   on x=-120100..-32970,y=-46592..27473,z=-11695..61039
#   on x=-18631..37533,y=-124565..-50804,z=-35667..28308
#   on x=-57817..18248,y=49321..117703,z=5745..55881
#   on x=14781..98692,y=-1341..70827,z=15753..70151
#   on x=-34419..55919,y=-19626..40991,z=39015..114138
#   on x=-60785..11593,y=-56135..2999,z=-95368..-26915
#   on x=-32178..58085,y=17647..101866,z=-91405..-8878
#   on x=-53655..12091,y=50097..105568,z=-75335..-4862
#   on x=-111166..-40997,y=-71714..2688,z=5609..50954
#   on x=-16602..70118,y=-98693..-44401,z=5197..76897
#   on x=16383..101554,y=4615..83635,z=-44907..18747
#   off x=-95822..-15171,y=-19987..48940,z=10804..104439
#   on x=-89813..-14614,y=16069..88491,z=-3297..45228
#   on x=41075..99376,y=-20427..49978,z=-52012..13762
#   on x=-21330..50085,y=-17944..62733,z=-112280..-30197
#   on x=-16478..35915,y=36008..118594,z=-7885..47086
#   off x=-98156..-27851,y=-49952..43171,z=-99005..-8456
#   off x=2032..69770,y=-71013..4824,z=7471..94418
#   on x=43670..120875,y=-42068..12382,z=-24787..38892
#   off x=37514..111226,y=-45862..25743,z=-16714..54663
#   off x=25699..97951,y=-30668..59918,z=-15349..69697
#   off x=-44271..17935,y=-9516..60759,z=49131..112598
#   on x=-61695..-5813,y=40978..94975,z=8655..80240
#   off x=-101086..-9439,y=-7088..67543,z=33935..83858
#   off x=18020..114017,y=-48931..32606,z=21474..89843
#   off x=-77139..10506,y=-89994..-18797,z=-80..59318
#   off x=8476..79288,y=-75520..11602,z=-96624..-24783
#   on x=-47488..-1262,y=24338..100707,z=16292..72967
#   off x=-84341..13987,y=2429..92914,z=-90671..-1318
#   off x=-37810..49457,y=-71013..-7894,z=-105357..-13188
#   off x=-27365..46395,y=31009..98017,z=15428..76570
#   off x=-70369..-16548,y=22648..78696,z=-1892..86821
#   on x=-53470..21291,y=-120233..-33476,z=-44150..38147
#   off x=-93533..-4276,y=-16170..68771,z=-104985..-24507
# After running the above reboot steps, 2758514936282235 cubes are on.
# (Just for fun, 474140 of those are also in the initialization
# procedure region.)
# Starting again with all cubes off, execute all reboot steps.
# Afterward, considering all cubes, how many cubes are on?
#
# Solution:
# The simple solution from part 1 quickly failed here due to the set growing
# rapidly. I came up with idea to keep just the information about the cuboids,
# rather than about each individual cube in the grid. The tricky part was
# to implement the difference between shapes, similar to Constructive Solid
# Geometry (CSG). In the task it is simple as we consider only rectangular
# shapes – the Rubik's cube was my inspiration here, with a Veritasium video
# about the discovery of imaginary numbers that illustrated geometric solution
# for cubic equations as a sum of cuboid volumes of various sizes [1].
# Long story short, when attempting to add a new cuboid to a set of currently
# enabled ones (switched on), we need to check if the new cuboid overlaps
# with any currently known – and if so, we subdivide the current cuboid
# to smaller parts and preserve all but the common volume, which results
# in 0 to 26 new smaller cuboids that will replace the current ones (3x3x3,
# except the 1 common – see Rubik's cube). This way we can add new volume
# (cuboid) without any duplicates (overlapping) in our space – the newly
# added cuboid will fill the skipped common volume. For turning off the cubes,
# it works really the same – the only difference is that we do not add new cube
# into the set of currently active cuboids (i.e. we will remove the common
# parts of considered cuboid [state=0] and all current ones). As the final
# answer we calculate the sum of volumes of all cuboids remaining in our set
# after all instruction steps processed.
# Illustration of slicing for a 1-axis – here the ///// is a common part:
#   min_1      min_2          max_1        max_2
#     |----------|//////////////|------------|
#             common1        common2
# When min_1 is left of common1 we shall create a shape of size from common1
# to min_1. Similarly on the right side of the common area. Here we have up
# to 3 areas, depending on min_i and max_i values. For a 3-dimensional object
# (cuboid) we have then up to 27 new shapes to consider.
# [1] https://www.youtube.com/watch?v=cUzklzVXJwo – time 8:36
#

INPUT_FILE = 'input.txt'


def overlap(cuboid1, cuboid2):
    x1_min, x1_max, y1_min, y1_max, z1_min, z1_max = cuboid1
    x2_min, x2_max, y2_min, y2_max, z2_min, z2_max = cuboid2

    if any(((x1_max < x2_min), (x2_max < x1_min),
            (y1_max < y2_min), (y2_max < y1_min),
            (z1_max < z2_min), (z2_max < z1_min))):
        return False
    else:
        return True


def subdivide_second_cuboid(cuboid1, cuboid2):
    x1_min, x1_max, y1_min, y1_max, z1_min, z1_max = cuboid1
    x2_min, x2_max, y2_min, y2_max, z2_min, z2_max = cuboid2

    nx_min = max(x1_min, x2_min)
    nx_max = min(x1_max, x2_max)
    ny_min = max(y1_min, y2_min)
    ny_max = min(y1_max, y2_max)
    nz_min = max(z1_min, z2_min)
    nz_max = min(z1_max, z2_max)

    result = []

    if x2_max > nx_max:
        x_upper = (nx_max + 1, x2_max)
    else:
        x_upper = None

    if x2_min < nx_min:
        x_lower = (x2_min, nx_min - 1)
    else:
        x_lower = None

    if y2_max > ny_max:
        y_upper = (ny_max + 1, y2_max)
    else:
        y_upper = None

    if y2_min < ny_min:
        y_lower = (y2_min, ny_min - 1)
    else:
        y_lower = None

    if z2_max > nz_max:
        z_upper = (nz_max + 1, z2_max)
    else:
        z_upper = None

    if z2_min < nz_min:
        z_lower = (z2_min, nz_min - 1)
    else:
        z_lower = None

    # 1 common cuboid that we want to drop
    # result.append((nx_min, nx_max, ny_min, ny_max, nz_min, nz_max))

    # 6 cuboids that spreads along 1-axis
    if x_upper:
        result.append((*x_upper, ny_min, ny_max, nz_min, nz_max))
    if x_lower:
        result.append((*x_lower, ny_min, ny_max, nz_min, nz_max))
    if y_upper:
        result.append((nx_min, nx_max, *y_upper, nz_min, nz_max))
    if y_lower:
        result.append((nx_min, nx_max, *y_lower, nz_min, nz_max))
    if z_upper:
        result.append((nx_min, nx_max, ny_min, ny_max, *z_upper))
    if z_lower:
        result.append((nx_min, nx_max, ny_min, ny_max, *z_lower))

    # 12 cuboids that spreads along 2-axes
    if x_upper and y_upper:
        result.append((*x_upper, *y_upper, nz_min, nz_max))
    if x_upper and y_lower:
        result.append((*x_upper, *y_lower, nz_min, nz_max))
    if x_lower and y_upper:
        result.append((*x_lower, *y_upper, nz_min, nz_max))
    if x_lower and y_lower:
        result.append((*x_lower, *y_lower, nz_min, nz_max))
    if y_upper and z_upper:
        result.append((nx_min, nx_max, *y_upper, *z_upper))
    if y_upper and z_lower:
        result.append((nx_min, nx_max, *y_upper, *z_lower))
    if y_lower and z_upper:
        result.append((nx_min, nx_max, *y_lower, *z_upper))
    if y_lower and z_lower:
        result.append((nx_min, nx_max, *y_lower, *z_lower))
    if x_upper and z_upper:
        result.append((*x_upper, ny_min, ny_max, *z_upper))
    if x_upper and z_lower:
        result.append((*x_upper, ny_min, ny_max, *z_lower))
    if x_lower and z_upper:
        result.append((*x_lower, ny_min, ny_max, *z_upper))
    if x_lower and z_lower:
        result.append((*x_lower, ny_min, ny_max, *z_lower))

    # 8 cuboids that spreads along 3-axes
    if x_upper and y_upper and z_upper:
        result.append((*x_upper, *y_upper, *z_upper))
    if x_upper and y_upper and z_lower:
        result.append((*x_upper, *y_upper, *z_lower))
    if x_upper and y_lower and z_upper:
        result.append((*x_upper, *y_lower, *z_upper))
    if x_upper and y_lower and z_lower:
        result.append((*x_upper, *y_lower, *z_lower))
    if x_lower and y_upper and z_upper:
        result.append((*x_lower, *y_upper, *z_upper))
    if x_lower and y_upper and z_lower:
        result.append((*x_lower, *y_upper, *z_lower))
    if x_lower and y_lower and z_upper:
        result.append((*x_lower, *y_lower, *z_upper))
    if x_lower and y_lower and z_lower:
        result.append((*x_lower, *y_lower, *z_lower))

    return result


def volume(cuboid):
    x_min, x_max, y_min, y_max, z_min, z_max = cuboid
    return (x_max - x_min + 1) * (y_max - y_min + 1) * (z_max - z_min + 1)


def main():
    with open(INPUT_FILE, 'r') as file:
        steps = [tuple(map(int, line.strip().split()))
                 for line in file.read().strip().replace('on', '1')
                                                .replace('off', '0')
                                                .replace('x=', '')
                                                .replace(',y=', ' ')
                                                .replace(',z=', ' ')
                                                .replace('..', ' ')
                                                .split('\n')]

    current_cuboids = set()

    for step in steps:
        state, x_min, x_max, y_min, y_max, z_min, z_max = step
        new_cuboid = (x_min, x_max, y_min, y_max, z_min, z_max)
        cuboids = set()

        if not current_cuboids:
            if state == 1:
                current_cuboids.add(new_cuboid)
            continue

        for current_cuboid in current_cuboids:
            if overlap(current_cuboid, new_cuboid):
                new_cuboids = subdivide_second_cuboid(new_cuboid,
                                                      current_cuboid)
                for cuboid in new_cuboids:
                    cuboids.add(cuboid)
            else:
                cuboids.add(current_cuboid)

        if state == 1:
            cuboids.add(new_cuboid)
        current_cuboids = cuboids

    print(sum([volume(cuboid) for cuboid in current_cuboids]))


if __name__ == '__main__':
    main()
