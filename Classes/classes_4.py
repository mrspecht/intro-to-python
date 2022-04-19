# Classes

class Students:
    students = []

    def __init__(self, *names):
        self.names = list(names)

    def enroll(self):
        self.students = self.names

    def __str__(self):                                                          # Python version of toString()
        return f"{len(self.students)} students are enrolled in this course"


course = Students("Jack Smith", "Bob Draven", "Steve George")
course.enroll()
print(course.students)
print(course)
                                                                                # '__dict__' is a dictionary or other mapping object used
print(course.__dict__)                                                          # to store an object’s (writable) attributes
