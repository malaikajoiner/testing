
class square:
    def square(self, n):
        squared = n**2
        print (squared)
        return squared

if __name__ == '__main__':
    sq = square()
    x = (input("num?"))
    x = int(x)
    sq.square(x)
