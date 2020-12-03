import matplotlib.pyplot as plt
import numpy as np


def main():
    reqs = [10, 100, 300, 500, 1000, 1500]

    random_lb = [554, 629, 537, 634, 644, 547]

    round_robin_lb = [564, 593, 524, 577, 582, 565]

    second_random_lb = [557, 641, 518, 583, 592, 532]

    cpu_work_lb = [556, 610, 490, 575, 551, 503]

    response_time_lb = [562, 584, 542, 573, 587, 556]
       
    barWidth = 0.15
    fig = plt.subplots(figsize =(20, 8)) 

    br1 = np.arange(len(reqs)) 
    br2 = [x + barWidth for x in br1] 
    br3 = [x + barWidth for x in br2] 
    br4 = [x + barWidth for x in br3] 
    br5 = [x + barWidth for x in br4] 

    plt.bar(br1, random_lb, color ='r', width = barWidth, 
            edgecolor ='grey', label ='random_lb') 
    plt.bar(br2, round_robin_lb, color ='g', width = barWidth, 
            edgecolor ='grey', label ='round_robin_lb') 
    plt.bar(br3, second_random_lb, color ='b', width = barWidth, 
            edgecolor ='grey', label ='second_random_lb') 
    plt.bar(br4, cpu_work_lb, color ='c', width = barWidth, 
            edgecolor ='grey', label ='cpu_work_lb') 
    plt.bar(br5, response_time_lb, color ='m', width = barWidth, 
            edgecolor ='grey', label ='response_time_lb')

    plt.xlabel('Number of requests', fontweight ='bold') 
    plt.ylabel('Response time', fontweight ='bold') 
    plt.xticks([r + barWidth for r in range(len(random_lb))], reqs)
    plt.legend()

    plt.show() 

if __name__ == '__main__':
	main()
