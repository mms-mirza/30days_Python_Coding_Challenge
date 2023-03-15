'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''
    
def main():

    test = [5, 4, 2, 1]
    print(solution(test))

def solution(A):

    #create a range of integers and +1 for the missing integer (+2 as range function returns 1 less than stop param)
    expected_sum = range(1, len(A) + 2)
    #sum of the expected range of integers - sum of elements = missing element/integer
    return sum(expected_sum) - sum(A)

if __name__ == "__main__":
    main()