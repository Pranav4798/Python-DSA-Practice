n = 2 
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

def exclusiveTime(n, logs):
    res = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        f_id, type, timestamp = log.split(':')
        f_id, timestamp = int(f_id), int(timestamp)

        if type == 'start':
            if stack:
                res[stack[-1]] += timestamp - prev_time
            stack.append(f_id)
            prev_time = timestamp
        else:
            res[stack.pop()] += timestamp - prev_time + 1
            prev_time = timestamp + 1

    return res

print(exclusiveTime(n, logs))