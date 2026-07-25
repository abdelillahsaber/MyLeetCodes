class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water = 0
        while left <= right:
            b = right - left
            h = min(height[left],height[right])
            water = max(water,b*h)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return water
