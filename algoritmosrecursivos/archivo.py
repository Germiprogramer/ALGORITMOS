def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

l = ["", "", "", "", "", "", ""]

def patocamina(n):
    if n<len(l):
        l[n] = "pato"
        try: 
            l[n-1] = ""
        except:
            pass
        print(l)
        patocamina(n+1)
    

patocamina(0)
    



