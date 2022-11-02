#Time_Complexity: O(m*n) 
#Space_Complexity : O(m*n)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix) # lenght of rows
        n = len(matrix[0]) # lenght of columns
        
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        
        result = []  # Create a empty array
        
        while left<=right and top<=bottom:  # Run until left less than right and top less than bottom
            #Left to Right
            for i in range(left, right+1):
                result.append(matrix[top][i]) # Append the values in the result array as matrix[top][i]
            top +=1 # increment top by 1
            #Top to Bottom    
            for j in range(top, bottom+1):  
                result.append(matrix[j][right]) # Append the values in the result array as matrix[j][right]
            right-=1
            
            if len(result) == m*n:  # if the length of result is equal to m*n
                break
            
            #Right to Left
            for k in range(right, left-1, -1):
                result.append(matrix[bottom][k]) # Append the values in the result array as matrix[bottom][k]
            bottom -=1
                
            #Bottom to Top
            for l in range(bottom,top-1, -1):
                result.append(matrix[l][left])  #Append the values in the result arry as matrix[l][left]
            left+=1
                
        return result   # return result
