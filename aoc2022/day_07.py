def determine_file_structure(data):
    """
    Given input data, outputs a dict of lists with the contained directories and files
     of the parent directory
    Files are represented only by tuples with name and file size (name: str, file_size: int)
    Directories are represented by their name only
    E.g. {"a": [("b.txt", 14848514), ("c.dat", 8504156), "d"], ...}
    """
    file_structure = {}
    current_directory = ""
    for line in data:
        if line.startswith("$"):
            if line[2:4] == "cd":
                directory = line[5:]
                if directory == "..":
                    current_directory = "/".join(current_directory.split("/")[:-1])
                else:
                    current_directory += f"/{directory}"
            elif line[2:4] == "ls":
                file_structure[current_directory] = []
        else:
            if line.startswith("dir"):
                directory = line[4:]
                file_structure[current_directory].append(current_directory + f"/{directory}")
            else:
                file_size, file_name = line.split(' ')
                file_structure[current_directory].append((file_name, int(file_size)))
    return file_structure


def determine_directory_size(directory, file_structure):
    size = 0
    for entity in file_structure[directory]:
        if isinstance(entity, str):
            size += determine_directory_size(entity, file_structure)
        else:
            size += entity[1]
    return size


def task_1(data):
    total = 0
    file_structure = determine_file_structure(data)
    for directory in file_structure:
        dir_size = determine_directory_size(directory, file_structure)
        if dir_size <= 100000:
            total += dir_size
    return total


def task_2(data):
    file_structure = determine_file_structure(data)

    used_space = determine_directory_size("//", file_structure)
    free_space = 70000000 - used_space
    space_required = 30000000 - free_space

    best_dir_size = None
    for directory in file_structure:
        dir_size = determine_directory_size(directory, file_structure)
        if dir_size < space_required:
            continue
        if not best_dir_size or dir_size < best_dir_size:
            best_dir_size = dir_size
    return best_dir_size


def main():
    with open("data/day_07.txt", "rt") as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
