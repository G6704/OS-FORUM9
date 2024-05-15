# OS-FORUM9
Halo sie this is the disk scheduling algorithm from the assignment made in Python

## Type this first in the Terminal
```
python generate_requests.py
```
This is to generate the random series of number
once you've done this once, no need to type this again in the terminal for every Algorithm Testing

## SCAN Algorithm
```
python SCAN.py 100 requests.txt left

python SCAN.py 100 requests.txt right
```
When running the SCAN program, you need to specify which direction the disk head should initially move: towards the inner cylinders (left) or towards the outer cylinders (right)

## C-SCAN Algorithm
```
python C_SCAN.py 100 requests.txt 
```
## FCFS Algorithm
```
python FCFS.py 100 requests.txt
```

## Results from my Machine

- SCAN Algorithm (left) = 5071
- SCAN Algorithm (Right) = 9881
- C-SCAN Algorithm = 9992
- FCFS Algorithm = 1685456