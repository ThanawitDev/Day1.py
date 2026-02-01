total_score = 0
count = 0
with open("note.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        data = clean_line.split(",")
        
        name = data[0]
        number = int(data[1])
        total_score += number
        count += 1  
        
        if number >= 80:
            grade = "A"
        elif number >= 50:
            grade = "B"
        else:
            grade = "F"
        
        print (f" Student: {name} | Score {number} | Grade {grade}")
average_score = total_score / count
print(f"--- Summary ---")
print(f"Average score for this class: {average_score}")