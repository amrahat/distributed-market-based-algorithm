from input import input, generate_input, generate_cost_matrix
from hungarian_algorithm import Hungarian


def hungarian(cost_matrix):
    hungarian = Hungarian(cost_matrix)
    hungarian.calculate()
    return hungarian.get_total_potential()


if __name__ == '__main__':
    agent_task_input = generate_input(10)
    cost_matrix_input = generate_cost_matrix(agent_task_input)
    print(hungarian(cost_matrix_input))
