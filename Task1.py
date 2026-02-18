import json
import os
from datetime import datetime 
class ToDoList:
    def _init_(self,filename="tasks.json"):
        self.filename=filename
        self.tasks=self.load_tasks()
    def load_tasks(self):
        #Load Tasks from file
        if os.path.exists(self.filename):
            with open(self.filename,'r')as file:
                return json.load(file)
        return[]
    def save_tasks(self,task):
        #Save tasks to file
        with open (self.filemane,'w')as file:
            json.dump(self.tasks,file,indent=2)
    
    def add_tasks(self):
        #add a new file
        new_task={
            'id':len(self.tasks)+1,
            'task':task,
            'completed':False,
            'created-at':datetime.now().strftime("%Y-%m-%d% H:%M:%S")
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added successfully!(ID:{new_task['id']})")
    def view_tasks(self):
        #view all tasks
        if not self.tasks:
            print("No tasks found ")
            return
        print("\n" + "="*60)
        print("YOUR TO-DO LIST")
        print("="*60)
        for task in self.tasks:
            status="Right"if task['completed'] else""
            print(f"[{status}]ID:{task['id']}|{task['task']}|created:{task['created_at']}")
            print("="*60 + "\n")

    def update_task(self,task_id,new_task=None,completed=None):
        #Update a task
        for task in self.tasks:
            if task['id']==task_id:
                if new_task:
                    task['task']=new_task
                if completed is None:
                    task['completed']=completed 
                self.save_tasks()
                print("f Task{task_id}updated successfully!")
                return
            print(f"Task with ID{task_id}not found!")

    def delete_task(self,task_id):
        #delete a Task
        for i,task in enumerate(self.tasks):
            if task['id']==task_id:
                deleted=self.tasks.pop(i)
                self.save_tasks()
                print(f"Task \'{deleted['task']}deleted successfully!")
                return
        print(f"task with ID{task_id} not found")

    def run(self):
        #main program loop
        while True:
            print("\n"+"="*40)
            print("TO-DO LIST APPLICATION")
            print("="*40)
            print("1.Add Task")
            print("2.View Tasks")
            print("3.Update task")
            print("4.Delete Task")
            print("5.Exit")
            print("="*40)
            choice=int(input("enter your choice (1-5)"))
            if choice==1:
                task=input("enter task description:")
                self.add_tasks(task)
            elif choice==2:
                self.view_tasks()
            elif choice==3:
                try:
                    task_id=int(input("Enter task ID to update:"))
                    print("1.Update description")
                    print("2.Mark as complete/incomplete")
                    sub_choice=input("Enter choice:")
                    if sub_choice==1:
                        new_task=input("Enter new task description:")
                        self.update_task(task_id,new_task=new_task)
                    elif sub_choice==2:
                        status=input("mark as complete?(y/n):").lower()=='y'
                        self.update_tasks(task_id,completed=status)
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid task ID!")
            elif choice==4:
                try:
                    task_id=int(input("Enter task ID to delete"))
                    self.delete_task(task_id)
                except ValueError:
                    print("Invalid task_id")
            elif choice==5:
                print("thank you for trying To-Do Application")
                break
            else:
                print("Invaalid choice!Please try again")
if __name__ == "__main__":
    app=ToDoList()
    app.run()
                




            


        


