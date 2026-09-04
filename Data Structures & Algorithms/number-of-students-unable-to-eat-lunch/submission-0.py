from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        
        count = 0
        for sandwich in sandwiches:
            if sandwich == students[0]:
                students.popleft()
                count = 0
                
            else:
                student = students.popleft()
                students.append(student)
                count += 1
                if count == len(students):
                    return len(students)
        return len(students)
                

