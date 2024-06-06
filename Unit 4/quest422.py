def parse_ranges(ranges_string):
    generator = (n.split('-') for n in ranges_string.split(','))
    range_generator = (num for start, stop in generator for num in range(int(start), int(stop) + 1))
    return range_generator


print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
