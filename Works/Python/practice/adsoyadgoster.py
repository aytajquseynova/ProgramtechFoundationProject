class Student:
    def __init__(self, ad, soyad,email):
        self.ad=ad
        self.soyad=soyad
        self.email=email
    def adGoster(self):
        print(self.ad)
    def adsoyadGoster(self):
        print(f'{self.ad}---{self.soyad}')    
    def emailCheck(self):
         if '@' in self.email:
             print('email duzgun daxil edilib')
         else:
             print('email duzgun daxil edilmeyibdir')   
a=Student('Aytac', 'Huseynova', 'aytajquseynova@gmail.com') 
b=Student('Lyaman', 'Macidli', 'macidovalaman.com')   
a.emailCheck()                             