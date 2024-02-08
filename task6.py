items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


class Item:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

def greedy_algorithm(items: dict, budget):
    items_list = []
    for key, value in items.items():
        items_list.append(Item(key, value['cost'], value['calories']))
    items_list.sort(key=lambda x: x.ratio, reverse=True)
    total_calories = 0
    print(f"Budget = {budget}")
    print("Order of selection:")
    i = 1
    for item in items_list:
        if budget >= item.cost:
            print(f"{i}. {item.name}")
            i += 1
            budget -= item.cost
            total_calories += item.calories
    return f"Total calories = {total_calories}"
    

def dynamic_programming(items, budget):
    print(f"Budget = {budget}")
    cost = [i["cost"] for i in items.values()]
    calories = [i["calories"] for i in items.values()]
    dish = [i for i in items.keys()]
    n = len(cost)
    K = [[0 for b in range(budget + 1)] for j in range(n + 1)]
    D = [[[] for b in range(budget + 1)] for j in range(n + 1)]
    for j in range(1, n + 1):
        for b in range(1, budget + 1):
            if cost[j - 1] <= b:
                K[j][b] = max(calories[j - 1] + K[j -1][b - cost[j - 1]], K[j - 1][b])
                if calories[j - 1] + K[j -1][b - cost[j - 1]] > K[j - 1][b]:
                    D[j][b] = D[j - 1][b - cost[j - 1]].copy()
                    D[j][b].append(dish[j-1])
                else:
                    D[j][b] = D[j - 1][b]
            else:
                K[j][b] = K[j - 1][b]
                D[j][b] = D[j - 1][b].copy()
       # print(K[j])
        #print(D[j])
    return f"Total calories = {K[n][budget]}. You should choose {D[n][budget]}" 





if __name__ == "__main__":
    print("Greedy algorithm")
    print(greedy_algorithm(items, 30))
    print()
    print("Dynamic programming")
    print(dynamic_programming(items, 30))