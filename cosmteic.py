

class Cosmetic:
    def __init__(self, name: str, shade: str, in_stock: bool):
        self.name = name
        self.shade = shade
        self.in_stock = in_stock

    def apply(self, location: str) -> str:
        return f'you apply {self.name} with shade {self.shade} to {location}'
    

if __name__ == '__main__':
    lipliner = Cosmetic('Makeup Forever', '608 Wherever Walnut', True)
    print(lipliner.apply('lips'))

if __name__ == '__main__':
    Mascara = Cosmetic ( 'Milani', 'Black', True)
    print (Mascara.apply ('eyelashes'))
