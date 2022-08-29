#Error handling

while True:
    try:
        age = int(input('what is your age'))
        10/age
    except ZeroDivisionError:
        print('enter value greater than 0')
        continue
    except ValueError:
        print('Enter a number')
        break
    else:
        print('thank you!!!')
    finally:
        print('you can go now')
    break
def sum(num1,num2):
    try:
        return num1/num2
    except(ZeroDivisionError,TypeError) as err:
        print(err)

print(sum(1,0))
