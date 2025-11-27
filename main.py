import sys, pygame, random, asyncio, re, time
from datetime import datetime

def choice_pizza(label_print):
    day = datetime.now().day
    month = datetime.now().month
    current_year = datetime.now().year
    surname = patronymic = my_name = email = phone_num = ''

    while (
        not re.search(r'.+\..+', email)
    ): email = input('Email: ')
    while (
        not my_name.istitle()
    ): my_name = input('Имя(C заглавной буквы): ')
    while (
        not surname.istitle()
    ): surname = input('Фамилия(C заглавной буквы): ')
    while (
        not patronymic.istitle()
    ): patronymic = input('Отчество(C заглавной буквы): ')

    while (
        not re.search(r'\D\d+\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
        and not re.search(r'\d+\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
        and not re.search(r'\d+\d\d\d\d\d\d\d\d\d\d', phone_num)
        and not re.search(r'\D\d\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
        and not re.search(r'\d\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
        and not re.search(r'\d\d\d\d\d\d\d\d\d\d\d', phone_num)
    ): phone_num = input('Номер телефона: ')

    while True:
        try:
            my_year = int(input("Ваш год рождения: "))
            if my_year <= current_year - 5 and my_year >= current_year - 200: break
            else: print('\nПроверьте условие ввода числа!\n')
        except ValueError: print('\nНеверный формат данных\n')

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('PIZZA')
    screen = pygame.display.set_mode((800, 600))
    size, pizza_type = 1, 0
    running = string_number = 2
    if my_year <= current_year - 18: running = 1

    pizza_list = (
        (
            'Неаполитанская(1$)',
            'Кальцоне(2$)',
            'Римская(3$)',
            'В нарезке(4$)',
            'Сицилийская(5$)',
            'Кастомная(НОВИНКА!!!)'
        ),
        (
            'Неаполитанская(2$)',
            'Кальцоне(4$)',
            'Римская(6$)',
            'В нарезке(8$)',
            'Сицилийская(10$)',
            'Кастомная(НОВИНКА!!!)'
        ),
        (
            'Неаполитанская',
            'Кальцоне',
            'Римская',
            'В нарезке',
            'Сицилийская',
            'Кастомная:'
        ),
    )

    custom_pizza = [
        0, #meat
        1, #green
        1, #ketchnnaise
        1, #cheese
        1  #mushroom
    ]
    payment = (
        'По карте',
        'Наличкой'
    )
    payment_type = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
                if running == 1:
                    if event.key == pygame.K_LEFT: size = 1
                    elif event.key == pygame.K_RIGHT: size = 2
                    if event.key == pygame.K_RETURN: running = 2

                elif running == 2:
                    if event.key == pygame.K_LEFT and pizza_type > 0: pizza_type -= 1
                    elif event.key == pygame.K_RIGHT and pizza_type < 5: pizza_type += 1
                    if event.key == pygame.K_RETURN:
                        if pizza_type == 5: running = 3
                        else: running = 5

                elif running == 3:
                    if event.key == pygame.K_UP and string_number > 0: string_number -= 1
                    elif event.key == pygame.K_DOWN and string_number < 4: string_number += 1
                    if event.key == pygame.K_LEFT and custom_pizza[string_number] > 0: custom_pizza[string_number] -= 1
                    elif event.key == pygame.K_RIGHT and custom_pizza[string_number] < 9: custom_pizza[string_number] += 1
                    if event.key == pygame.K_RETURN: running = 5
                elif running == 5:
                    if event.key == pygame.K_LEFT: payment_type = 0
                    elif event.key == pygame.K_RIGHT: payment_type = 1
                    if event.key == pygame.K_RETURN: running = 4
                elif running == 4:
                    if event.key == pygame.K_RETURN: running = 0


        screen.fill((0,0,0))

        pizza_total = (
            (1,2,3,4,5, custom_pizza[0] + custom_pizza[1] + custom_pizza[2] + custom_pizza[3] + custom_pizza[4] + 0.5),
            (2,4,6,8,10, custom_pizza[0] + custom_pizza[1] + custom_pizza[2] + custom_pizza[3] + custom_pizza[4] + 0.5)
        )

        if running == 1: label_print(screen, f"Размер пиццы: < {size}м >", (400, 300), (255, 255, 0), True)
        elif running == 2: label_print(screen, f"Какую вам пиццу: < {pizza_list[size-1][pizza_type]} >", (400, 300), (255, 255, 0), True)
        elif running == 3:
            colors_string = [
                (255, 255, 255), (255, 255, 255),
                (255, 255, 255), (255, 255, 255),
                (255, 255, 255)
            ]
            colors_string[string_number] = (255, 255, 0)
            label_print(screen, f"Мяско: < {custom_pizza[0]} >", (400, 240), colors_string[0], True)
            label_print(screen, f"Зелень: < {custom_pizza[1]} >", (400, 270), colors_string[1], True)
            label_print(screen, f"Кетчунез: < {custom_pizza[2]} >", (400, 300), colors_string[2], True)
            label_print(screen, f"Сырочек: < {custom_pizza[3]} >", (400, 330), colors_string[3], True)
            label_print(screen, f"Грибочек: < {custom_pizza[4]} >", (400, 360), colors_string[4], True)
        elif running == 5:
            label_print(screen, f'Способ оплаты < {payment[payment_type]} >', (400, 300), (255, 255, 0), True)
            money = random.uniform(pizza_total[size - 1][pizza_type], (pizza_total[size - 1][pizza_type])*2)
            check = random.randint(0,2000)
        elif running == 4:
            label_print(screen, f"Кассовый чек N{check}", (30, 30), (0, 255, 255), False)
            label_print(screen, f"Тип: {pizza_list[2][pizza_type]}", (30, 60), (0, 255, 255), False)
            if pizza_type == 5:
                label_print(screen, f"    Мяско: {custom_pizza[0]}", (30, 90), (0, 255, 255), False)
                label_print(screen, f"    Зелень: {custom_pizza[1]}", (30, 120), (0, 255, 255), False)
                label_print(screen, f"    Кетчунез: {custom_pizza[2]}", (30, 150), (0, 255, 255), False)
                label_print(screen, f"    Сырочек: {custom_pizza[3]}", (30, 180), (0, 255, 255), False)
                label_print(screen, f"    Грибочек: {custom_pizza[4]}", (30, 210), (0, 255, 255), False)
                if pizza_total[size - 1][5] == 0.5: label_print(screen, "(вам дали пустую лепёшку?)", (400, 240), (0, 255, 0), True)
            if payment_type == 1: label_print(screen, f"Сдача: {money - pizza_total[size - 1][pizza_type]}$", (30, 270), (0, 255, 255), False)
            label_print(screen, f"Способ оплаты: {payment[payment_type]}", (30, 300), (0, 255, 255), False)
            label_print(screen, f"ИТОГО: {pizza_total[size - 1][pizza_type]}$", (30, 330), (0, 255, 255), False)
            label_print(screen, f"Email: {email}", (30, 360), (0, 255, 255), False)
            label_print(screen, f"Phone: {phone_num}", (30, 390), (0, 255, 255), False)
            label_print(screen, f"Год рождения: {my_year}", (30, 420), (0, 255, 255), False)
            label_print(screen, f"ФИО: {surname} {my_name} {patronymic}", (30, 450), (0, 255, 255), False)
            label_print(screen, "Спасибо за покупку! Приходите ещё!", (30, 480), (0, 255, 255), False)
            label_print(screen, f"{day}.{month}.{current_year}", (30, 510), (0, 255, 255), False)


        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

@choice_pizza
def label_print(screen, label, pos, color, center):
    font = pygame.font.Font(None, 34)
    label = font.render(label, True, color)
    if center:
        label_rect = label.get_rect(center = pos)
        screen.blit(label, label_rect)
    else: screen.blit(label, pos)

async def goodbye_print():
    await asyncio.sleep(3)
    print(
        '\n############################\n'
        '#                  ____    #\n'
        '# До свидания! <- / _ _\\   #\n'
        '#                 |  ()|   #\n'
        '#                  \\__/    #\n'
        '############################\n'
    )
async def thank_you():
    await asyncio.sleep(3)
    print(
        '\n####################################\n'
        '#                          ____    #\n'
        '#  Спасибо за покупку! <- / _ _\\   #\n'
        '#                         |  ()|   #\n'
        '#                          \\__/    #\n'
        '####################################\n'
    )

# old
# loop = asyncio.get_event_loop()
# task1 = loop.create_task(goodbye_print())
# task2 = loop.create_task(thank_you())
# loop.run_until_complete(asyncio.wait([task1, task2]))

async def main(): await asyncio.gather(goodbye_print(),thank_you())
asyncio.run(main())

sys.exit()
