Your task is to complete the function printPat which takes one argument 'n' denoting the length of the pattern and prints the following pattern
for n=2 the pattern will be 
2 2 1 1
2 1
for n=3 the pattern will be 
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1

Input:
The first line of input is the number of test cases .  The T test cases follow . The first line of each test case is an integer N.

Output:
For each test case print the required pattern in a single line . 
Note : Instead of printing new line print a "$" without quotes.

Constraints:
1<=T<=20
1<=N<=40

Example:
Input
1
2
3
Output
2 2 1 1 $2 1 $
3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $


{
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        print (printPat(n))
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

def printPat(n):
    #Code here
    result = ""
    for i in range(n,0,-1):
        t = []
        for j in range(n,0,-1):
            t.extend([str(j)]*i)
        result+=" ".join(t)
        result+=" $"
    return result
        
