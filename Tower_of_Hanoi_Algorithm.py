def hanoi_solver(n):
    source = list(range(n,0,-1))
    auxiliary = []
    target = []
    states = [f"{source} {auxiliary} {target}"]
    
    def move_disks(count, start, end, spare):
        if count == 0:
            return
        move_disks(count - 1, start, spare, end)
        disk = start.pop()
        end.append(disk)
        states.append(f"{source} {auxiliary} {target}")

        move_disks(count - 1, spare, end, start)

        

    move_disks(n, source, target, auxiliary)
    return "\n".join(states)
print(hanoi_solver(3))