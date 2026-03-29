class StudentPerformance:
    
    # Constructor - takes list of scores as input
    def __init__(self, scores):
        self.scores = scores
    
    # Method to find difference between last and first score
    def score_difference(self):
        try:
            # Check if list is empty
            if len(self.scores) == 0:
                raise ValueError("No scores available")
            
            # Indexing to get first and last score
            first_score = self.scores[0]
            last_score  = self.scores[-1]
            
            # Calculate difference
            difference = last_score - first_score
            
            print("Difference between last and first score is: " + str(difference))
        
        except ValueError:
            print("No scores available to calculate difference")

