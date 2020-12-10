import random
from hungarian_algorithm import Hungarian

input = {
    'A': {'#191': 22, '#122': 14, '#173': 120, '#121': 21, '#128': 4, '#104': 51},
    'B': {'#191': 19, '#122': 12, '#173': 172, '#121': 21, '#128': 28, '#104': 43},
    'C': {'#191': 161, '#122': 122, '#173': 2, '#121': 50, '#128': 128, '#104': 39},
    'D': {'#191': 19, '#122': 22, '#173': 90, '#121': 11, '#128': 28, '#104': 4},
    'E': {'#191': 1, '#122': 30, '#173': 113, '#121': 14, '#128': 28, '#104': 86},
    'F': {'#191': 60, '#122': 70, '#173': 170, '#121': 28, '#128': 68, '#104': 104},
}


def generate_input(n):
    agent_task_input = {}
    random_tasks = random.sample(range(100, 300), n)
    for i in range(65, 65 + n + 1):
        task_cost = {'#' + str(i): random.randint(1, 200) for i in random_tasks}
        agent_task_input[chr(i)] = task_cost
    return agent_task_input


def generate_cost_matrix(agent_task_input):
    values = [value for value in agent_task_input.values()]
    cost_matrix = []

    for val in values:
        row = list(val.values())
        cost_matrix.append(row)

    return cost_matrix


if __name__ == '__main__':
    cost_matrix = generate_cost_matrix(input)

    hungarian = Hungarian(cost_matrix)
    hungarian.calculate()
    print("Calculated value:\t", hungarian.get_total_potential())

# e -  # 191 (1), b-#122 (12), c #173(2) d #121 (11) a #128(4) f #104 104
