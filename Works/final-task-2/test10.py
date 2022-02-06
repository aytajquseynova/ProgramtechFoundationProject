users = []

menu = """
      Qeydiyyatdan kecmek ucun [1] yazin: \n 
      Sisteme daxil olmaq ucun [2] yazin: \n
      Ana menuye qayitmaq ucun [3] yazin: \n
      Sistemden cixmaq ucun [4] yazin: \n
      """
print(menu)
choice = int(input('Seciminizi daxil edin: '))

class User:
    def _init_(self,username,password):
        self.username=username
        self.password=password
        
    def show_user(self):
        print(f'{self.username} siz artiq qeydiyyatdan kecmisiniz')

while True:
    if choice == 1:
        username=input('Istifadeci adiniz: ')
        password=input('Parolunuz: ')
        
        user = User(username, password)  
        users.append(username)
        
        print('Ugurla qeydiyyatdan kecdiniz!')
        choice = int(input('Seciminizi daxil edin: '))     
    if choice==2:
        username=input('Istifadeci adiniz: ')
        password=input('Parolunuz: ')
        user = User(username,password)
        if username in users:
           user.show_user()
        elif user not in users:
           print('Qeydiyyatdan kecmemisiniz!')
        choice = int(input('Seciminizi daxil edin: '))
    if choice == 3:
        print(menu) 
        choice = int(input('Seciminizi daxil edin: '))

    if choice ==4:
       break