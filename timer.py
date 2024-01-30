import sys, time
import sevseg # Импорт программы sevseg.py.
# (!) Можете заменить это значение на любое количество секунд:
secondsLeft = int(input("Введите количество секунд: "))
try:
    while True: # Основной цикл программы.
# Очищаем экран, выводя несколько символов новой строки:
        print('\n' * 60)
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60) # Получаем из модуля sevseg строковые значения для цифр:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
        # Отображаем цифры:
        print(hTopRow +    '   ' + mTopRow +    '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)
        if secondsLeft == 0:
            print()
            print(' * * * * GO * * * *')
            break
        print()
        print('Press Ctrl-C to quit.')
        time.sleep(1) # Вставляем паузу на 1 секунду.
        secondsLeft -= 1
except KeyboardInterrupt:
    sys.exit() # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
