#!/usr/bin/env python3


INPUT_FILENAME = "2023/3/input.txt"
IGNORE_CHARS = "0123456789."


sum_partnumbers = 0


def process_line(lines):
  global sum_partnumbers
  if lines[1] != "":
    num_str = ""
    for idx, char in enumerate(lines[1]):
      if char.isdigit():
        num_str += char
      else:
        if num_str != "":
          right_coord = idx
          left_coord = idx - len(num_str) - 1
          if left_coord < 0 : left_coord = 0
          top_coord = 0 if lines[0] != "" else 1
          bottom_coord = 2 if lines[2] != "" else 1
          is_partnumber = False
          for y in range(top_coord, bottom_coord+1):
            for x in range(left_coord, right_coord+1):
              if x >= len(lines[y]):
                pass
              elif y == 1 and x > left_coord and x < right_coord:
                pass
              else:
                print (y, x)
                if lines[y][x] not in IGNORE_CHARS:
                  is_partnumber = True
          if is_partnumber:
            sum_partnumbers += int(num_str)
            print("valid num: %s" % num_str)
          num_str = ""




with open(INPUT_FILENAME, "r") as input_file:
  lines = [""] * 3
  line_num = 0
  lines[2] = input_file.readline().strip()
  print("Line: %d" % line_num)
  while lines[2] != "":
    #print(lines)
    lines[2] += "."
    process_line(lines)
    #print()
    lines[0] = lines[1]
    lines[1] = lines[2]
    lines[2] = input_file.readline().strip()
    line_num += 1
    print("Line: %d" % line_num)
  #print(lines)
  process_line(lines)
  print("PARTNUMBERS SUM: %d" % sum_partnumbers)