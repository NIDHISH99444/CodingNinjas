import  collections
def snakesAndLadders( board):

    N = len(board)
    board_linear = [0]
    order = True
    r = N - 1

    while (r >= 0):
        row = board[r]
        if not order:
            row.reverse()
        order = not (order)
        board_linear = board_linear + row
        r -= 1

    queue = collections.deque()
    queue.append((1, 0))
    visited = set([1])
    dest = len(board_linear) - 1

    while queue:
        current_pos, steps = queue.popleft()
        for next_pos in range(current_pos + 1, current_pos + 7):
            if next_pos == dest:
                return steps + 1

            if next_pos not in visited:
                visited.add(next_pos)
                if board_linear[next_pos] != -1:
                    # Has ladder or snake.
                    if board_linear[next_pos] == dest:
                        return steps + 1
                    queue.append((board_linear[next_pos], steps + 1))
                else:
                    queue.append((next_pos, steps + 1))
    return -1

board=[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]

print(snakesAndLadders(board))