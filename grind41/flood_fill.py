"""Step1

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        stack = []
        stack.append((sr, sc))
        visited = set()

        while stack:
            cx, cy = stack.pop()

            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + x, cy + y
                if nx < 0 or n <= nx:
                    continue
                if ny < 0 or m <= ny:
                    continue
                if (nx, ny) in visited:
                    continue
                if image[nx][ny] != image[sr][sc]:
                    continue
                stack.append((nx, ny))
            
            image[cx][cy] = image

        return image