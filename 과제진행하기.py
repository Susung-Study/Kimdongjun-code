def solution(plans):
    answer = []
    todolist = []
    
    for i in range(len(plans)):
        plans[i][1] = changetime(plans[i][1])
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key=lambda x:x[1])
    
    for i in range(len(plans)-1):
        todolist.append([plans[i][0],plans[i][2]])
        timediff = plans[i+1][1] - plans[i][1]
        while todolist and timediff:
            if todolist[-1][1] <= timediff:
                s,t = todolist.pop()
                timediff -= t
                answer.append(s)
            else:
                todolist[-1][1] -= timediff
                timediff = 0
    answer.append(plans[-1][0])
    
    while todolist:
        task = todolist.pop()
        answer.append(task[0])
    return answer

def changetime(time):
    time = time.split(':')
    return 60*int(time[0]) + int(time[1]) 