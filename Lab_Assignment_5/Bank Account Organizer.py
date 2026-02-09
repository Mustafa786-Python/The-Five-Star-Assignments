accounts = [
    "NYC1045689",
    "NYC2047789",
    "NYC2078689",
    "NYC1045109",
    "NYC3054321",
    "MIA2546689",
    "MIA2244569",
    "MIA2248789",
    "MIA2548989",
    "MIA2045123",
    "LA1012345",
    "LA1023456",
    "LA2034567",
    "LA1019876",
    "LA2023456",
    "CHI1122334",
    "CHI1133445",
    "CHI2123456",
    "CHI2134567",
    "CHI1145678"]

bank_record = {}

# Loop in acccounts
for acc in accounts:
    region = acc[0:3]
    branch = acc[3:5]

    if region not in bank_record:
        bank_record[region] = {}

    if branch not in bank_record[region]:
        bank_record[region][branch] = []

    bank_record[region][branch].append(acc)

for regions, branches in bank_record.items():
    print(f"\nregion: {regions}")

    for branch, acc_list in branches.items():
        print(f"{branch}: {acc_list}")
