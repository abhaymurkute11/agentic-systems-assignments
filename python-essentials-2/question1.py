class StudentMarks:
    
    # Constructor - takes list of marks as input
    def __init__(self, marks):
        self.marks = marks
    
    # Method to calculate average of last 3 marks
    def last_three_avg(self):
        try:
            # Check if less than 3 marks exist
            if len(self.marks) < 3:
                raise ValueError("Not enough marks")
            
            # Negative indexing to get last 3 marks
            last_three = self.marks[-3] + self.marks[-2] + self.marks[-1]
            average = last_three / 3
            
            print("Average of last 3 marks is: " + str(average))
        
        except ValueError:
            print("Not enough marks to calculate average")
