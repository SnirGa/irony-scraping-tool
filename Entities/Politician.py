class Politician:
    def __init__(self,full_name):
        self.first_name=full_name.split(' ')[0]
        self.last_name=full_name.split(' ')[1]
    def __str__(self):
        return self.first_name+' '+self.last_name
