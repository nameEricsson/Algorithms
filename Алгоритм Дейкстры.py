from math import inf
graph = {}
graph['you'] = ['alice', 'bob', 'claire']


graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2


graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}


infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:   #перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:    #если этот узел с наименьшец стоимостью из уже виденных и он еще не был обработан
            lowest_cost = cost    #он назначается новым узлом с наименьшей стоимосью
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)    #найти узел с наименьшей стоимостью среди необработанных
while node is not None:                #если обработаны все узлы цикл вайл завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n] #перебрать всех соседей текущего узла
        if costs[n] > new_cost:        #если к соседу можно быстрее добраться через текущий узел обновить стоимость для этого узла
            costs[n] = new_cost
            parents[n] = node          #этот узел стоновится новым родителем для соседа
    processed.append(node)             #узел помечается как обработанный
    node = find_lowest_cost_node(costs)#найти следуюзий узел для обработки и повторить цикл

print('Ваш маршрут будет состоять из узлов ', processed)

