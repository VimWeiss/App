from flet import *

def main(page:Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#0f0636'
    PINK = '#eb06ff'
    TEXCOL = 'white'
    
    tasks = Column()
    
    categories_card = Row(
        scroll='auto',
    )
    
    categories = ['Работа', 'Семья', 'Друзья']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=35,
                bgcolor=BG, 
                height=110, 
                width=190,
                padding=15,
                content=Column(
                    controls=[
                        Text('Задания в категории', color=TEXCOL),
                        Text(category, color=TEXCOL),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=i*30),
                            content=Container(bgcolor=PINK),
                        )
                    ]
                )
            )
        )
    
    first_page_contents=Container(
        content=Column(controls=[
            Row(alignment='spaceBetween',
                controls=[
                    Container(
                        content=Icon(icons.MENU)),
                    Row(
                        controls=[
                            Icon(icons.SEARCH),
                            Icon(icons.NOTIFICATIONS_OUTLINED),
                        ]
                    )
                ]
            ),
            Container(height=20),
            Text(value='Привет Вадим!', color=TEXCOL),
            Text(value='КАТЕГОРИИ', color=TEXCOL),
            Container(padding=padding.only(top=10, bottom=20),
                      content=categories_card,),
            Text('ЗАДАНИЯ НА СЕГОДНЯ', color=TEXCOL),
            Stack(controls=[
                tasks,
                FloatingActionButton(
                    icon = icons.ADD, on_click= lambda _: page.go('/create_task')),
            ])
        ])
    )
    
    page_1 = Container()
    page_2 = Row(controls=[Container(
                                width=400,
                                height=850,
                                bgcolor=FG,
                                border_radius=35,
                                padding=padding.only(top=50, left=20,right=20, bottom=5),
                                content=Column(controls=[
                                    first_page_contents
                                ])
                                )  
                           ]
                 )
    
    container = Container(width=400, 
                          height=850, 
                          bgcolor=BG,
                          border_radius=35,
                          content=Stack(
                              controls=[
                                  page_1,
                                  page_2
                              ]
                          )
                          )
    page.add(container)
    

app(target=main)
