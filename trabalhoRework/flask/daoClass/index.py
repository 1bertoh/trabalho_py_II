import json
import os
from daoClass import InteractFile

class Avatar():
    # def __init__(self):
    #     self.avatar_list = self.interactFile([], InteractFile.READ)
    #     self.__initialMenu()

    #def __Crud ():
    
    def interactFile(self, avatares_list: list, action: InteractFile) -> list:
        """Pass a empty list if you want just read the file"""
        self.__root_path = os.path.abspath(".\\")
        print(self.__root_path)

        with open(f'{self.__root_path}\\data\\data.json', action.value, encoding='utf-8') as file:
            if action.value == "r":
                return self.__readingList( file )
            elif action.value == "w+":
                self.__createDeleteUpdate(self, avatares_list, file)

    def __initialMenu(self):
        if len(self.avatar_list) > 0:
            self.__menuHasAvatar()
        else:
            self.__menuHasNotAvatar()

    def __menuHasAvatar():
        """Render on screen a menu telling that the usar has avatar created"""
        print()

    def __menuHasNotAvatar():
        """Render on screen a menu telling that the usar has not avatar created"""
        print()


    def __readingList(self, avatares):
        """Return the avatar list"""
        lista = json.load(avatares)

        return lista

    def __createDeleteUpdate(self, avatares_list: list, file):
        data = json.dumps(avatares_list)
        file.write(data)
        file.close()
        """Makes a update/append on the data based on the passed list change """
        print()

teste = Avatar()
# teste.interactFile(InteractFile.READ)
