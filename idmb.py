from input import generate_input


# input: ('agent': (taskid, cost)
def should_swap_tasks(agent1, agent2, allocated_task, agent_task_input):
    task1 = allocated_task[agent1]
    task2 = allocated_task[agent2]

    current_total_cost = task1[1] + task2[1]

    cost_after_swapping = agent_task_input[agent1][task2[0]] + agent_task_input[agent2][task1[0]]

    return cost_after_swapping < current_total_cost


def swap_task(agent1, agent2, allocated_task, agent_task_input):
    temp = allocated_task[agent1]
    allocated_task[agent1] = (allocated_task[agent2][0], agent_task_input[agent1][allocated_task[agent2][0]])
    allocated_task[agent2] = (temp[0], agent_task_input[agent2][temp[0]])


def idmb(agent_task_input):
    unallocated_task = list(agent_task_input[list(agent_task_input.keys())[0]].keys())
    unallocated_agents = list(agent_task_input.keys())
    allocated_task = {}  # {"A", (#192, 1)
    for task in unallocated_task:
        cost_list = {x: agent_task_input[x][task] for x in unallocated_agents}
        minimum = min(cost_list.items(), key=lambda x: x[1])
        allocated_task[minimum[0]] = (task, minimum[1])

        # for agent in allocated_task:
        #     if should_swap_tasks(minimum[0], agent, allocated_task):
        #         print("swapping", minimum[0], agent)
        #         swap_task(minimum[0], agent, allocated_task)

        unallocated_agents.remove(minimum[0])  # removing the agents as it has been allocated

    for agent in allocated_task:
        other_agents_task = allocated_task.copy()
        del other_agents_task[agent]
        for other_agent in other_agents_task:
            if should_swap_tasks(agent, other_agent, allocated_task, agent_task_input):
                swap_task(agent, other_agent, allocated_task, agent_task_input)

    # print(allocated_task)

    total_cost = sum(v for (name, v) in allocated_task.values())

    return total_cost


if __name__ == '__main__':
    print(idmb(generate_input(10)))
