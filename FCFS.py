import sys

def read_requests(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def fcfs(initial_position, requests):
    current_position = initial_position
    total_head_movements = 0

    for request in requests:
        total_head_movements += abs(current_position - request)
        current_position = request

    return total_head_movements

def main():
    if len(sys.argv) != 3:
        print("Usage: python FCFS.py <initial_position> <filename>")
        sys.exit(1)

    initial_position = int(sys.argv[1])
    filename = sys.argv[2]
    requests = read_requests(filename)

    total_movements = fcfs(initial_position, requests)
    print(f"FCFS Total Head Movements: {total_movements}")

if __name__ == "__main__":
    main()
