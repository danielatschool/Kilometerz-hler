km_stand_vorher = float(input("Geben Sie den Kilometerstand beim vorherigen Tanken ein: "))
km_stand_jetzt = float(input("Geben Sie den Kilometerstand beim jetzigen Tanken ein: "))

tankmenge_liter = float(input("Geben Sie die getankte Menge in Litern ein: "))  
verbrauch = (tankmenge_liter / (km_stand_jetzt - km_stand_vorher)) * 100

print(f"Der durchschnittliche Verbrauch beträgt {verbrauch:.2f} Liter pro 100 Kilometer.")