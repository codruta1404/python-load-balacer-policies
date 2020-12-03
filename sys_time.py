import matplotlib.pyplot as plt
import numpy as np

def main():
    reqs = [10, 100, 300, 500, 1000, 1500]

    random_lb_sys_time = [6.64, 59.50, 76.25, 249.78, 375.04, 385.987]

    round_robin_lb_sys_time = [1.25, 13.27, 39.98, 66.98, 132.07, 194.59]

    second_random_lb_sys_time = [1.99, 19.13, 46.81, 84.29, 290.91, 236.25]

    cpu_work_lb_sys_time = [1.90, 13.93, 38.40, 72.10, 128.40, 192.19]

    response_time_lb_sys_time = [1.21, 15.51, 53.29, 77.60, 154.31, 231.22]

    barWidth = 0.15
    fig = plt.subplots(figsize =(20, 8)) 

    br1 = np.arange(len(reqs)) 
    br2 = [x + barWidth for x in br1] 
    br3 = [x + barWidth for x in br2] 
    br4 = [x + barWidth for x in br3] 
    br5 = [x + barWidth for x in br4] 

    plt.bar(br1, random_lb_sys_time, color ='r', width = barWidth, 
            edgecolor ='grey', label ='random_lb_sys_time') 
    plt.bar(br2, round_robin_lb_sys_time, color ='g', width = barWidth, 
            edgecolor ='grey', label ='round_robin_lb_sys_time') 
    plt.bar(br3, second_random_lb_sys_time, color ='b', width = barWidth, 
            edgecolor ='grey', label ='second_random_lb_sys_time') 
    plt.bar(br4, cpu_work_lb_sys_time, color ='c', width = barWidth, 
            edgecolor ='grey', label ='cpu_work_lb_sys_time') 
    plt.bar(br5, response_time_lb_sys_time, color ='m', width = barWidth, 
            edgecolor ='grey', label ='response_time_lb_sys_time')

    plt.xlabel('Number of requests', fontweight ='bold') 
    plt.ylabel('System time', fontweight ='bold') 
    plt.xticks([r + barWidth for r in range(len(random_lb_sys_time))], reqs)
    plt.legend()
    
    plt.show() 

if __name__ == '__main__':
	main()
