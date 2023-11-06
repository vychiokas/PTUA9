def ips_between(start, end):
    start = start.split(".")[::-1]
    end = end.split(".")[::-1]

    ips = 0
    level = 0
    full_range = 256
    for start_number, end_number in zip(start, end):
        if start_number != end_number:
            ips += (int(end_number) - int(start_number)) * full_range** level
        level += 1
    return ips

print(ips_between("87.182.66.227", "87.182.79.39"))
