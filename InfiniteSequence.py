def main():
    A = input()
    print(find_sequence(A))

def find_sequence(A):
    seqLen = len(A)+1
    result = 0 

    for size in range(1,seqLen): # порядок числового выражения
        if size == 1 and A[0] == '0':
            continue
        for bias in range(size): # смещение внутри введенной последовательности
            if A[bias] == '0':
                continue
            pos = analysis(size, bias, A)
            if result == 0 and pos != False or pos != False and result > pos:
                result = pos
        if result != 0:
            break
    return result

def analysis(size, bias, sequence): # анализ числа 'sequence'
    firstNum, prevNum, num = 0,0,0
    i = bias
    while i < len(sequence):
        prevNum = num
        if i+size <= len(sequence):
            num = int(sequence[i:i+size])
            if num == 0:
                return False
        else: # если вышли за рамки введенной последовательности
            lastNum = sequence[i:]
            if lastNum[0] == 0:
                return False 
            border = size - len(lastNum)
            lastNum = int(lastNum)
            num = substitution(sequence[i-border:i], lastNum)
                
        if i == bias: # 1-я итерация
            firstNum = num
            if bias > 0: # вычисление предыдущего числа за рамками sequence
                fragment = sequence[0:bias]
                x = str(num - 1)
                if fragment != x[-bias:]:
                    return False    

        elif num - prevNum != 1: # последующие итерации в рамках sequence
            return False

        i += size
        if num == (10**size)-1: # случай, когда следующее число - на порядок выше
            size+=1

    return position(firstNum)-bias

# метод восстановления недостающего фрагмента
def substitution(previous, fragment): 
    size = 10**len(previous)
    if int(previous) < size-1:
        return fragment*size + int(previous)+1
    else:
        return fragment*size

# подсчет первого вхождения числа number в бесконечную последовательность
def position(number): 
    size = len(str(number))
    pos = 0
    for i in range(1,size):
        pos += 9*(i*10**(i-1))
    bias = number - 10**(size-1)
    return pos+(bias*size)+1

main()