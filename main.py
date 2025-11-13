"""Programme qui permet de tester si un mot est un palindrome"""

#### Fonction secondaire
def ispalindrome(p):
    """Renvoir True ou False si la chaine en paramètre est un palindrome"""
    dico = str.maketrans({"ë": "e","é": "e","è": "e", "É": "e",
                          "ê": "e", "à": "a", "À": "a", ",": "",
                           "'": "", "!": "", "?": "", " ": "",
                         "ô": "o", "-": "", ":": "", "ç": "c"})
    chaine = p.translate(dico)
    final = chaine.lower()
    if final[::]==final[::-1]:
        return True
    return False

#### Fonction principale
def main():
    """Fonction principale qui appel la fonction secondaire isplalindrome"""
    print(ispalindrome("échec"))
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
