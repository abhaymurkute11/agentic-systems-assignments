class StudentScores:
    
    # Constructor - takes list of scores as input
    def __init__(self, scores):
        self.scores = scores
    
    # Method to find highest among last 2 scores
    def highest_last_two(self):
        try:
            # Check if less than 2 scores exist
            if len(self.scores) < 2:
                raise ValueError("Not enough scores")
            
            # Negative indexing to get last 2 scores
            second_last = self.scores[-2]
            last        = self.scores[-1]
            
            # Find highest among the two
            if second_last > last:
                highest = second_last
            else:
                highest = last
            
            print("Highest score among last two is: " + str(highest))
        
        except ValueError:
            print("Not enough scores to find highest value")