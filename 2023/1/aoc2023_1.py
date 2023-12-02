#!/usr/bin/env python3

INPUT_FILENAME = "input2.txt"
digits = "0123456789"

digits_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits_ov_str = []
digits_ov_num = []
for idx1, ds1 in enumerate(digits_str):
  for c1 in range(len(ds1)-1, -1, -1):
    ds1_ss = ds1[c1:]
    for idx2, ds2 in enumerate(digits_str):
      ds2_ss = ds2[0:len(ds1_ss)]
      if ds1 != ds2 and ds1_ss == ds2_ss:
        digits_ov_str.append("%s%s" % (ds1[0:-len(ds1_ss)], ds2))
        digits_ov_num.append("%d%d" % (idx1+1, idx2+1))

sum = 0
with open(INPUT_FILENAME, "r") as input_file:
  for line in input_file:
    for idx, val in enumerate(digits_ov_str):
      if val in line : line = line.replace(val, digits_ov_num[idx])
    for idx, val in enumerate(digits_str):
      if val in line : line = line.replace(val, "%d" % (idx+1))
    first = None
    last = None
    for digit in line:
      if digit in digits:
        if first is None:
          first = digits.index(digit)
        last = digits.index(digit)
    line_number = int("%s%s" % (first, last))
    sum += line_number

print ("SUM: %d" % sum)
