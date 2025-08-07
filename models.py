import numexpr
import keyboard


t_sinais=0
t_num=0
operadores=["+","-","/","*"]
def cliquei(e=any,equacao=any,resultado=any,input=any,page=any,simb_equal=any):
     global t_num, t_sinais, operadores
     simb_equal.visible=True
     if equacao.value == "" and not input in operadores:
          equacao.value+=input
          t_num+=1
          page.update()
     elif equacao.value == "" and input in operadores:
          equacao.value=f"0{input}"
          t_num+=1
          t_sinais+=1
          page.update()
     elif not equacao.value == "":
          if equacao.value[-1] in operadores and input in operadores:
               nova_equacao=equacao.value[:-1]+(input)
               equacao.value=nova_equacao
               page.update()
          else:
               equacao.value+=input
               t_num+=1
               page.update()
               if t_num>=2 and input in operadores:
                    resultado.value=numexpr.evaluate(equacao.value[:-1]).item()
                    page.update()

def ac_func(e=any, equacao=any, resultado=any, page=any, simb_equal=any):
     equacao.value=""
     resultado.value=""
     simb_equal.visible=False
     page.update()

def igual_func(e=any, equacao=any, resultado=any, page=any):
     if equacao.value[-1] in operadores:
          resultado.value=numexpr.evaluate(equacao.value[:-1]).item()
     else:
          resultado.value=numexpr.evaluate(equacao.value).item()
     page.update()

def retroceder(e=any, equacao=any, page=any):
     if equacao.value=="":
          pass
     else:
          nova_equacao=equacao.value[:-1]
          equacao.value=nova_equacao
          page.update()

def operador_porcentagem(e=any, equacao=any, page=any):
     if equacao.value=="":
          pass
     else:
          nova_equacao=f"{equacao.value[:-1]}{float(equacao.value[-1])*0.01}"
          equacao.value=nova_equacao
          page.update()

