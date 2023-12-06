#!/usr/bin/env python3


INPUT_FILENAME = "2023/4/input.txt"


ncards = [1] * 300
idx = 0
with open(INPUT_FILENAME, "r") as input_file:
  for idx, line in enumerate(input_file.readlines()):
    for n in range(ncards[idx]):
      line_points = 0
      card, nums = line.split(":")
      winning_nums, our_nums = nums.split("|")
      winning_nums = [int(n.strip()) for n in winning_nums.strip().split(" ") if n.strip() != ""]
      our_nums = [int(n.strip()) for n in our_nums.strip().split(" ") if n.strip() != ""]
      for num in our_nums:
        if num in winning_nums:
          line_points += 1
      for i in range(line_points):
        ncards[idx+i+1] += 1
ncards = ncards[0:idx+1]
print(ncards)
print("NCARDS: %d" % sum(ncards))