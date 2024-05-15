import sys

def read_requests(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def scan(initial_position, requests, direction='left'):
    requests.sort()
    total_head_movements = 0
    current_position = initial_position

    left_requests = [r for r in requests if r < current_position]
    right_requests = [r for r in requests if r >= current_position]

    if direction == 'left':
        # Service requests to the left and then to the right
        for request in reversed(left_requests):
            total_head_movements += abs(current_position - request)
            current_position = request
        if right_requests:
            total_head_movements += abs(current_position - right_requests[0])
            current_position = right_requests[0]
        for request in right_requests:
            total_head_movements += abs(current_position - request)
            current_position = request
    else:
        # Service requests to the right and then to the left
        for request in right_requests:
            total_head_movements += abs(current_position - request)
            current_position = request
        if left_requests:
            total_head_movements += abs(current_position - left_requests[-1])
            current_position = left_requests[-1]
        for request in reversed(left_requests):
            total_head_movements += abs(current_position - request)
            current_position = request

    return total_head_movements

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python SCAN.py <initial_position> <filename> [<direction>]")
        sys.exit(1)

    initial_position = int(sys.argv[1])
    filename = sys.argv[2]
    direction = sys.argv[3].lower() if len(sys.argv) == 4 else 'left'
    requests = read_requests(filename)

    if direction not in ['left', 'right']:
        print("Direction must be 'left' or 'right'")
        sys.exit(1)

    total_movements = scan(initial_position, requests, direction)
    print(f"SCAN Total Head Movements ({direction}): {total_movements}")

if __name__ == "__main__":
    main()
