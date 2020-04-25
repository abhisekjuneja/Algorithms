"""
Given an array A, find the greatest number in a that is a product of two elements in A. 
If there are no two elements in A that can be multiplied to produce another element contained in A, return -1.

Example

    For a = [10, 3, 5, 30, 35], the output should be
    maxPairProduct(a) = 30.

    Explanation: 30 is a product of 10 and 3.

    For a = [2, 5, 7, 8], the output should be
    maxPairProduct(a) = -1;

    For a = [10, 2, 4, 30, 35], the output should be
    maxPairProduct(a) = -1;

    For a = [10, 2, 2, 4, 30, 35], the output should be
    maxPairProduct(a) = 4.

    Explanation: 4 is a product of 2 and 2.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer a

    Guaranteed constraints:
    1 ≤ a.length ≤ 105,
    1 ≤ a[i] ≤ 104.

    [output] integer
        The greatest element in a such that it is the product of other two elements from a.
"""

def maxPairProduct(A):
    # Create an Empty Dictionary
    H = dict()

    # Add Element(s) of the Array into the Dictionary,
    # Key = Element, Value = Count of Element in Array 
    for N in A: 
        H[N] = H.get(N, 0) + 1

    # Sort the Array
    S = sorted(A)

    # Iterate [i] over the elements of the Array in Reverse Order
    for i in range(len(S) - 1, 0, -1):
        # Iterate [j] from the Beginning of the Sorted Array,
        # While [j] is less than [i],
        # (i.e. the first multiplicand index is less than the product index)
        # and the value of the first multiplicand is less than
        # the square root of the product
        j = 0
        while(j < i and S[j] <= math.sqrt(S[i])): 
            if (S[i] % S[j] == 0):
                # If the Product is Divisible by the First Multiplicand,
                # Divide them to obtain the Second Multiplicand
                R = S[i]//S[j]
                C = H.get(R, 0)

                # If Both the Multiplicands are not the same,
                # Check if the Second Element occurs at least once in the Array
                # But If Both the Multiplicands are same,
                # Check if the Second Element occurs at least twice in the Array
                if R != S[j] and C > 0 or R == S[j] and C > 1:
                    return S[i]

            j += 1
    
    # If there are no two elements in the Array,
    # that can be multiplied to produce another element in the Array, 
    # return -1
    return -1