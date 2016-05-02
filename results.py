import sys

def getResults(threshold):
    numNegative = 0;
    numPositive = 0;

    with open('fr_results.txt', 'r') as f:
        content = f.read().splitlines()

    for i in range(0, len(content)):
        if content[i] == 'negative':
            numNegative = numNegative + 1
        elif content[i] == 'positive':
            numPositive = numPositive + 1

    results = numNegative / (numNegative + numPositive)
    if results < threshold:
        print "pass"
        return "pass"
    else:
        print "fail"
        return "fail"

if __name__ == '__main__':
    getResults(0.6)


