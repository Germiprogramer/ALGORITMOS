def warping_path(z):

    resultado = (z[0])[0]
    i=0
    j=0
    total=1
    
    while i<=(5) or j<=(5):
        print("El camino pasa por la posición ({},{})".format(i,j))
        try:
            if (z[i+1])[j]<(z[i+1])[j+1] and (z[i+1])[j]<(z[i])[j+1]:
                resultado=resultado+(z[i+1])[j]
                i=i+1
                j=j
                total=total+1
            elif (z[i])[j+1]<(z[i+1])[j+1] and (z[i])[j+1]<(z[i+1])[j]:
                resultado=resultado+(z[i])[j+1]
                i=i
                j=j+1
                total=total+1
            else:
                resultado=resultado+(z[i+1])[j+1]
                i=i+1
                j=j+1
                total=total+1
        except:
            break
    else:
        pass

    if i < (5-1):
        resultado=resultado+(z[i+1])[j]
        total=total+1
    if j < (5-1):
        resultado=resultado+(z[i])[j+1]
        total=total+1
