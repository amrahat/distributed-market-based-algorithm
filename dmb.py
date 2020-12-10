# from input import input
from input import generate_input


def dmb(agent_task_input):
    unallocated_task = list(agent_task_input[list(agent_task_input.keys())[0]].keys())
    unallocated_agents = list(agent_task_input.keys())
    allocated_task = {}  # {"A", (#192, 1)
    total_cost = 0
    for task in unallocated_task:
        cost_list = {x: agent_task_input[x][task] for x in unallocated_agents}
        minimum = min(cost_list.items(), key=lambda x: x[1])
        total_cost = total_cost + minimum[1]
        allocated_task[minimum[0]] = (task, minimum[1])
        unallocated_agents.remove(minimum[0])  # removing the agents as it has been allocated

    return total_cost


if __name__ == '__main__':
    print(dmb(generate_input(10)))
