f = open("input.txt")
passports = f.read().split("\n\n")
valid_passports = 0
for passport in passports:
    passport_fields = passport.replace("\n", " ").split()
    passport_template = "byriyreyrhgthcleclpid"
    valid = False
    for field in passport_fields:
        field_name = field.split(":")[0]
        if field_name != "cid":
            passport_template = passport_template.replace(field_name, '')
    if passport_template == "" or passport_template == "cid":
        valid_passports += 1
print(valid_passports)
