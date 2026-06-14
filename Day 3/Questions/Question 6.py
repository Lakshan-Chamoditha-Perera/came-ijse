scores  = [ 0.91, 0.88, None, 0.95, 0.25, 0.72, 0.81]

valid_scores  = []
processed_count = 0

for score in scores:
    processed_count += 1
    if score is None:
        continue
    if score < 0.3:
        print("Critical anomally detected")
        break
    valid_scores.append(score)
    
print("Valid scores: ", valid_scores)
print("Number of processed items: ", processed_count)