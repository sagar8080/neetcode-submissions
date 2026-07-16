class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp = 0

        while fp < len(numbers):
            find = target - numbers[fp]
            lp = numbers.index(find) if find in numbers else -1
            
            if lp > fp:
                return [fp+1, lp+1]
            
            fp += 1