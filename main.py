import networkx as nx

#current to do: read in file as 2 lists, 1 left int 1 right int

user_1 = [] #Lists of users, user_1[i] and user_2[i] indicate an edge between element
user_2 = []

with open("facebook_links.txt") as File:
    for line in File:
        line = line.split("\t")      #Splits line into list of 3 elements
        user_1.append(line[0])
        user_2.append(line[1])

fb_graph = nx.Graph()



#Goal: Create a graph of friends from txt. Using graph, find avg degree and count of vertices with degree > 100. (need list of vertices' degrees)
#Adjacency list: An array of lists. vertex 1 would be element 1 in the array, and the element is a list of all the vertices
#If j is in list A[i], then i is in list A[j]
#There are many skipped elements in the txt (ex element 2 is connected to 1, but doesn't have it's own left list). Is there a way to optimize this? or just use a load of space