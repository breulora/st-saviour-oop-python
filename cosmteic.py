

class Cosmetic:
    def __init__(self, name: str, shade: str, in_stock: bool):
        self.name = name
        self.shade = shade
        self.in_stock = in_stock

    # you can apply all cosmetics!
    def apply(self, location: str) -> str:
        return f'you apply {self.name} with shade {self.shade} to {location}'
    

if __name__ == '__main__':
    # this is the first instance
    lipliner = Cosmetic('Makeup Forever', '608 Wherever Walnut', True)
    print(lipliner.apply('lips'))

    # this is the second instance
    Mascara = Cosmetic ( 'Milani', 'Black', True)
    print (Mascara.apply('eyelashes'))
