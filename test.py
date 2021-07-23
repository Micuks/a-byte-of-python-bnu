forbidden = (';',':',',',' ','.')
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
upper = tuple(upper)
lower = 'qwertyuiopasdfghjklzxcvbnm'
lower = tuple(lower)
def intolower(char):
    return lower[upper.index(char)]

def process(strin):
    for i in strin:
        if i in forbidden:
            del(strin[strin.index(i)])
            process(strin)
        if i in upper:
            strin[strin.index(i)] = intolower(i)
            process(strin)
            
def reverse(strin):
    return strin[::-1]

def ispalindrome(strin):
    return strin == reverse(strin)

if __name__ == '__main__':
    # stri = list(input('Enter a string:'))
    # print(upper,lower)
    stri = list('Rise to vote, sir.')
    originstring = stri
    originstring = ''.join(originstring)
    process(stri)
    # stri = ''.join(stri)
    # print(stri)
    if ispalindrome(stri):
        print(originstring, 'is a palindrome')
    else:
        print(originstring, 'is not a palindrome')
    print('Done')
