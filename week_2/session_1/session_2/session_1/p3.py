def get_highest_priority_task(tasks):
    priority_level = 0
    high_task = None
    for task in tasks:
        if int(tasks[task]) > priority_level:
            priority_level = tasks[task]
            high_task = task
        elif int(tasks[task]) == priority_level:
            if task < high_task:  # This checks if the current task name is alphabetically smaller
                high_task = task
    tasks.pop(high_task)
    return high_task
    

def main():
    tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
    perform_task = (get_highest_priority_task(tasks))
    print(perform_task)

    perform_task = (get_highest_priority_task(tasks))
    print(perform_task)

    perform_task = (get_highest_priority_task(tasks))
    print(perform_task)

    print(tasks)

main()