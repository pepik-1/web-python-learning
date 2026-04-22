clients = [
    (1,'111','a@x.com'),
    (2,'111','b@x.com'),
    (3,'222','c@x.com'),
    (4,'333','c@x.com'),
    (5,'444','d@x.com')       
           ]
phones = {}
emails = {}

for id,num,email in clients:
    phones.setdefault(num,set()).add(id)
    emails.setdefault(email,set()).add(id)
print(phones)
print(emails)

dubles = []
for o in (phones,emails):
    for ids in o.values():
        if len(ids) > 1:
            dubles.append(ids)


dub = set()

for n in dubles:
    dub |= n

unique = []

for el in clients:
    if el[0] not in dub:
        unique.append(el[0])
print(unique)
