import requests
import json
import os
import numpy
from cgi import test
import pandas as pd

def day():
    request = requests.get("http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2010&dataFinal=01/03/2021")
    resposta = json.loads(request.content)

    data = ['Data']
    vg = ['valor Ganhos']
    vt = ['valor Total']

    valorInicial = 657.43
    valorTotal = float(valorInicial)
    valorGanho = 0
    count = 0
    print("....................................................................\n")
    for n in resposta:
        count+=1
        valorTotal += valorTotal * (float(n['valor'])/100)
        valorGanho = valorTotal - valorInicial
        if count >= 2:
            print(f"| data:{n['data']: <4} | valor Total:{valorTotal:10.6} | valor Ganho:{valorGanho:10.6} |")
            data.append(n['data'])
            vt.append(format(valorTotal, '.2f'))
            vg.append(format(valorTotal - valorInicial,'.2f'))
  
    obj = []
    obj.append(data)
    obj.append(vt)
    obj.append(vg)

    dia =  pd.DataFrame(obj)
    dia.to_csv('Day.csv', index=False)

    

    print(".....................................................................\n")
    input("\nPRESSIONE ENTER PARA VOLTAR\n")


def month():
    request = requests.get("http://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json&dataInicial=01/01/2010&dataFinal=01/03/2021")
    resposta = json.loads(request.content)

    data = ['Data']
    vg = ['valor Ganhos']
    vt = ['valor Total']

    valorInicial = 657.43
    valorTotal = float(valorInicial)
    count = 0
    year_count = 2010
    month_count = 1

    print(".....................................................................\n")
    for n in resposta:
        count+=1
        valorTotal += valorTotal * (float(n['valor'])/100)

        if count == 1:
            valorGanho = valorTotal - valorInicial
            print(f"| data:{n['data']: <4} | valor Total:{valorTotal:10.6} | valor Ganho:{valorGanho:10.6} |")
            month_count+=1
            count = 0
            data.append(n['data'])
            vt.append(format(valorTotal, '.2f'))
            vg.append(format(valorTotal - valorInicial, '.2f'))
            if month_count == 12:
                year_count+=1
                month_count = 12

    obj = []
    obj.append(data)
    obj.append(vt)
    obj.append(vg)

    mes =  pd.DataFrame(obj)
    mes.to_csv('Month.csv', index=False)
    print(".....................................................................\n")
    input("\nPRESSIONE ENTER PARA VOLTAR\n")

def year():
    request = requests.get("http://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json&dataInicial=01/01/2010&dataFinal=01/03/2021")
    resposta = json.loads(request.content)

    data = ['Data']
    vg = ['valor Ganhos']
    vt = ['valor Total']

    valorInicial = 657.43;
    valorTotal = float(valorInicial)
    count = 0
    year_count = 2010

    print(".....................................................................\n")
    for n in resposta:
        count+=1
        valorTotal += valorTotal * (float(n['valor'])/100)
        if count == 12 :
            valorGanho = valorTotal - valorInicial
            print(f"| data:{n['data']: <4} | valor Total:{valorTotal:10.6} | valor Ganho:{valorGanho:10.6} |")
            year_count+=1
            count = 1
            data.append(n['data'])
            vt.append(format(valorTotal, '.2f'))
            vg.append(format(valorTotal - valorInicial,'.2f'))

    obj = []
    obj.append(data)
    obj.append(vt)
    obj.append(vg)

    ano =  pd.DataFrame(obj)
    ano.to_csv('Year.csv', index=False)       
    print(".....................................................................\n")
    input("\nPRESSIONE ENTER PARA VOLTAR\n")

def period():
    request = requests.get("http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2000&dataFinal=31/03/2022")
    resposta = json.loads(request.content)

    listP = []
    aux = []

    count = 0
    maiorValor = float(0)
    valor = float(0)
    teste = numpy.size(resposta)

    while  teste > 0:
        for n in resposta:
            count+=1
            valor += float(n['valor'])
            listP.append(n['data'])
            if count == 500:
                count = 0
                if valor > maiorValor:
                    aux = listP
                    maiorValor = valor
                
                valor = float(0)
                listP = []

        del resposta[0]
        teste = numpy.size(resposta)
    os.system('cls || clear')
    print("..........................................................................\n")
    print("O periodo mais lucrativo de 500 entre 01/01/2000 a 31/03/2022:")
    print(aux.pop(0))
    print(aux.pop())
    print("..........................................................................\n")
    input("\nPRESSIONE ENTER PARA VOLTAR\n")

def menu():
    os.system('cls || clear')
    print("*-------------------------------------------------*\n"
          "| 1 - Imprimir valores diarios                    |\n"
          "| 2 - Imprimir valores mensais                    |\n"
          "| 3 - Imprimir valores anuais                     |\n"
          "| 4 - Imprimir periodo mais lucrativo (500 dias)  |\n"
          "| 5 - Sair                                        |\n"
          "*-------------------------------------------------*\n\n")

def main():
    while True:
        os.system('cls || clear')
        menu()
        opc = int(input("Informe uma opção: "))
        if opc == 5:
            break
        elif opc == 1:
            print("\nCarregando...")
            day()
        elif opc == 2:
            
            month()
        elif opc == 3:
            
            year()
        elif opc == 4:
            print("\nCarregando...")
            period()
        else:
            print("opção Inválida")

main()