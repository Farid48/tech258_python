# Dictionaries

# Key = Value pairs

student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "setup","collections"]
}

print(student1["completed_lesson_names"][0])
student1["completed_lessons"] = 3
print(student1["completed_lessons"])
student1["completed_lesson_names"].remove("collections")
print(student1["completed_lesson_names"])

print(student1.keys())

story1 = {
    "start": "There was once a hero who lived in the quiet mountains. He possesssed immense strength and was known by the townsfolk",
    "middle": "A beast came to the town and destroyed everything",
    "end": "The hero killed the beast but died in the process",
}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["start"])
print(story1["middle"])
print(story1["end"])

story1.update({"hero": "Strong_guy"})
print(story1.keys())


