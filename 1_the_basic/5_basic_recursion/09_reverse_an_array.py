'''
You are given an array of integers arr[]. Your task is to reverse the given array.
Note: Modify the array in place.
Examples:
Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.
Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.
'''

class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr) - 1
        mylist = []
        def myReverseArray(arr, index):
            if index == -1:
                return 
            mylist.append(arr[index])
            myReverseArray(arr, index - 1)
        myReverseArray(arr, n)
        
        for i in range(len(mylist)):
            arr[i] = mylist[i]
        return arr
        
        


#{ 
 # Driver Code Starts
import sys


def main():
    # Read the number of test cases
    tc = int(sys.stdin.readline())

    while tc > 0:
        # Read the array elements as a string
        str_arr = sys.stdin.readline().split()

        # Convert the string array to an integer array
        arr = [int(x) for x in str_arr]

        # Create a Solution object
        obj = Solution()

        # Reverse the array
        obj.reverseArray(arr)

        # Print the reversed array
        for i in range(0, len(arr)):
            print(arr[i], end=" ")
        print()
        print("~")

        # Decrement the test case count
        tc -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends