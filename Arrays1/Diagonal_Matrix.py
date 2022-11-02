#Time_Complexity: O(m*n) 
#Space_Complexity : O(m*n)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat) # length of the rows
        n = len(mat[0]) #length of the columns
        result = [0]* (m*n) # Create an array with 0 for m*n
        flag = 1    
        index = 0
        
        r = 0
        c = 0
        
        while index<len(result):    # Run until the length of result
            result[index] = mat[r][c]   # Assign result[index] with matrix[rows][column]
            
            if flag == 1:   # if flag is 1
                if c == n-1:    # if index is in the last column
                    r+=1 # increment row by 1
                    flag = -1 # Change the flag to -1
                elif r == 0:    # if the index is in the fitst row
                    c+=1 # increment column by 1
                    flag = -1 # change the flag to -1
                else:
                    r-=1 # decrement row by 1
                    c+=1 # increment column by 1
            else:   
                if r == m-1: # if index is in the last row
                    c+=1 # increment column by 1
                    flag = 1 # change the flag to 1
                elif c == 0: # if the index is in the first column
                    r+=1 # increment the row by 1
                    flag = 1 # change the flag to 1
                else:
                    r+=1 # increment row by 1
                    c-=1 # decrement the column by 1
            index+=1 # increment the index by 1  
        return result   # return result
