gamers = []

form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""

def add_gamer(gamer, gamer_list):
    if "name" in gamer and "availability" in gamer:
        gamer_list.append(gamer)


def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

def calculate_availability(gamers_list, available_frequency):
    for name in gamers_list:
        for availability in name["availability"]:
            available_frequency[availability] += 1


def find_best_night(availability_table):
    highest_key_count = ""
    highest_key = 0
    for day, count in availability_table.items():
        if count >= highest_key:
            highest_key_count = day
            highest_key = count
    return highest_key_count

def available_on_night(gamers_list, day):
    people_available = []
    for item in gamers_list:
        if day in item["availability"]: people_available.append(item["name"])
    return people_available

def send_email(gamers_who_can_attend, day, game):
    for person in gamers_who_can_attend:
        print(form_email.format(name=person, day_of_week=day, game=game))

kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

count_availability = build_daily_frequency_table()
calculate_availability(gamers, count_availability)
print(count_availability)

game_night = find_best_night(count_availability)
print(game_night)

attending_game_night = available_on_night(gamers, game_night)
print("Attending: ", attending_game_night)

send_email(attending_game_night, game_night, "Abruptly Goblins!")

unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")