attempt_results = [0.72, 0.81, 0.86, 0.93, 0.94]
threshold = 0.9
max_attempts = 11

attempt = 1

while attempt <= max_attempts and attempt <= len(attempt_results):

    print(f"Attempt {attempt}: accuracy = {attempt_results[attempt-1]}")

    if attempt_results[attempt-1] >= threshold:
        print(f"Training Succeeded : {attempt_results[attempt-1]}")
        break
    
    attempt += 1