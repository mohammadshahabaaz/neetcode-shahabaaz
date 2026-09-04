from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        
        sandwichIndex = 0
        count = 0
        
        while students and sandwichIndex < len(sandwiches):
            if sandwiches[sandwichIndex] == students[0]:
                students.popleft()
                sandwichIndex += 1
                count = 0
                
            else:
                student = students.popleft()
                students.append(student)
                count += 1
                if count == len(students):
                    return len(students)
        return len(students)
                

