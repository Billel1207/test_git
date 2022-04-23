a = a + 5
b=b+2

a +b


class math():
    def avg(self, list_):
        sum_ = sum(list_)
        n = len(list_)
        average = sum_ / n
        return average
test1 = [10, 20, 30, 40, 50]
instance = math()

print('la moyenne de la liste est {}'.format(instance.avg(test1)))

class Imput():
    def __init__(self,la_liste):
        self.chiffre_liste = la_liste

    def Moyenne(self):
        somme_des_nombres = 0
        Positions_des_None = []

        for x in range(len(self.chiffre_liste)):
            if self.chiffre_liste[x] is None:
                Positions_des_None.append(x)
            else:
                somme_des_nombres+=self.chiffre_liste[x]
        for x in Positions_des_None:
            self.chiffre_liste[x] = somme_des_nombres / (len(self.chiffre_liste)-len(Positions_des_None))

        return self.chiffre_liste