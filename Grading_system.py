student_scores = {
    "Harry": 99,
    "Chandana": 45,
    "Neha": 89,
    "Aman": 76,
    "Nikhil": 23
}

for key in student_scores:
    if student_scores[key] in range(91, 100):
        print(f"{key} : Outstanding")
    elif student_scores[key] in range(81, 90):
        print(f"{key}: Exellent")
    elif student_scores[key] in range(71, 80):
        print(f"{key}: Acceptable")
    else:
        print(f"{key}: Fail")
