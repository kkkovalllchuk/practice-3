from exp_root import root, exponentiation
from factorial import factorial
from logarithm import logarithm

def _main():
    print('-'*20)
    print("Якщо ви хочете знайти факторіал - введіть factorial\nЯкщо корінь квадратний - введіть root2\nЯкщо кубічний - введіть root3\nЯкщо логарифм з певною основою - log\nЯкщо натуральний логарифм - введіть ln\nЯкщо логарифм з основою 10 - lg\nЯкщо квадрат - введіть exp2\nЯкщо куб числа - введіть exp3")
    print('-'*20)
    print("Якщо хочете завершити програму - введіть break")
    print('-'*20)

    while True:
        while True: 
            print('-'*20)  
            a = input("Що ви хочете обчислити?")
    
            if a == "break" or a == "BREAK":
                    print("До побачення!!!!!!!!")
                    break
    
            else:
                if a !='factorial'and  a !='root2' and   a !='root3'and a !='log'and a !='ln' and a !='lg' and  a != 'exp2' and a !='exp3':
                    print("Введені невірні дані.")
                    raise ValueError
                
                if a  == "factorial":
                    b = int(input("Введіть число для якого потрібно знайти факторіал: "))
                    if b < 0:
                        print("Введіть додатне число")
                        raise ValueError
                    else:
                        print("Відповідь: ",factorial.fact(b))
                elif a == "root2":
                    b = float(input("Введіть число для якого хочете знайти корінь: "))
                    if b < 0:
                        print("Введіть додатне число")
                        raise ValueError
                    else:
                        print("Відповідь: ",root.root2(b))
                elif a == 'root3':
                    b = float(input("Введіть число для якого хочете знайти корінь: "))
                    print("Відповідь: ",root.root3(b))
                elif a == 'log':
                    b1 = float(input("Введіть число для знаходження логарифма: "))
                    if b1 < 0:
                        print("Введіть додатне число")
                        raise ValueError
                    b2 = float(input("Введіть основу для логарифма: "))
                    if b2 < 0 or b2 == 1:
                        print("Введіть додатне число")
                        raise ValueError
                    else:
                        print("Відповідь: ",logarithm.log(b2, b1))
                elif a == 'ln':
                    b1 = float(input("Введіть число для якого хочете знайти логарифм: "))
                    if b1 < 0:
                        raise ValueError
                    else:
                        print("Відповідь: ",logarithm.ln(b1))
                elif a == 'lg':
                    b1 = float(input("Введіть число для якого хочете знайти логарифм: "))
                    if b1 < 0:
                        print("Введіть додатне число")
                        raise ValueError
                    else:
                        print("Відповідь: ",logarithm.lg(b1))
                elif a == 'exp2':
                    b = float(input("Введіть число для якого хочете знайти квадрат: "))
                    print("Відповідь: ",exponentiation.exp2(b))
                elif a == 'exp3':
                    b = float(input("Введіть число для якого хочете знайти куб: "))
                    print("Відповідь: ",exponentiation.exp3(b))



if __name__ == '__main__':
    _main()