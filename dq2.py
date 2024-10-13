def power(a, b):
    # If b = 0, whatever be the value of a,
    # our result will be 1.
    res = 1
    while b > 0:
        # If b is an odd number, then
        # (a^b) = (a * (a^(b–1)/2)^2)
        if b & 1:
            res *= a

        # If b is an even number, then
        # (a^b) = ((a^2)^(b/2))
        a *= a
        b >>= 1
    return res

def find_digit(N):
    # No of digits
    digits = 1
    # Total numbers in current digit interval
    base = 9

    # Find the interval in which the Nth digit lies
    while N - digits * base > 0:
        N -= digits * base
        base *= 10
        digits += 1
    index = N % digits

    # Calculate the number which contains the Nth digit
    res = power(10, digits - 1) + (N - 1) // digits

    # Find out which digit in the number is the result
    if index != 0:
        res //= 10 ** (digits - index)
    return res % 10

# Driver Code
if __name__ == "__main__":
    
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    queries = l
    for query in queries:
        print find_digit(query),
    print