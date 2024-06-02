def count_first_letter(names):
    new_dict = {}
    for last_name, first_name in names.items():
        if last_name[0] not in new_dict:
            new_dict[last_name[0]] = len(first_name)
        else:
            new_dict[last_name[0]] += len(first_name)
    return new_dict

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}