#!/usr/bin/env python3
#
# --- Day 7: No Space Left On Device / Part Two ---
#
# Now, you're ready to choose a directory to delete.
#
# The total disk space available to the filesystem is 70000000. To run
# the update, you need unused space of at least 30000000. You need to find
# a directory you can delete that will free up enough space to run the update.
#
# In the example above, the total size of the outermost directory (and thus
# the total amount of used space) is 48381165; this means that the size of
# the unused space must currently be 21618835, which isn't quite the 30000000
# required by the update. Therefore, the update still requires a directory
# with total size of at least 8381165 to be deleted before it can run.
#
# To achieve this, you have the following options:
# – Delete directory e, which would increase unused space by 584.
# – Delete directory a, which would increase unused space by 94853.
# – Delete directory d, which would increase unused space by 24933642.
# – Delete directory /, which would increase unused space by 48381165.
#
# Directories e and a are both too small; deleting them would not free up
# enough space. However, directories d and / are both big enough! Between
# these, choose the smallest: d, increasing unused space by 24933642.
#
# Find the smallest directory that, if deleted, would free up enough space on
# the filesystem to run the update. What is the total size of that directory?
#
#
# --- Solution ---
#
# The difference here is that we need to find the size of directory which
# removed would give us enough of free space in the filesystem. The current
# usage is the size of directory / calculated during previous part.
# Then we process the sorted list of discovered sizes and check whether each
# size, together with current free space, adds to the value bigger or equal
# to the one we need. As an answer, we print the smallest size that satisfies
# the condition.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        commands = [command.strip().split('\n')
                    for command in file.read().strip().split('$')
                    if command]  # skip empty elements (e.g. before first $)

    cwd = '/'
    full_space = 70000000
    needed_space = 30000000
    files = {}

    for command in commands:
        stdin = command[0]
        stdout = command[1:]

        cmd = stdin.strip().split()

        if cmd[0] == 'cd':
            if cmd[1].startswith('/'):
                cwd = cmd[1]
            elif cmd[1] == '..':
                cwd = '/'.join(cwd.split('/')[:-1])
                if not cwd:
                    cwd = '/'
            else:
                cwd = f'{cwd}/{cmd[1]}'.replace('//', '/')

        elif cmd[0] == 'ls':
            for line in stdout:
                size, file = line.split()

                if size == 'dir':
                    pass  # Nothing to do here...

                else:
                    path = f'{cwd}/{file}'.replace('//', '/')
                    files[path] = int(size)

        else:
            print('Unsupported command: ', cmd)
            exit(1)

    dirs = {}

    for path, size in files.items():
        subdirs = path.split('/')[:-1]

        for i in range(1, len(subdirs) + 1):
            subpath = '/'.join(subdirs[:i])
            if not subpath:
                subpath = '/'

            if subpath not in dirs:
                dirs[subpath] = 0
            dirs[subpath] += int(size)

    sizes = sorted([size for size in dirs.values()])
    used_space = max(sizes)  # same as dirs['/']

    free_space = full_space - used_space

    for size in sizes:
        if free_space + size >= needed_space:
            break

    print(size)


if __name__ == '__main__':
    main()
