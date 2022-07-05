#!/usr/bin/python3
"""
Creation of the console of the web application
"""

import cmd
from models.base_model import BaseModel
import global_usage
from global_usage import *
from models import storage
import models
import shlex
import json
# print(global_usage.classes)
# print(global_usage)
# print(global_usage.City)


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """
        La fonction emptyline est appelée lorsqu'une ligne vide
        est entré en réponse à l'invite.
        Une ligne vide est renvoyée par l'interpréteur
        si une déclaration est fournie et qu'elle n'a pas de contenu.
        La fonction ne fait rien.

        :param self : référence l'instance de l'objet lui-même
        :retour: Aucun
        :doc-author: Trelent
        """
        pass

    def do_EOF(self, line):
        """
        La fonction do_EOF est appelée lorsque
        l'utilisateur saisit EOF (End of File).
        Cette fonction est utilisée pour sortir du programme.

        :param self : accède aux variables appartenant à la classe
        :param line : Passe la ligne saisie par l'utilisateur
        :return : la chaîne &quot;return&quot;
        :doc-author: Trelent
        """
        print()
        return True

    def do_quit(self, line):
        """
        La fonction do_quit est appelée lorsque
        l'utilisateur entre la commande 'quit'.
        Il imprime un message puis termine le programme.

        :param self : Accéder aux attributs de la classe
        :param line : Transmet la commande saisie par
        l'utilisateur à la fonction
        :return : une chaîne &quot;quitter la session
        :doc-author: Trelent
        """
        return True

    def do_create(self, className):
        """
        La fonction do_create crée une nouvelle instance
        de la classe spécifiée.
        Il l'enregistre ensuite dans le fichier JSON et imprime
        le numéro d'identification de l'objet nouvellement créé.

        :param self : référence les attributs
        et les méthodes de la classe dans laquelle il est appelé
        :param className : crée une nouvelle instance de la classe
        :return : L'identifiant de l'instance nouvellement créée
        :doc-author: Trelent
        """

        if not className:
            print("** class name missing **")
        try:
            newClass = eval(className)()
            print(newClass.id)
            newClass.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        La fonction do_show affiche une instance
        d'une classe en fonction du nom et de l'identifiant de la classe.

        :param self : Accéder aux attributs et méthodes de la classe
        :param line : stocke l'entrée de l'utilisateur
        :return: Les attributs et valeurs de l'objet
        :doc-author: Trelent
        """
        if line in ["", None]:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{words[0]}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        La fonction do_destroy supprime une instance
        basé sur le nom et l'identifiant de la classe.

        :param self : référence la classe elle-même
        :param line : Passez la ligne de commande
        arguments de la fonction
        :return : Vrai si la commande destroy
        est réalisé avec succès
        :doc-author: Trelent
        """
        if not line:
            print("** class name missing ** ")
            return False
        data = shlex.split(line)
        print(data)
        if data[0] not in global_usage.classe:
            print("** class doesn't exist **")
            return False
        if len(data) == 1:
            print("** instance id missing **")
            return False
        classNameId = f"{data[0]}.{data[1]}"
        if classNameId not in models.storage.all():
            print("** no instance found **")
            return False
        del models.storage.all()[classNameId]
        models.storage.save()

    def do_all(self, line):
        """
        La fonction do_all imprime tous les objets stockés.


        :param self : référence la classe elle-même
        :param line : Transmettez les arguments
        de la ligne de commande à la fonction do_all
        :retour: Une liste de tous les objets stockés
        :doc-author: Trelent
        """

        list_args = shlex.split(line)
        if len(list_args) > 0 and list_args[0] not in classe:
            print("** class doesn't exist **")
        else:
            list_result = []
            for key, value in storage._FileStorage__objects.items():
                if len(list_args) == 0:
                    list_result.append(str(value))
                elif list_args[0] == value.to_dict()["__class__"]:
                    list_result.append(str(value))
            print(list_result)

    def do_update(self, line):
        """
        La fonction do_update met à jour une instance
        basé sur le nom et l'identifiant de la classe
        en ajoutant ou en mettant à jour un attribut
        (enregistrez la modification dans le fichier JSON).


        :param self : Accès aux attributs et méthodes de la classe
        :param line : Passe la ligne saisie par l'utilisateur
        :return : la valeur renvoyée par la fonction setattr
        :doc-author: Trelent
        """

        print(line)
        if not line:
            print("** class name missing ** ")
            return False
        data = shlex.split(line)
        print(data)
        if data[0] not in global_usage.classe:
            print("** class doesn't exist **")
            return False
        lendata = len(data)
        if lendata == 1:
            print("** instance id missing **")
        else:
            strLine = f"{data[0]}.{data[1]}"
            if strLine not in models.storage.all():
                print("** no instance found **")
                return False
            if lendata == 2:
                print("** attribute name missing **")
                return False
            if lendata == 3:
                print("** value missing **")
                return False
        setattr(models.storage.all()[strLine], data[2], data[3])
        models.storage.save()

    def do_count(self, line):
        """
        La fonction do_count compte le nombre d'instances d'une classe.
            Si aucun argument n'est passé,
            il compte toutes les instances dans le stockage.
            Sinon, il compte toutes les instances correspondant à l'argument.

        :param self : Accéder aux attributs et méthodes de la classe
        :param line : Vérifie si l'utilisateur a entré un nom de classe
        :return : le nombre d'instances de la classe spécifiée
        :doc-author: Trelent
        """

        count = 0
        if line:
            list_args = shlex.split(line)
            for key, value in storage._FileStorage__objects.items():
                if value.__class__.__name__ == list_args[0]:
                    count += 1
        else:
            for _ in storage._FileStorage__objects.keys():
                count += 1
        print(count)

    def default(self, line):
        """
        Update a command interpreter by default
        """
        array = line.split(".")
        if array[0] in HBNBCommand.classes:
            if array[1] == "all()":
                return self.do_all(array[0])
            if array[1] == "count()":
                return self.do_count(array[0])
            if array[1][:4] == "show":
                new_array = array[1].split("(")
                new_new_array = new_array[1].split(")")
                new_arg = f"{array[0]} {new_new_array[0]}"
                return self.do_show(new_arg)
            if array[1][:7] == "destroy":
                new_array = array[1].split("(")
                new_new_array = new_array[1].split(")")
                new_arg = f"{array[0]} {new_new_array[0]}"
                return self.do_destroy(new_arg)
            if array[1][:6] == "update":
                new_array = array[1].split("(")
                new_new_array = new_array[1].split(")")
                ar = new_new_array[0].split(",")
                new_arg = f"{array[0]} {ar[0]} {ar[1]} {ar[2]}"
                return self.do_update(new_arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
