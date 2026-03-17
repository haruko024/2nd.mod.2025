# Read the file
file = open("codes.txt", "r").read().splitlines()
new_list = []

for x in file:
    new_code = x.split("-")[1].strip()

    if new_code == "0000":
        new_code = "NP"

    new_list.append(new_code)


open("codes.txt", "w").write("\n".join(new_list))
print("Success!")
