courses = [
    {"title": "Python 101", "students": 45},
    {"title": "Database Design", "students": 12},
    {"title": "Web Development", "students": 85},
    {"title": "Cyber Security", "students": 30},
    {"title": "Artificial Intelligence", "students": 62}
]
total_budget = 0
for course in courses :
    if course["students"] >= 60:
        course["size"] = "Large"
        course["cost"] = 15000 
    elif course["students"] >= 30:
        course["size"] = "Medium"
        course["cost"] = 10000
    else:
        course["size"] = "Small"
        course["cost"] = 5000
    total_budget += course["cost"]

print (f"Current Courses Informaton: {courses} ")
print (f"Total Budget is {total_budget}")