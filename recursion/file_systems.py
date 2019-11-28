import os


def disk_usage(path):
    total = os.path.getsize()

    if os.path.isdir(path):
        for f in os.listdir(path):
            full_path = os.path.join(path, f)
            total += disk_usage(full_path)

    print("{0:<7}".format(total), path)

    return total
