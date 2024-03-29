n = int(input())
m = input()

if n == 1:
    print(m)
    exit(0)

numbers = []
operators = []
for k, v in enumerate(m):
    if k % 2 == 0:
        numbers.append(int(v))
    else:
        operators.append(v)


def operate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    else:
        return a * b


def operate_all(numbers, operators):
    result = numbers[0]
    for k, v in enumerate(operators):
        result = operate(result, numbers[k + 1], v)

    return result


answer = -int(1e10)


# 백트레이싱. 뒤에서부터 연산함
def dfs(idx, numbers, operators, visited):
    # 가장 마지막까지 왔음. 전체 계산하면 됨
    if idx == 0:
        global answer
        answer = max(answer, operate_all(numbers, operators))
        return

    # 괄호 쳐서 계산하는 거
    if visited[idx + 1] is False:
        new_numbers = numbers[:idx] + [operate(numbers[idx], numbers[idx + 1], operators[idx])] + numbers[idx + 2:]
        new_operators = operators[:idx] + operators[idx + 1:]
        new_visited = visited[:]
        new_visited[idx] = True
        dfs(idx - 1, new_numbers, new_operators, new_visited)
    # 괄호 안쳐서 계산하는 거
    dfs(idx - 1, numbers, operators, visited[:])


initial_index = len(operators) - 1
dfs(initial_index, numbers, operators, [False] * (len(operators) + 1))
print(answer)
