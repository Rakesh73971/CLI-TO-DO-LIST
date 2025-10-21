import csv,os

FILE_NAME = 'tasks.csv'

def print_menu():
    print('\nTodo-List')
    print('1.Display Tasks')
    print('2.Add Task')
    print('3.Remove Task')
    print('4.Exit')


def get_choice():
    while True:
        choice = input('Enter your choice: ')
        valid_choice = ('1','2','3','4')
        if choice not in valid_choice:
            print('Invalid Choice')
            continue
        else:
            return choice
        
def load_tasks():
    tasks=[]
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,mode='r',newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    tasks.append(row[0])
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME,mode='w',newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])
            
def display_tasks(tasks):
    if not tasks:
        print('No tasks entered')
        return 
    for index,task in enumerate(tasks,start=1):
        print(f"{index}. {task}")
    
def add_task(tasks):
    while True:
        task = input('Enter your task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            save_tasks(tasks)
            break
        else:
            print('Invalid task')

def remove_task(tasks):
    display_tasks(tasks)
    while True:
        try:
            task_number = int(input('Enter task number: '))
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number-1)
                save_tasks(tasks)
                print(f"{removed} removed successfully")
                break
            else:
                print('Invalid task number')
        except ValueError:
            print('Enter a number.')

def main():
    tasks = load_tasks()
    while True:
        print_menu()

        choice = get_choice()
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            break
    
if __name__ == "__main__":
    main()
