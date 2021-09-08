def maior_primo(k):

    primos = []
    for i in range(k+1):
        count = 0
        for j in range(k+1):
            if i%(j+1) == 0: 
                count += 1
        if count == 2:
            primos.append(i)

    return(max(primos))
print(maior_primo(5))