import sys

def read_requests(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def c_scan(initial_position, requests):
    requests.sort()
    total_head_movements = 0
    current_position = initial_position

    right_requests = [r for r in requests if r >= current_position]
    left_requests = [r for r in requests if r < current_position]

    # Service requests to the right
    for request in right_requests:
        total_head_movements += abs(current_position - request)
        current_position = request

    # Jump to the beginning of the disk and service left requests
    if left_requests:
        total_head_movements += abs(current_position - 4999)  # Go to the end
        total_head_movements += abs(4999 - 0)  # Jump from end to beginning
        current_position = 0
        for request in left_requests:
            total_head_movements += abs(current_position - request)
            current_position = request

    return total_head_movements

def main():
    if len(sys.argv) != 3:
        print("Usage: python C_SCAN.py <initial_position> <filename>")
        sys.exit(1)

    initial_position = int(sys.argv[1])
    filename = sys.argv[2]
    requests = read_requests(filename)

    total_movements = c_scan(initial_position, requests)
    print(f"C-SCAN Total Head Movements: {total_movements}")

if __name__ == "__main__":
    main()
