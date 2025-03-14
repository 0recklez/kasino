from random import randint

balance = 2000


def get_attempts(coef):
    attempts = {
        2: 10,
        3: 6,
        5: 3
    }
    return attempts.get(coef, 3)


def calculate_win(bet, coef):
    return bet * coef


def is_valid(arg):
    if arg.isdigit() and (1 <= int(arg) <= 100):
        return True
    else:
        return False


def get_bet(current_balance):
    while True:
        try:
            bet = int(input('введите ставку🤗: '))
            if bet <= 0:
                print("нельзя депать меньше нуля")
            elif bet > balance:
                print("нельзя депнуть больше чем есть на балансе, сначала нужно взять микрозайм")
            else:
                return bet
        except ValueError:
            print('введите целое число')


def get_coef():
    while True:
        try:
            coef = int(input('введите желаемый коэффицент(2, 3, 5): '))
            if coef in {2, 3, 5}:
                return coef
            print("доступные коэффиценты: 2, 3, 5")
        except ValueError:
            print("введите целое число")


def dodep(current_balance):
    print(f"\nваш текущий баланс: {balance}")
    bet = get_bet(balance)
    coef = get_coef()
    hidden_number = randint(1, 100)
    counter = get_attempts(coef)
    return hidden_number, coef, counter, bet


def main():
    global balance
    print("добро пожаловать в казик💸\nвам выпал фрибет 2000🥳🥳 ваш баланс: 2000")
    if input('чтобы посмотреть условия игры введите "условия":  ').lower() == 'условия':
        print('вам нужно угадать число от 1 до 100 за определенное кол-во, попыток\n'
              'чем меньше попыток, тем больше коэффицент')
    if input("чтобы посмотреть доступные коэффиценты введите 'коэф':  ").lower() == 'коэф':
        print("коэффицент 2, кол-во попыток 10\nкоэффицент 3, кол-во попыток 6\nкоэффицент 5👍👍, кол-во попыток 3")
    hidden_number, coef, counter, bet = dodep(balance)
    while True:
        user_number = input('введите число: ')
        if not is_valid(user_number):
            print('введите целое число от 1 до 100😡😡: ')
            continue
        num = int(user_number)
        if num > hidden_number:
            counter -= 1
            print(f'ваше число больше загаданного, осталось попыток: {counter}')
        elif num < hidden_number:
            counter -= 1
            print(f'ваше число меньше загаданного, осталось попыток: {counter}')
        else:
            balance += calculate_win(bet, coef)
            print(f"вы победили, ваш баланс: {balance}")
            if input('если хотите продолжить введите "додеп": ').lower() == 'додеп':
                hidden_number, coef, counter, bet = dodep(balance)
            else:
                break
            continue
        if counter == 0:
            balance -= bet
            if balance <= 0:
                print('вы все проиграли, необходим наисрочнейший додеп')
                break
            print(f'тааак тут без додепа не разобраться🤔🤔\nваш баланс: {balance}')
            if input('если хотите продолжить введите "додеп": ').lower() == 'додеп':
                hidden_number, coef, counter, bet = dodep(balance)
            else:
                break


if __name__ == "__main__":
    main()
