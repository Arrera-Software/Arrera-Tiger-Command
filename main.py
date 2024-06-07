import argparse 
from Objet.CArreraTiger import* 

def main():
    # Demmarage de l'objet tiger 
    objTiger = CArreraTiger("https://raw.githubusercontent.com/Arrera-Software/Software-debot/main/arrerasoft.json")
    
    # Demarrage Argument 
    parser = argparse.ArgumentParser(description="Arrera Tiger version ligne de commande")
    subparsers = parser.add_subparsers(dest='command')
    # Definition argument install
    parser_install = subparsers.add_parser('install', help='Installer le logiciel')
    # Ajout des arg 
    parser_install.add_argument("-s","--software",type=str,help="logiciel")

    # Verrification des argument
    args = parser.parse_args()
    if (args.command =='install'):
        if (args.software) :
            soft = args.software
            print("Installation de "+soft)
            objTiger.install(soft,soft+".zip","soft")
            print("installation terminer")
        else :
            print("erreur taper help")
    
if __name__ == "__main__":
    main()