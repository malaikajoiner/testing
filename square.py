import sys
class square:
    def square(self, n):
        squared = n**2
        print (squared)
        return squared

if __name__ == '__main__':
    sq = square()
    x = int(sys.argv[1])
    sq.square(x)
