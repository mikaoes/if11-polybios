import src_py as src

ch = src.chiffre(10, "polybius") #polybius statt polybios da sonst Buchstaben doppelt vorkommen

code = ch.encrypt("Guten Tag. Wie geht es dir? Ich verschluessele gerne Nachrichten wie Polybios.")
decode = ch.decrypt(code)

print(code)
print(decode)

if input("Fortfahren? (y/n) ") == "n": exit()
# Kommunikation zwischen zwei Freunden:
print("\n"*5, "Kommunikation zwischen zwei Freunden:", "\n"*2)

freund1 = src.chiffre(10, "polybius")
freund2 = src.chiffre(10, "informatk")

code = freund1.encrypt("Hast du Morgen Zeit?")
print("Freund2 erhält folgende Nachricht:", freund2.decrypt(code))
print("-> Er hat einen unterschiedlichen Schlüssel, kann die Nachricht also nicht lesen.")

print("Freund2 aktualisiert seinen Schlüssel auf den von Freund1.")
freund2 = src.chiffre(10, "polybius")

print("Freund2 erhält folgende Nachricht:", freund2.decrypt(code))