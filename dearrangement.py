from math import factorial

# takes in n >= 1
# returns the number of possible derangements of n items
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |    1    |     0    |
# |---------|----------|
# |    2    |     1    |
# |---------|----------|
# |    3    |     2    |
# |---------|----------|
# |    4    |     9    |
# |---------|----------|
# |    5    |    44    |
# |---------|----------|
def numDerangements(n):# Used the dearrangement formula (d=∑ n​!(−1)^r/r!).
    d = 0
    for r in range(n+1):
        d += ((-1) ** r) * factorial(n) // factorial(r)
    return d
    
# Testing code provided in main():
def main():
    testArgs = [[1,0],[2,1],[3,2],[4,9],[5,44]]
    for arg in testArgs:
        nArg, answer = arg
        result = numDerangements(nArg)
        if result != answer:
            print(f"Failed numDerangements test with arg n={nArg}.\nExpected: {answer}, Got: {result}")
        else:
            print(f"Passed numDerangements test with arg n={nArg}.")
    return 0

if __name__ == '__main__':
    main()
