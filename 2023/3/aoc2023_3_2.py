#!/usr/bin/env python3


INPUT_FILENAME = "2023/3/input.txt"


lines_nums = []
lines_stars = []


def process_line(line):
    line_nums = []
    line_stars = []
    num_str = ""
    for idx, char in enumerate(line):
      if char.isdigit():
        num_str += char
      else:
        if num_str != "":
          line_nums.append((idx-len(num_str), idx-1, int(num_str)))
          num_str = ""
        if char == "*":
          line_stars.append(idx)
    lines_nums.append(line_nums)
    lines_stars.append(line_stars)


def gen_neighbours(x, line_len, y, num_lines):
  left    = x - 1 if x > 0 else x
  right   = x + 1 if x < line_len-1 else x
  top     = y - 1 if y > 0 else y
  bottom  = y + 1 if y < num_lines-1 else y
  neighbours = []
  for i in range(top, bottom+1):
    for j in range (left, right+1):
      if not (j == x and i == y):
        neighbours.append((j, i))
  return neighbours



line_len = 0
with open(INPUT_FILENAME, "r") as input_file:
  for line in input_file.readlines():
    line = line.strip()
    line_len = len(line)
    process_line(line + ".")

sum_gears = 0
num_lines = len(lines_stars)
for y, line in enumerate(lines_stars):
  for star in line:
    neighbours = gen_neighbours(star, line_len, y, num_lines)
    #print(neighbours)
    num_neighbours = []
    for neighbour_x, neighbour_y in neighbours:
      for idx, num_neighbour in enumerate(lines_nums[neighbour_y]):
        num_start, num_end, num = num_neighbour
        if neighbour_x in range(num_start, num_end+1) and num_neighbour not in num_neighbours:
          num_neighbours.append(num_neighbour)
    print(num_neighbours)
    if len (num_neighbours) == 2:
      sum_gears += num_neighbours[0][2] * num_neighbours[1][2]
print ("GEARS SUM: %d" % sum_gears)
