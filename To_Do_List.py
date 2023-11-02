tasks = []
tasks_priority = []
tasks_date = []
tasks_status=[]
def add_task():
    t1 = input("Enter new task name:")
    tasks.append(t1)
    t2 = int(input("Enter task priority: 1-High, 2-Medium, 3-Low:"))
    tasks_priority.append(t2)
    t3 = input("Enter due date for task:")
    tasks_date.append(t3)
    print("Task has been added succesfully")
    tasks_status.append("No")

def view_task():
    if len(tasks)==0:
        print("No Tasks")
    else:
        print("List of tasks are:")
        print("Sl No.\t  Task Name\t\t Task Priority\t Due Date\t Status")
        for i in range (len(tasks)):
            print(i+1,"\t",tasks[i],"\t\t",tasks_priority[i],"\t",tasks_date[i],"\t",tasks_status[i])

def mark_task():
    ch = int(input("Enter task number which is completed:"))
    tasks_status[ch-1] = "Yes" 

def delete_task():
    if len(tasks)==0:
        print("No tasks to be deleted")
    else:
        print("Tasks:")
        for i in range (len(tasks)):
            print(tasks[i])
        choice = int(input("Enter the task number to delete:"))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            del tasks_priority[choice-1]
            del tasks_date[choice-1]
            del tasks_status[choice-1]
            print("Task deleted succesfully.")
        else:
            print("Invalid Task Number")

def main():

        while True:
            print('\n======== To-Do-List Application ========')
            print("1.Add Task")
            print("2.View Task")
            print("3.Delete Task")
            print("4.Mark as Complete")
            print("5.Quit")

            choice = int(input("Enter your choice:"))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_task()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                mark_task()
            elif choice == 5:
                print("Goodbye")
                break
            else:
                print("Invalid Choice, Please Try again")
    
if __name__ == "__main__":
    main()

