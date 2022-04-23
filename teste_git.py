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