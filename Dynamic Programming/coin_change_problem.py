"""find the number of ways of making change for a particular number of units using the given types of coins?"""
def getWays(n, c):
    table = [0] * (n + 1)
    table[0]=1
    for coin in c:
        for i in range(coin, n + 1):
                table[i] = table[i]+ table[i - coin]
    print(table[-1])
if __name__ == '__main__':
    n=1#value for which change is to be given by using the coins in the array
    c=[2,5,3,6]#value of coins
    getWays(n,c)
"""There are five ways to make change for  10 units using our coins ."""