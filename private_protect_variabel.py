class member:

    __member = []

    def __init__(self, name, clases, no):
        self.__name = name
        self.__calses = clases
        self.__no = no

        self._protect = name
        member.__member.append(name)

    # GETTER
    def get_member(self):
        return self.__member
        
    # SETTER
    def set_member(self, nama):
        return self.__member.append(nama)


alexa = member('alexa', 12, 17)
lux = member('lux', 13, 18)

print(alexa.set_member('adel'))
print(alexa.get_member())
