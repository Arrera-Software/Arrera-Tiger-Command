import argparse 
from Objet.CArreraTiger import*
from tkinter import filedialog 

def main():
    # Demmarage de l'objet tiger 
    objTiger = CArreraTiger("https://raw.githubusercontent.com/Arrera-Software/Software-debot/main/arrerasoft.json")
    listSoft = objTiger.listSoft()
    # Ouverture du fichier de config
    fileConfig = jsonWork()
    fileConfig.loadFile("tigerConfig.json")
    # Demarrage Argument 
    parser = argparse.ArgumentParser(description="Arrera Tiger version ligne de commande")
    subparsers = parser.add_subparsers(dest='command')
    # Definition argument install
    parser_install = subparsers.add_parser('install', help='Installer le logiciel')
    # Ajout des arg 
    parser_install.add_argument("-s","--software",type=str,help="logiciel")
    # Deffinition de la command liste
    paser_list = subparsers.add_parser('list',help='liste des logiciel')
    # Deffinition de la command config
    parser_config = subparsers.add_parser('config',help="commande qui permet de configurer l'emplacement des logiciel installer")
    # Verrification des argument
    args = parser.parse_args()
    if (args.command =='install'):
        file = fileConfig.lectureJSON("file")
        if (args.software) :
            if (file==""):
                print("Selectionner l'emplacement ou les logiciel doivent etre installer en tapant 'config'")
            else :
                soft = args.software
                print("Installation de "+soft)
                objTiger.install(soft,soft+".zip",file)
                print("installation terminer")
        else :
            print("erreur taper help")
    else :
        if (args.command=='list'):
            nb = len(listSoft)
            print("Liste des logiciel : ")
            if(nb==1):
                print("- "+listSoft[0])
            else :
                for i in range(0,nb):
                    print("- "+listSoft[i]+"\n")
        else :
            if (args.command=='config'):
                print("Selectionner le dossier")
                folder = filedialog.askdirectory(title="Sélectionner un dossier")
                fileConfig.EcritureJSON("file",folder)
                print("Emplacement configurer")


    
if __name__ == "__main__":
    main()