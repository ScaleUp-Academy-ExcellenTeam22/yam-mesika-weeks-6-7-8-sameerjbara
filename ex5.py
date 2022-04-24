class User:
    """A User  class. Allows managing users .

       Parameters
       ----------
       user_name : str
           name of the user.
       password : str
           password of the user.
       user_type : str
           ype of user (manager/regular user).
       Attributes
       ----------
      user_name : str
           name of the user.
      password : str
           password of the user.
      user_type : str
           ype of user (manager/regular user).
       """

    def __init__(self, user_name, password, user_type):
        self.user_name = user_name
        self.password = password
        self.user_type = user_type

    def __str__(self):
        return f"user name:{self.user_name} user type:{self.user_type}"


class File:
    """A FIle class. Allows creating Basic Files .

           Parameters
           ----------
           size : int
               size of the file.
           content : str
               the content of the file.
           creator : User
               the creator of the file.
           Attributes
           ----------
           size : int
                size of the file.
           content : str
               the content of the file.
           creator : User
               the creator of the file.
           """

    def __init__(self, size, content, creator):
        self.size = size
        self.content = content
        self.creator = creator

    def __str__(self):
        return f"file size:{self.size} file content:{self.content} file creator:{self.creator}"


class TextFile(File):
    """A TextFIle class. Allows creating text Files .

               Parameters
               ----------
               size : int
                   size of the file.
               content : str
                   the content of the file.
               creator : User
                   the creator of the file.
               Attributes
               ----------
              size : int
                   size of the file.
               content : str
                   the content of the file.
               creator : User
                   the creator of the file.
               """

    def count(self, string):
        """:returns how many time the string appeared in the file content.
                Parameters
                ----------
                string : str
                    The searched string.
                Returns
                -------
                int
                    number of the appearance of the string.
                Raises
                ------
                KeyError
                    none.
                """
        return str(self.content).count(string)

    def read(self, user):
        """:returns the content of the file
        only of the requesting user is the creator or the manager  of the file
                        Parameters
                        ----------
                        user : User
                            The requesting User .
                        Returns
                        -------
                        string
                            content of the file.
                        Raises
                        ------
                        KeyError
                            none.
                        """
        return self.content if user == self.creator or user.user_type == "manager" else None


class BinaryFile(File):
    """A BinaryFIle class. Allows creating Binary Files .

                   Parameters
                   ----------
                   size : int
                       size of the file.
                   content : str
                       the content of the file.
                   creator : User
                       the creator of the file.
                   Attributes
                   ----------
                  size : int
                       size of the file.
                   content : str
                       the content of the file.
                   creator : User
                       the creator of the file.
                   """

    def get_dimensions(self):
        pass

    def read(self, user):
        """:returns the content of the file
                only of the requesting user is the creator or the manager  of the file
                                Parameters
                                ----------
                                user : User
                                    The requesting User .
                                Returns
                                -------
                                string
                                    content of the file.
                                Raises
                                ------
                                KeyError
                                    none.
                                """
        return self.content if user == self.creator or user.user_type == "manager" else None


class FolderFile(File):
    """A folder class. Allows creating folders.

                   Parameters
                   ----------
                   size : int
                       size of the file.
                   content : str
                       the content of the file.
                   creator : User
                       the creator of the file.
                   Attributes
                   ----------
                  size : int
                       size of the file.
                   content : str
                       the content of the file.
                   creator : User
                       the creator of the file.
                   """
    pass
