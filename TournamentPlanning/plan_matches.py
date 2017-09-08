import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of the given matches' file")
args = parser.parse_args()
graph_file = args.filename

matches_schedule = open(graph_file)

players = []
matches = {}

for line in matches_schedule:
    helper_list = []
    for i in line.split():
        helper_list.append(i)
    if helper_list[0] not in matches:
        matches[helper_list[0]] = []
        matches[helper_list[0]].append(helper_list[1])
    else:
        matches[helper_list[0]].append(helper_list[1])
    if helper_list[1] not in matches:
        matches[helper_list[1]] = []
        matches[helper_list[1]].append(helper_list[0])
    else:
        matches[helper_list[1]].append(helper_list[0])


for key in matches:
    players.append(key)

players.sort()

availability = {}
for player in players:
    availability[player] = []
    for i in range(0, len(players)):
        availability[player].append(i)


def earliest_day_to_start(player_list, opponent_list):
    z = set(player_list) & set(opponent_list)
    earliest_day = min(z)
    return earliest_day


f = open(graph_file)
final_planning = []
for line in f:
    helper_list = []
    for i in line.split():
        helper_list.append(i)
    player = helper_list[0]
    opponent = helper_list[1]
    early_day = earliest_day_to_start(availability[player], availability[opponent])
    availability[player].remove(early_day)
    availability[opponent].remove(early_day)
    if str(player) > str(opponent):
        final_planning.append([str(opponent), str(player), str(early_day)])
    else:
        final_planning.append([str(player), str(opponent), str(early_day)])

f.close()
final_planning.sort()

for i in final_planning:
    print("(" + str(i[0]) + ", " + str(i[1]) + ") " + str(i[2]))

