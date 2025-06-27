def insert(queue, task):
    queue.append(task)

def extract(queue):
    return queue.pop(0) if not is_empty(queue) else None

def peek(queue):
    return queue[0] if not is_empty(queue) else None

def is_empty(queue):
    return len(queue) == 0


def complete_next_task(queue):
    if is_empty(queue):
        print("No tasks in the queue.")
        return
    highest_priority_index = 0
    for i in range(1, len(queue)):
        if queue[i]['priority'] < queue[highest_priority_index]['priority']:
            highest_priority_index = i
    task = queue.pop(highest_priority_index)
    print(f"Completed task: {task['title']}, Duration: {task['duration']} mins, Priority: {task['priority']}")


def search_for_task(queue, title):
    sorted_queue = sorted(queue, key=lambda x: x['title']) 
    low, high = 0, len(sorted_queue) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_queue[mid]['title'] == title:
            print(f"Task found: {sorted_queue[mid]}")
            return sorted_queue[mid]
        elif sorted_queue[mid]['title'] < title:
            low = mid + 1
        else:
            high = mid - 1

    print("Task not found.")
    return None


def sort_tasks(queue):
    return sorted(queue, key=lambda x: x['duration'])  

def main():
    queue = []
    num_tasks = int(input("Enter number of tasks: "))

    for _ in range(num_tasks):
        title = input("Enter task title: ")
        duration = int(input("Enter duration in minutes: "))
        priority = int(input("Enter priority (lower number = higher priority): "))
        task = {'title': title, 'duration': duration, 'priority': priority}
        insert(queue, task)

    print("\nCurrent Task Queue:")
    for task in queue:
        print(task)

    print("\n--- Complete Next Task ---")
    complete_next_task(queue)

    print("\n--- Search For Task ---")
    title = input("Enter title to search: ")
    search_for_task(queue, title)

    print("\n--- Sorted Tasks by Duration ---")
    sorted_queue = sort_tasks(queue)
    for task in sorted_queue:
        print(task)


main()
