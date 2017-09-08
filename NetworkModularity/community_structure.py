import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of the given matches' file")
parser.add_argument("-n", "--GROUPS", type=int, help="amount of groups")
args = parser.parse_args()
graph_file = args.filename

if args.GROUPS:
    groups_number = args.GROUPS
else:
    groups_number = 2

node_connections = {}
degrees_to_each_node = {}
groups = []

f = open(graph_file)
for line in f:
    helper_list = []
    for i in line.split():
        helper_list.append(i)
    if helper_list[0] not in node_connections:
        node_connections[helper_list[0]] = []
        node_connections[helper_list[0]].append(helper_list[1])
        degrees_to_each_node[helper_list[0]] = 1
        groups.append(int(helper_list[0]))
    else:
        node_connections[helper_list[0]].append(helper_list[1])
        degrees_to_each_node[helper_list[0]] += 1
    if helper_list[1] not in node_connections:
        node_connections[helper_list[1]] = []
        node_connections[helper_list[1]].append(helper_list[0])
        degrees_to_each_node[helper_list[1]] = 1
        groups.append(int(helper_list[1]))
    else:
        node_connections[helper_list[1]].append(helper_list[0])
        degrees_to_each_node[helper_list[1]] += 1

f.close()
groups.sort()
groups = [[str(i)] for i in groups]
total_degrees = 0
for i in node_connections:
    total_degrees += len(node_connections[i])


initial_modularity = 0
for node in node_connections:
    initial_modularity -= pow(len(node_connections[node])/total_degrees, 2)


def connections_between_groups(ei_lst, ej_list):
    connections_counter = 0
    for i in ei_lst:
        for j in ej_list:
            if i in node_connections[j]:
                connections_counter += 1
    return connections_counter


def connections_within_group(group_list):
    connections_counter = 0
    for i in group_list:
        for j in group_list:
            if i in node_connections[j]:
                connections_counter += 1
    return connections_counter


def ai(group):
    ai = 0
    for node in group:
        ai += degrees_to_each_node[node]/total_degrees
    return ai


def new_group(group1, group2):
    group = ""
    for i in group1:
        group = group + str(i) + " "
    for j in group2:
        group = group + str(j) + " "
    return group


def groups_rearrange(q, grp):
    list1 = []
    for i in grp[0].split():
        list1.append(i)
    for i in list1:
        for j in groups:
            if i in j:
                if j in groups:
                    groups.remove(j)
    groups.append(list1)

while len(groups) > groups_number:
    modularity = []
    for i in groups:
        for j in groups:
            if (i != j) & (i < j):
                eij = connections_between_groups(i, j)
                if eij != 0:
                    DQ = 2*((eij/total_degrees) - (ai(i) * ai(j)))
                    group = str(new_group(i, j))
                    modularity.append([DQ, group])
                    modularity.sort(reverse=True)

    q = modularity[0][0]
    initial_modularity += q
    grp = modularity[0][1:]
    groups_rearrange(q, grp)

groups.sort()

final_groups = []

for i in groups:
    list3 = [int(j) for j in i]
    list3.sort()
    final_groups.append(list3)

final_groups.sort()
for i in final_groups:
    print(i)

print("Q = " + str(round(initial_modularity, 4)))




