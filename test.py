snelheid = float(input("Beginsnelheid meteoriet (m/s): "))

resolutie = 0.5  # meetnauwkeurigheid telescoop (m/s)

tijd = 0


vorige_meting = snelheid

verschil = 1

while verschil > 0.2:
    # fysische evolutie (deterministisch)
    snelheid += 9.81
    snelheid *= 0.95

    verschil = snelheid - vorige_meting

    tijd += 1

    vorige_meting = snelheid


print(f"De meteoriet haalde een topsnelheid van {round(snelheid,2)} m/s na {tijd} seconden.")