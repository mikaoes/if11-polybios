import src_py as src

ch = src.chiffre(10, "polybius") #polybius statt polybios da sonst Buchstaben doppelt vorkommen

code = ch.encrypt("Guten Tag. Wie geht es dir? Ich verschluessele gerne Nachrichten wie Polybios.")
decode = ch.decrypt(code)

print(code)
print(decode)