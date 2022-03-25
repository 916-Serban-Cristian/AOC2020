def validate_height(height):
    if "cm" in height:
        good_height = int(height.replace("cm", ""))
        if good_height in range(150, 194):
            return True
    elif "in" in height:
        bad_height = int(height.replace("in", ""))
        if bad_height in range(59, 77):
            return True
    return False


def validate_hair_colour(hair_colour):
    if hair_colour[0] != "#":
        return False
    else:
        hair_digits = hair_colour.replace("#", "")
        if len(hair_digits) != 6:
            return False
        for digit in hair_digits:
            if digit not in "0123456789" and digit not in "abcdef":
                return False
    return True


f = open("input.txt")
passports = f.read().split("\n\n")
valid_passports = 0
for passport in passports:
    passport_fields = passport.replace("\n", " ").split()
    passport_template = {"byr": lambda year: int(year) in range(1920, 2003),
                         "iyr": lambda year: int(year) in range(2010, 2021),
                         "eyr": lambda year: int(year) in range(2020, 2031),
                         "hgt": validate_height,
                         "hcl": validate_hair_colour,
                         "ecl": lambda eye_colour: eye_colour in "amb blu brn gry grn hzl oth",
                         "pid": lambda passport_id: len(passport_id) == 9,
                         "cid": lambda country_id: True}
    valid = True
    for field in passport_fields:
        field_name, field_contents = field.split(":")[0], field.split(":")[1]
        if not passport_template[field_name](field_contents):
            valid = False
            break
        passport_template.pop(field_name)
    if len(passport_template) == 1 and "cid" not in passport_template or len(passport_template) > 1:
        valid = False
    if valid:
        valid_passports += 1
print(valid_passports)
