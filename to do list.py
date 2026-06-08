tasks = []
q = int(input('enter theno.of tasks you want to perform: '))
for a in range(q):
    tsk = input('Enter the task you want to perform: ')
    tasks.append(tsk)
print(tasks)

k = 1
for tsk in tasks:                   
       print(k,'.',tsk)               
       k+=1                         
       
index = int(input('\nEnter the number of which task you want to remove: '))
index = index - 1
if index >= 0 and index < len(tasks):
    removed_task =  tasks.pop(index)
    print(f'Removed Task: {removed_task}')
    print('Updated task list: ',tasks)
else:
    print('enter correct number')

values = input('enter words seperated by space: ')
s = set(values.split())
print(s)
