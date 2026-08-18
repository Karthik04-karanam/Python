class College:
    def __init__(self,collegeName,location,courses):
        self.collegeName=collegeName
        self.location=location
        self.courses=courses
c=College("Aditya University","Surampalem",["CSE","ECE","EEE"])
print("College Name:",c.collegeName,"Location:",c.location,"Courses:",c.courses)