import random
tasks = []

for i in range(10):
    tasks.append({
        'id': f't_{i}',
        'assignee':random.choice(['ivan','olga','petr','anna','oleg']),
        'status':random.choice(['in progress','blocked','in review','waiting vendor']),
        'days in status':random.randint(0,10)
    })
print(tasks)
assignees_in_progress = []
the_most = []

for el in tasks:
    if el['status'] == 'in progress' and el['days in status'] >= 7:
        assignees_in_progress.append(el['assignee'])

print(assignees_in_progress)


in_progress = []
blocked = []
in_review = []
waiting_vendor = []

for el in tasks:
    if el['status'] == 'in progress':
        in_progress.append(el['assignee'])
    if el['status'] == 'blocked':
        blocked.append(el['assignee'])
    if el['status'] == 'in review':
        in_review.append(el['assignee'])
    if el['status'] == 'waiting vendor':
        waiting_vendor.append(el['assignee'])
if len(in_progress) == 1:
    print(in_progress)
if len(blocked) == 1:
    print(blocked)
if len(in_review) == 1:
    print(in_review)
if len(waiting_vendor) == 1:
    print(waiting_vendor)

the_most_a = ''
num = 0

for el in tasks:
    if el['status'] == 'in progress' or el['status'] == 'blocked':
        if el['days in status'] > num:
            num = el['days in status']
            the_most_a = el['assignee']

print(the_most_a)