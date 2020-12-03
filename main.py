from policies import Scheduler
import time

if __name__ == "__main__":
    nr_reqs = int(input("Enter number of requests:"))
    scheduler = Scheduler()

    policy_list = ['random_lb', 'round_robin_lb', 'second_random_lb',
                   'cpu_work_lb', 'response_time_lb']
    print('########################################')
    print('List of policies:')
    for i in policy_list:
        print(i)
    print('########################################')
    policy = input("Choose a policy's name from the list above:")

    while (1):
        if policy == "random_lb":
            t = time.perf_counter()
            scheduler.random_lb(nr_reqs)
            elapsed_time = time.perf_counter() - t
            print('System time: ', elapsed_time)
            break
        if policy == "round_robin_lb":
            t = time.perf_counter()
            scheduler.round_robin_lb(nr_reqs)
            elapsed_time = time.perf_counter() - t
            print('System time: ', elapsed_time)
            break
        if policy == "second_random_lb":
            t = time.perf_counter()
            scheduler.second_random_lb(nr_reqs)
            elapsed_time = time.perf_counter() - t
            print('System time: ', elapsed_time)
            break
        if policy == "cpu_work_lb":
            t = time.perf_counter()
            scheduler.cpu_work_lb(nr_reqs)
            elapsed_time = time.perf_counter() - t
            print('System time: ', elapsed_time)
            break
        if policy == "response_time_lb":
            t = time.perf_counter()
            scheduler.response_time_lb(nr_reqs)
            elapsed_time = time.perf_counter() - t
            print('System time: ', elapsed_time)
            break
        else:
            print("Invalid policy!")
            break
