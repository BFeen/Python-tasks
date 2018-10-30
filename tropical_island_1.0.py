def main(): 
    island = [list(map(int, input().split()))] # Ввод массива массивов
    while len(island) <= 50 and len(island[0]) <= 50:
        rdl = list(map(int, input().split()))
        if rdl == []:
            break
        else:
            island.append(rdl)
    print(get_water_volume(island))

def get_water_volume(island):

    out, used = [], []
    m, n = len(island)-1, len(island[0])-1
    water_volume = 0

    for i in range(1,m):
        for j in range(1,n):
            if (i,j) not in used:
                river = [(i,j)]
                used.append((i,j))
                for x,y in river: # Проверка всех клеток "течения" и формирование списков river и out
                    if y-1 == 0: # слева
                        out.append(island[x][y-1])
                    elif (x,y-1) not in river:
                        if island[x][y-1] <= island[i][j]:
                            river.append((x,y-1))
                        else:
                            out.append(island[x][y-1])

                    if x-1 == 0: # сверху
                        out.append(island[x-1][y])
                    elif (x-1,y) not in river:
                        if island[x-1][y] <= island[i][j]:
                            river.append((x-1,y))
                        else:
                            out.append(island[x-1][y])

                    if y+1 == n: # справа
                        out.append(island[x][y+1])
                    elif (x,y+1) not in river:
                        if island[x][y+1] <= island[i][j]:
                            river.append((x,y+1))
                        else:
                            out.append(island[x][y+1])

                    if x+1 == m: # снизу
                        out.append(island[x+1][y])
                    elif (x+1,y) not in river:
                        if island[x+1][y] <= island[i][j]:
                            river.append((x+1,y))
                        else:
                            out.append(island[x+1][y])

                    if out != []: # если клетка имеет непосредственный выход в море
                        if island[i][j] >= min(out):
                            out.clear()
                            break

                if out !=[]: # после формирования всех списков по ходу течения, заполняем уровень реки
                    for x,y in river:
                        if island[x][y] < min(out):
                            water_volume += min(out) - island[x][y]
                            island[x][y] = min(out)
                            if (x,y) not in used:
                                used.append((x,y))
            out.clear()
    return water_volume

main()