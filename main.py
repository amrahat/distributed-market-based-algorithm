from input import generate_input, generate_cost_matrix
from dmb import dmb
from idmb import idmb
from hungarian import hungarian
import matplotlib.pyplot as plt

if __name__ == '__main__':
    input_count = [3, 5, 8, 10, 13, 15, 18, 20, 22, 25]
    dmb_result = {}
    idmb_result = {}
    hungarian_result = {}
    # hungarian_alt_result = {}
    for count in input_count:
        print("-" * 80)
        print("Input task count ", count)
        agent_task_input = generate_input(count)
        dmb_cost = dmb(agent_task_input)
        idmb_cost = idmb(agent_task_input)
        print("DMB", dmb_cost)
        print("IDMB", idmb_cost)

        dmb_result[count] = dmb_cost
        idmb_result[count] = idmb_cost

        cost_matrix_input = generate_cost_matrix(agent_task_input)
        hungarian_cost = hungarian(cost_matrix_input)
        print("Hungarian", hungarian_cost)
        hungarian_result[count] = hungarian_cost

    # generating plots
    colors = ['orange', 'red', 'blue']
    plt.rcParams.update({'font.size': 14})
    plt.plot(list(dmb_result.keys()), list(dmb_result.values()), colors[0], label='DMB')
    plt.plot(list(idmb_result.keys()), list(idmb_result.values()), colors[1], label='IDMB')
    plt.plot(list(hungarian_result.keys()), list(hungarian_result.values()), colors[2], label='Hungarian')
    plt.legend(loc='upper left',
               fancybox=False, shadow=False, ncol=4, prop={'size': 10})
    plt.xlabel("Number of tasks/agents")
    plt.ylabel("Cost")
    plt.show()

    # generating error plots
    dmb_error = {x: (dmb_result[x] - hungarian_result[x]) / hungarian_result[x] * 100 for x in hungarian_result.keys()}
    idmb_error = {x: (idmb_result[x] - hungarian_result[x]) / hungarian_result[x] * 100 for x in
                  hungarian_result.keys()}

    plt.plot(list(dmb_error.keys()), list(dmb_error.values()), colors[0], label='DMB')
    plt.plot(list(idmb_error.keys()), list(idmb_error.values()), colors[1], label='IDMB')
    plt.legend(loc='upper left',
               fancybox=False, shadow=False, ncol=4, prop={'size': 10})
    plt.xlabel("Number of tasks/agents")
    plt.ylabel("Error in % in comparison with the optimal solution")
    plt.show()
