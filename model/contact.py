from sys import maxsize
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None,id=None,
                 address=None, phonehome=None, phonemobile=None, phonework=None,
                 phonefax=None, email=None, bday=None, bmonth=None,byear=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.phonehome = phonehome
        self.phonemobile = phonemobile
        self.phonework = phonework
        self.phonefax = phonefax
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.all_phones_from_home_page=all_phones_from_home_page


        # как будет выглядеть объект при выводе : идентификатор, имя, фамилия
    def __repr__ (self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

        # сравнение объектов логически по именам безусловно и идентификаторам, если они определены
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
            and self.firstname == other.firstname and self.lastname == other.lastname

        # вычислять по контакту ключ используемой для сравнения
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize  # максим. целое число

