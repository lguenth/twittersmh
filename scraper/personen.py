# @ Zeichen weglassen, damit auch Erwähnungen in Ergebnissen auftauchen und nicht nur Tweets der Person selbst
personen = ["Suli Kurban", "CJahnz", "frauenvondamals",
            "ellebil", "isi_peazy", "KKadro", "augustaschacht", "Maria Dragus", "Nora Hespers", "LydiaAemilia", "fraunora", "Luna Wedler", "jorinde_wiese", "fraaanie"]

for person in personen:
    query = f"ichbinsophiescholl AND {person}"
