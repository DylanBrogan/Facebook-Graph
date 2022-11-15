import networkx as nx

#Lists of users, elements at the same index indicates an edge
user_list_1 = [] 
user_list_2 = []

#Parses file into 2 lists
with open("facebook_links.txt") as File:
    for line in File:
        line = line.split("\t")
        user_list_1.append(line[0])
        user_list_2.append(line[1])

#Creates list of tuples of all edges to be inserted into a graph
edge_list = []
count = 0
for user in user_list_1:
    edge_list.append((user, user_list_2[count]))
    count += 1

fb_graph = nx.Graph(edge_list)

degree_list = nx.degree_histogram(fb_graph)

#Counts number of users with more than 100 friends
v_count = 0
for vertex in degree_list:
    if vertex>100:
        v_count += 1

print(f"Average degree of vertices: {sum(degree_list)/len(degree_list)}")
print(f"Vertices with degree >100: {v_count}")