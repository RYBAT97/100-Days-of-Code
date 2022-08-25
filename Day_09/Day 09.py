# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."
# }
#
# # programming_dictionary.
# print(programming_dictionary['Bug'])

# ------------------------------------------------------------------

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }
#
# student_grades = {}
#
# for key in student_scores:
#     if 91 <= student_scores[key] <= 100:
#         student_grades[key] = "Outstanding"
#     elif 81 <= student_scores[key] <= 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif 71 <= student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
#
# print(student_grades)

# -----------------------------------------------------------------

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 8
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
#     }
# }

# -----------------------------------------------------------------

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(country_name, visit_count, cities_list):
    travel_log.append({
        "country": country_name,
        "visits": visit_count,
        "cities": cities_list
    })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
