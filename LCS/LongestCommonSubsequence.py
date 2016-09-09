# *-* coding: utf-8 *-*
# author: Guangzhan


# return longest common sub sequence c and b
def LCS_Length(x, y):
    m = len(x)
    n = len(y)

    b = [[0] * n for i in range(m)]
    c = [[None for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m+1):
        c[i][0] = 0
    for j in range(0, n+1):
        c[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = "↖"

            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "↑"

            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "←"
    return c, b


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"
    c1, b1 = LCS_Length(x, y)
    for c2 in c1:
        print(c2)
    print("\n********\n")
    for b2 in b1:
        print(b2)
