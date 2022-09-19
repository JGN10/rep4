class abuela:
    global var_ab
    global var2 
    var2 = 'definida en la clase abuela'
    var_ab = 'abuelaaaaaa'
    def __init__(self,nombre):
        self.abuela = nombre
    def ab1(self):
        print('en funcion de abuela')
        #print(f'el nombre de la abuela : {self.abuela} ')
        print(f' valor de la variable global abuela: {var_ab} ')

class madre(abuela):
    global var_ma 
    var_ma = 'madreeeeee'
    def __init__(self,nombre):
        self.madre = nombre
    def ma1(self):
        print('en funcion de madre')
       # print(f'el nombre de la madre : {self.madre} ')
        print(f' valor de la variable global madre: {var_ma} ')
        print(f' valor de la variable global abuela: {var_ab} ')
        #print(f'valor de la abuela {self.abuela}' )
        #self.ab1()

class nieta(madre):
    global var_hi 
    var_hi = 'Hijaaaaaaaa'
    def __init__(self,nombre):
        self.hija = nombre
    def hi1(self):
        print('en funcion de hija')
        print(f'el nombre de la hija : {self.hija} ')
        print(f' valor de la variable global hija: {var_hi} ')
        print(f' valor de la variable global madre: {var_ma} ')
        print(f' valor de la variable global abuela: {var_ab} ')
        #print(f'valor de la abuela {self.abuela}' )
        #self.ab1()

class hijo():
    global var_hijo 
    var_hijo = 'Hijooooo'
    def __init__(self,nombre):
        self.hijo = nombre



abuela1 = abuela('Ab_nombre')
abuela1.ab1()
madre1 = madre('MA_nombre')
madre1.ma1()
madre1.ab1()
hija1 = nieta('HI_nombre')
hija1.hi1()
hija1.ma1()


hija1.ab1()
print (f' variable madre global madre {var_ma}')

hijo1 = hijo('hijo_nombre')
print (f' variable madre global hijo {var_hijo}')
print (f' variable definia en la abuela {var2}')
