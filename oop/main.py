class Soda:

    def __init__(self, taste='regular'):
        self.taste = taste

    def __str__(self):
        return f'You have {self.taste} soda'


soda_taste = Soda()
soda_taste.taste = 'orange'
print(soda_taste)

