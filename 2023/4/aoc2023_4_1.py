#!/usr/bin/env python3


INPUT_FILENAME = "2023/4/input.txt"


points = 0
with open(INPUT_FILENAME, "r") as input_file:
  for line in input_file.readlines():
    line_points = 0
    card, nums = line.split(":")
    winning_nums, our_nums = nums.split("|")
    winning_nums = [int(n.strip()) for n in winning_nums.strip().split(" ") if n.strip() != ""]
    our_nums = [int(n.strip()) for n in our_nums.strip().split(" ") if n.strip() != ""]
    for num in our_nums:
      if num in winning_nums:
        if line_points == 0:
          line_points = 1
        else:
          line_points *= 2
    points += line_points
print("POINTS: %d" % points)
