#!/usr/bin/env python3

INPUT_FILENAME = "input1.txt"
NREDS = 12
NGREENS = 13
NBLUES = 14


with open(INPUT_FILENAME, "r") as input_file:
  possible_games = []
  sum_cube_power = 0
  for line in input_file:
    game, results = line.split(":")
    game_no = int(game[5:])
    #print (game_no)
    #print(line)
    results = results.split(";")
    possible_game = True
    max_num_cubes = {"red":0, "green":0, "blue":0}
    for result in results:
      num_cubes = {"red":0, "green":0, "blue":0}
      cubes = result.split(",")
      for cube in cubes:
        num, color = cube.strip().split(" ")
        num_cubes[color] = num_cubes[color] + int(num)
        if num_cubes[color] > max_num_cubes[color] : max_num_cubes[color] = num_cubes[color] 
      #print (num_cubes)
      if num_cubes["red"] > NREDS or num_cubes["green"] > NGREENS or num_cubes["blue"] > NBLUES:
        possible_game = False
    if possible_game : possible_games.append(game_no)
    #print (max_num_cubes)
    sum_cube_power += max_num_cubes["red"] * max_num_cubes["green"] * max_num_cubes["blue"]
  print("Possible games: ", possible_games)
  print("SUM: %d" % sum(possible_games))
  print("SUM CUBE POWER: %d" % sum_cube_power)
