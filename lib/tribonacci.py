# Works like a Fibonacci, 
# but summing the last 3 (instead of 2) numbers of the sequence 
# to generate the next.


def tribonacci(signature, n):
    sequence = signature
    for i in range (3,n):
        next_num = sum(sequence[-3:-1]) + sequence[-1]
        sequence.append(next_num)

    return sequence