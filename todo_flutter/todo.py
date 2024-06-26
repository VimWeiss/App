from flet import *
from custom_checkbox import CustomCheckBox

def main(page:Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#0f0636'
    PINK = '#ed0c79'
    TEXCOL = 'white'
    
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(0.8, alignment=alignment.center_right)
        page_2.update()
    
    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page_2.update()
    
    #Навигация по приложению
  

    create_task_view = Container(
        content=Container(on_click= lambda _: page.go('/'),
            height=40, 
            width=40,
            content=Text('x'),)
    )
    

    #Создание категорий
    
    tasks = Column(
        height=400,
        scroll='auto',
        #controls=[Container(height=50, width=300, bgcolor='red'),
        #          Container(height=50, width=300, bgcolor='red'),
        #          Container(height=50, width=300, bgcolor='red'),
        #          Container(height=50, width=300, bgcolor='red'),],
        
    )
    
    for i in range(10):
        tasks.controls.append(
            Container(height=50, 
                      width=400, 
                      bgcolor=BG, 
                      border_radius=25, padding = padding.only(left=15, top=13),
                      content=CustomCheckBox(PINK, label='Введите запись',),)
        )
    
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
    
    #Главная страница с контентом
    first_page_contents=Container(
        content=Column(controls=[
            Row(alignment='spaceBetween',
                controls=[
                    Container(on_click=lambda e: shrink(e),
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
                FloatingActionButton(bottom=60, right=20,
                    icon = icons.ADD, on_click= lambda _: page.go('/create_task')),
            ])
        ])
    )
    
    page_1 = Container()
    page_2 = Row(alignment='end',
                controls=[Container(
                                width=400,
                                height=850,
                                bgcolor=FG,
                                border_radius=35,
                                animate = animation.Animation(600, AnimationCurve.DECELERATE),
                                animate_scale = animation.Animation(400, curve='decelerate'),
                                padding=padding.only(top=50, left=20,right=20, bottom=5),
                                content=Column(controls=[
                                    first_page_contents
                                ])
                                )  
                           ]
                 )
    
    container = Container(width=400, 
                          height=750, 
                          bgcolor=BG,
                          border_radius=35,
                          content=Stack(
                              controls=[
                                  page_1,
                                  page_2
                              ]
                          )
                          )
    
    
    pages = {'/':View("/",[container],),
             '/create_task':View("/create_task", [create_task_view],)
             }
    
#    def route_change():
#        page.views.clear()
#        page.views.append(
#           View(
#                "/",
#                [container],
#            )
#        )
        
    def route_change(route):
        page.views.clear()
        page.views.append(
           pages[page.route]
        )  
        
    page.add(container)
    
    page.on_route_change = route_change
    page.go(page.route)

app(target=main)
