#!/usr/bin/env python3
#
# --- Day 9: Disk Fragmenter / Part Two ---
#
# Upon completion, two things immediately become clear. First, the disk
# definitely has a lot more contiguous free space, just like the amphipod
# hoped. Second, the computer is running much more slowly! Maybe introducing
# all of that file system fragmentation was a bad idea?
#
# The eager amphipod already has a new plan: rather than move individual
# blocks, he'd like to try compacting the files on his disk by moving whole
# files instead.
#
# This time, attempt to move whole files to the leftmost span of free space
# blocks that could fit the file. Attempt to move each file exactly once
# in order of decreasing file ID number starting with the file with
# the highest file ID number. If there is no span of free space to the left
# of a file that is large enough to fit the file, the file does not move.
#
# The first example from above now proceeds differently:
#
#   00...111...2...333.44.5555.6666.777.888899
#   0099.111...2...333.44.5555.6666.777.8888..
#   0099.1117772...333.44.5555.6666.....8888..
#   0099.111777244.333....5555.6666.....8888..
#   00992111777.44.333....5555.6666.....8888..
#
# The process of updating the filesystem checksum is the same;
# now, this example's checksum would be 2858.
#
# Start over, now compacting the amphipod's hard drive using this
# new method instead. What is the resulting filesystem checksum?
#
#
# --- Solution ---
#
# The difference in this part is that now we move files from the end of a disk
# only when they can be kept in some hole without causing data fragmentation.
# For this, in a loop we iterate on files from the end of disk map: for each
# file we browse the holes from the disk's beginning and if we can find a hole
# that is at least the size of the file, then we relocate that file to a new
# position. This requires 7 operations in scenario, where for convenience
# we keep separate lists of files and holes (based on diskmap).
#
#                     +---------+
#   block ID    0   1 | 2   3   4   5  ...
#   file_index  0   1 v 2   3   4   5  ...
#   hole_index    0   1 ^ 2   3 | 4   5  ...
#                       +-------+
#
# To relocate file index J, to hole with index K:
# – pop the file from index J,
# – insert the file at index K + 1,
# – remove (pop) the hole with index J,
# – add length of the moved file (F) to the hole with index J - 1,
# – expand a hole with index J - 1 by the size of a moved file from index J,
# – update a hole at index K to be zero (Z),
# – create a new hole at index K + 1 to contain a remaining space of hole K.
#
#   block ID    0   1   4   2   3       5  ...
#   file_index  0   1   2   3   4       5  ...
#   hole_index    0   1   ?   2   3+F+4   5  ...
#      comment       (Z) New      Merge
#
# Such algorithm completes after a couple of seconds, however it could be
# optimized with additional condition – by introducing the starting index
# during holes search. As the beginning of disk map will become tightly-packed,
# in the list of holes we will quickly observe a lot of elements of length 0,
# that can be skipped during the browsing. Additionally, this allows us
# to finish early, as we can identify when the processed file (as next one
# from the end of the disk) is already in the area of tightly-packed data
# – we do not want to move the file to a later position in the disk,
# so in such case we finish the processing.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        diskmap = tuple(map(int, file.read().strip()))

    files = list(enumerate(diskmap[0::2]))  # (ID, length)
    holes = list(diskmap[1::2])  # length

    if len(holes) < len(files):
        holes.append(0)

    start_index = 0

    for file in reversed(files.copy()):
        _, length = file
        file_index = files.index(file)

        if file_index < start_index:  # nothing else can be moved!
            break

        for hole_index, hole in enumerate(holes[start_index:], start_index):
            if hole_index >= file_index:  # no point in moving the file
                break

            if hole < length:  # not enough space to move the file
                continue

            # relocate the file
            file = files.pop(file_index)
            files.insert(hole_index + 1, file)

            # update the holes map – merge the holes where the file was
            after = holes.pop(file_index)
            holes[file_index - 1] += length
            holes[file_index - 1] += after

            # update the holes map – nothing before and remaining space after
            holes[hole_index] = 0
            holes.insert(hole_index + 1, hole - length)

            break  # file was moved, proceed immediately to next file

        # skip tightly-packed files (all first holes of length zero)
        for hole_index, hole in enumerate(holes[start_index:], start_index):
            if hole == 0:
                start_index = hole_index
            else:
                break

    diskmap_v2 = []

    for file, hole in zip(files, holes):
        diskmap_v2.append(file)

        if hole:  # skip holes of length zero
            diskmap_v2.append((None, hole))  # (ID, length)

    checksum = 0
    address = 0

    for entry in diskmap_v2:
        ID, length = entry

        if ID is not None:
            checksum += ID * int(length * (address + address + length - 1) / 2)

        address += length

    print(checksum)


if __name__ == '__main__':
    main()
