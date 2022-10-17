import time
from random import randint

def matrixMultiplication(n):
    #creates matrices A and B and populates them with random integers in range 10,000, also creates a matrix to store the results
    matrixA = []
    matrixB = []
    resultMatrix = []
    for i in range(n):
        matrixA.append([randint(1, 10000) for i in range(n)])
        matrixB.append([randint(1, 10000) for i in range(n)])
        resultMatrix.append([[0] * n for i in range(n)])

    #multiplies every number of row x in A with the appropriate number in column x of B, and sums up the results
    for row in range(len(matrixA)):
        for column in range(len(matrixB)):
            result = 0
            for num in range(len(matrixB)):
                result += matrixA[row][num] * matrixB[num][column]
            resultMatrix[row][column] = result

def test():
    numberOfTests = 5
    iterations = [20, 40, 60, 80, 100, 120, 140, 160]
    times = []
    #iteratively runs the matrix multiplication function
    #runs the program the amount of times specified and obtains the average time for each value of n
    for num in iterations:
        for i in range(numberOfTests):
            time1 = time.time()
            for i in range(1, num):
                matrixMultiplication(i)
            time2 = time.time()
            times.append(time2 - time1)
            averageTimes = round((sum(times)) / len(times), 3)
        print(f"The average time for {num} iterations is {averageTimes} seconds")

if __name__ == "__main__":
    test()
