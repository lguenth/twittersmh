medien = ["uebermedien", "bwr", "BR_Presse",
          "SWRpresse", "herstory_pod", "bpb", "WDDD"]

for medium in medien:
    query = f"ichbinsophiescholl AND {medium}"
    print(query)