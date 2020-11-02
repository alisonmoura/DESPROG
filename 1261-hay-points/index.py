[ m, n ] = input().split()

m = int(m)
n = int(n)

jobs_point = {}

for i in range(m):
    [ name, salary ] = input().split()
    jobs_point[name] = int(salary)

for i in range(n):
    total = 0
    job_description = ""
    typed_in = input()
    while (typed_in != '.'):
        job_description += " "
        job_description += typed_in
        typed_in = input()
    
    for word in job_description.split():
        if word in jobs_point:
            total += jobs_point[word]

    print(total)