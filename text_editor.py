# Enter your code here. Read input from STDIN. Print output to STDOUT
Q = int(input())
S=''
deleted_stack = []
lengths_stack = []
operations_stack = []
for i in range(Q):
    command = input()
    command_no = int(command[:1])
    if command_no == 1:
        S += command[2:]
        operations_stack.append(1)
        lengths_stack.append(len(command[2:]))
    elif command_no == 2:
        pos = len(S) - int(command[2:])
        deleted_stack.append(S[pos:])
        S = S[:pos]
        operations_stack.append(2)
    elif command_no == 3:
        k = int(command[2:])
        print(S[k - 1])
    else:
        last_operation = operations_stack.pop()
        if last_operation == 1:
            lngth = lengths_stack.pop()
            S = S[:(len(S) - lngth)]
        else:
            S += deleted_stack.pop()