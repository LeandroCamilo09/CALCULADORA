import flet as ft
from models import cliquei, ac_func, igual_func, retroceder, operador_porcentagem
import keyboard
import threading

def main(page: ft.Page):
     page.window.width=340
     page.window.height=545
     page.theme_mode="DARK"
     page.window.resizable=False
     page.bgcolor=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=[ft.Colors.AMBER, ft.Colors.AMBER_100],
    )
     page.title="Calculadora"
     page.padding=4
     simb_equal=ft.Text("=",visible=False)
     equacao=ft.Text("", size=16, color="grey")
     resultado=ft.Text("", size=50, weight=ft.FontWeight.W_600)



     cont_qua_res=ft.Column(
          [ft.Row(
               [equacao,simb_equal],
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.END,
               ),
               resultado
               ],
               horizontal_alignment=ft.CrossAxisAlignment.END,
               height=100,
               alignment=ft.MainAxisAlignment.END,
               spacing=0
               )
     
     def escutador_de_teclas():
          def ao_pressionar(tecla):
               nome = tecla.name
               if nome == 'esc':
                    print("Encerrando (ESC).")
                    equacao.value=""
                    resultado.value=""
                    simb_equal.visible=False
                    page.update()
               elif nome in [f"{i}" for i in range(0,10)]:
                    cliquei(equacao=equacao, resultado=resultado, input=nome,page=page, simb_equal=simb_equal)
                    page.update()
               elif nome in [".","+","-","/","*"]:
                    if nome == ",":
                         cliquei(equacao=equacao, resultado=resultado, input=".",page=page, simb_equal=simb_equal)
                         
                    else:
                         cliquei(equacao=equacao, resultado=resultado, input=nome,page=page, simb_equal=simb_equal)
                    page.update()
               
               elif nome in "%":
                    operador_porcentagem(equacao=equacao,page=page)
                    page.update()
               
               elif nome in "=" or nome == "enter":
                    igual_func(equacao=equacao, resultado=resultado, page=page)
                    page.update()
               
               elif nome in "backspace":
                    retroceder(equacao=equacao,page=page)
                    page.update()
               
               else:
                    pass

          keyboard.on_press(ao_pressionar)
          keyboard.wait()  # Mantém o escutador ativo

     # Roda o escutador em segundo plano
     threading.Thread(target=escutador_de_teclas, daemon=True).start()

     numeros=[
          ft.CupertinoButton(content=ft.Text("AC"), 
          bgcolor="#333333", border_radius=5, color="orange", on_click= lambda e :ac_func(e=e,equacao=equacao,resultado=resultado,page=page,simb_equal=simb_equal)),

          ft.CupertinoButton(icon="BACKSPACE_OUTLINED", 
          bgcolor="#333333", border_radius=5, color="white",icon_color="orange", on_click=lambda e: retroceder(e=e, equacao=equacao,page=page)),

          ft.CupertinoButton(content=ft.Text("%"), 
          bgcolor="#333333", border_radius=5, on_click=lambda e: operador_porcentagem(e=e, equacao=equacao,page=page), color="orange"),

          ft.CupertinoButton(content=ft.Text("/"), 
          bgcolor="#333333", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="/",page=page, simb_equal=simb_equal), color="orange"),

          ft.CupertinoButton(content=ft.Text("1"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="1",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("2"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="2",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("3"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="3",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("X"), 
          bgcolor="#333333", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="*",page=page, simb_equal=simb_equal), color="orange"),

          ft.CupertinoButton(content=ft.Text("4"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="4",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("5"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="5",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("6"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="6",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("-", size=30), 
          bgcolor="#333333", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="-",page=page, simb_equal=simb_equal), color="orange"),

          ft.CupertinoButton(content=ft.Text("7"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="7",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("8"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="8",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("9"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="9",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("+", size=30), 
          bgcolor="#333333", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="+",page=page, simb_equal=simb_equal), color="orange"),

          ft.CupertinoButton(content=ft.Text("00"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="00",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("0"), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input="0",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text(","), 
          bgcolor="#444444", border_radius=5, on_click=lambda e: cliquei(e=e, equacao=equacao, resultado=resultado, input=".",page=page, simb_equal=simb_equal), color="white"),

          ft.CupertinoButton(content=ft.Text("=", size=30, text_align=ft.TextAlign.CENTER), bgcolor="orange", border_radius=5, color="black", on_click=lambda e: igual_func(e, equacao=equacao, resultado=resultado, page=page), width=ft.FontWeight.W_100),
          ]

     grid=ft.GridView(
          controls=numeros, 
          runs_count=4,
          spacing=2,
          run_spacing=2,
          child_aspect_ratio=1.25
          )

     app=ft.Column(
          [cont_qua_res,grid],
          expand=True,
          alignment=ft.MainAxisAlignment.END,
          horizontal_alignment=ft.CrossAxisAlignment.END
     )
     page.add(app)
ft.app(target=main)