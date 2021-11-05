# Original challenge can be found here:
# https://www.hackerrank.com/challenges/py-the-captains-room/

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
k = input()
room_list = map(int, input().split())

count_dict = {}
for room in room_list:
    if room in count_dict:
        count_dict[room] += 1
    else:
        count_dict[room] = 1

for room in count_dict:
    if count_dict[room] == 1:
        captain_room = room


print(captain_room)
