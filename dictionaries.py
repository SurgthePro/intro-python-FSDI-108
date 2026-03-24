# Dictionaies store data in KEY: VALUE pairs.
# written with curly brackets {}.

student = {
    "name" : "Sergio",
    "age" : "46",
    "major" : "Computer Science"
}
print(student)

# Accessing Items:
print(student["name"])
print(student.get("major"))

#Adding Items:
student["graduation_year"] = 2025 # the new item is added as the end of the dictionary.
print(student)

#Changing Values:
student["age"] = 40
print(student)

#Removing Items:
student.pop("major") # Removed the KEY:VALUE
print(student)

#Check IF  a key exists:
if "name" in student:
    print("Key 'name' exists in the dictionary!")

#Nested Dictionaries:
students = {
    "student1" : {"name": "Sergio", "age": 46},
    "student2" : {"name": "Lucy", "age" : 22}
    }
print(students["student2"]["age"]) # Accessing nested values.


"""
MINI-CHALLENGE: Student Report Card
YOu need to store and analyze a student's grades.
1. Create a dictionary called "report_card" with keys:
    -"name"
    -"subject"
    -"grades" (use a tuple with 3 numbers)
# Example: {"name": "Leo", ... "grades": (90, 95, 88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (Hint: use sum() and len()).
4. Add a new key called "average" with the calculated result.
5. If the averagee is 90 or above -> print "EXCELLENT!"
    iF between 70 & 89, print "Good Job!"
    otherwise, print "Needs improvement."
6. Remove the "subject" key and print the updated dictionary.
"""

report_card = {
    "name": "Sergio",
    "subject": "FSDI",
    "grades": (90, 95, 85)
}
print(f"Student: {report_card["name"]}, Subject: {report_card["subject"]}")
print(report_card["subject"])

report_card["average_grade"] = sum(report_card["grades"]) / len(report_card["grades"]) 

if report_card["average_grade"] >= 90:
    print("Excellent!")
elif report_card["average_grade"] >= 70:
    print("Great Job!")
else:
    print("Needs improvement.")
report_card.pop("subject")
print(report_card)

# The following code is for assignment 2b:
# Create a dictionary with key:value pairs:
activity = {
    "first_activity": "unit intro",
    "second_activity": "teach strategy",
    "third_activity": "teach skill"
}
print(activity)
# Accessing values using keys:
print(activity["first_activity"]) # This accesses the first item value.
print(activity.get("third_activity")) # This access the third item value.
# Adding new keys:
activity["fourth_activity"] = "teach vocabulary" # This adds a new key:pair item at the end of the dictionary.
print(activity)
# Updating existing values:
activity["first_activity"] = "unit wrap-up" # This modifies/undates the first item in the dictionary.
print(activity)
# Removing keys:
activity.pop("fourth_activity") # This removes a specific key:value pair.
print(activity)

# Printing the dictionary and its length:
print(f"Activities dictionary: {activity} has a length of: {len(activity)} activities altogether.")

# Note: I personally found dictionaries to be somewhat practical/applicable/useful.