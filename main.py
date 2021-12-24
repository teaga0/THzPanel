#As apis são enviadas em um grupo para uso free, caso voce seja dono de alguma, entre em contato comigo usando a função "0"

######################
#By Berimbolo & t3ag4#
######################
import os



os.system('pip install requests') or None
os.system('pip install json') or None
os.system('pip install twilio') or None
os.system('pip install Flask') or None
os.system('clear') or None

import time
from flask import Flask
from twilio.rest import Client
import json
import requests

a = "2"
m = "8"
n = "1"
o = "7"




txt2 = """
╔════╦╗░╔╗░░░╔═══╗░░░░░░░░░░ ╔╗╔╗
║╔╗╔╗║║░║║░░░║╔═╗║░░░░░░░░░░░║╠╝╚╗
╚╝║║╚╣╚═╝╠═══╣║░╚╬══╦═╗╔══╦╗╔╣╠╗╔╬══╗
░░║║░║╔═╗╠══║║║░╔╣╔╗║╔╗╣══╣║║║║║║║╔╗║
░░║║░║║░║║║══╣╚═╝║╚╝║║║╠══║╚╝║╚╣╚╣╔╗║
░░╚╝ ╚╝░╚╩═══╩═══╩══╩╝╚╩══╩══╩═╩═╩╝╚╝
######################
#By Berimbolo & t3ag4#
######################\n
"""
b = "+"
c = "5"
d = "5"
e = "5"

txt = """
╔════╦╗░╔╗░░░╔═══╗░░░░░░░░░░ ╔╗╔╗
║╔╗╔╗║║░║║░░░║╔═╗║░░░░░░░░░░░║╠╝╚╗
╚╝║║╚╣╚═╝╠═══╣║░╚╬══╦═╗╔══╦╗╔╣╠╗╔╬══╗
░░║║░║╔═╗╠══║║║░╔╣╔╗║╔╗╣══╣║║║║║║║╔╗║
░░║║░║║░║║║══╣╚═╝║╚╝║║║╠══║╚╝║╚╣╚╣╔╗║
░░╚╝ ╚╝░╚╩═══╩═══╩══╩╝╚╩══╩══╩═╩═╩╝╚╝
######################
#By Berimbolo & t3ag4#
######################

 o que deseja?
[1]ip
[2]cep
[3]cnpj
[4]Numero
[5]IP LOGGER
[6]egg
[0]de uma sugestao ou entre em contato comigo!!!
"""
print(txt)
od = input(":")
 
 

j = "9"
k = "9"
l = "8"

os.system('clear') or None


f = "1"
g = "8"
h = "5"


if od == '1':

  print(txt2)
  pesquisa_ip = input("digite um ip:")
  
  os.system('clear') or None
  
  print(txt2)
  dadosip = requests.get("https://api.ipinfodb.com/v3/ip-city/?key=87da097b47b0b39e30b28ef4f537999ef4ca0fe5b5028626c697ca72d7fedb3b&ip={}&format=json".format(pesquisa_ip))
  dadosip = dadosip.json()
  statuscode = dadosip['statusCode']
  ip = dadosip['ipAddress']
  code = dadosip['countryCode']
  nome = dadosip['countryName']
  estado = dadosip['regionName']
  cidade = dadosip['cityName']
  zipcode = dadosip['zipCode']
  latitude = dadosip['latitude']
  longitude = dadosip['longitude']
  timeone = dadosip['timeZone']
  print("status:{}\nip:{}\ncode:{}\nnome:{}\nestado:{}\ncidade:{}\nzipcode:{}\nlat:{}\nlong:{}\ntimezone:{}".format(statuscode, ip, code, nome, estado, cidade, cidade, zipcode, latitude, longitude, timeone))
 

#o codigo ta bagunçado e com alguns erros, pretendo atualizar.
elif od == '2':

  os.system('clear') or None

  print(txt2)
  pesquisa_cep = input("digite um cep:")

  os.system('clear') or None

  print(txt2)
  dados = requests.get("https://cep.awesomeapi.com.br/json/{}".format(pesquisa_cep))
  dados = dados.json()
  cep = dados['cep']
  rua = dados['address_name']
  estado = dados['state']
  bairro = dados['district']
  latitude = dados['lat']
  longitude = dados['lng']
  cidade = dados['city']
  ibge = dados['city_ibge']
  ddd = dados['ddd']
  print("CEP:{}\nRua:{}\nEstado:{}\nBairro:{}\nLatitude:{}\nLongitude:{}\nCidade:{}\nIBGE:{}\nDDD:{}".format(cep, rua, estado, bairro, latitude, longitude, cidade, ibge, ddd))



elif od == '3':

  print(txt2)
  pesquisa_cnpj = input("Digite um cnpj (sem'.'ou '/' '):\n")

  os.system('clear') or None

  print(txt2)
  dados = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(pesquisa_cnpj))
  dados = dados.json()
  atividade_principal = dados['atividade_principal']
  data_situacao = dados['data_situacao']
  complemento = dados['complemento']
  tipo = dados['tipo']
  nome = dados['nome']
  estado = dados['uf']
  telefone = dados['telefone']
  email = dados['email']
  atividades_secundarias = dados['atividades_secundarias']
  situacao = dados['situacao']
  bairro = dados['bairro']
  logradouro = dados['logradouro']
  numero = dados['numero']
  cep = dados['cep']
  municipio = dados['municipio']
  porte = dados['porte']
  abertura = dados['abertura']
  natureza_juridica = dados['natureza_juridica']
  

  print("ATIVIDADE PRINCIPAL:{}\nDATA SITUAÇAO:{}\nCOMPLEMENTO:{}\nTIPO:{}\nNOME:{}\nESTADO:{}\nTELEFONE:{}\nEMAIL:{}\nOUTRAS ATIVIDADES:{}\nSITUACAO:{}\nBAIRRO:{}\nLOGRADOURO:{}\nNUMERO:{}\nCEP:{}\nMUNICIPIO:{}\nPORTE:{}\nABERTURA:{}\nNATUREZA JURIDICA:{}\n".format(atividade_principal, data_situacao, complemento, tipo, nome, estado, telefone, email, atividades_secundarias, situacao, bairro, logradouro, numero, cep, municipio, porte, abertura, natureza_juridica))



elif od == '4':

  os.system('clear') or None

  print(txt2)

  opc = """Escolha uma opção:
[1]ddd
[2]numero (em breve)""" 
  print(opc)

  opcinp = input(":")

  if opcinp == '1':
    
    os.system('clear') or None
    print(txt2)
    pesquisa_ddd = input("Digite um DDD:\n")

    os.system('clear') or None

    print(txt2)
    dados = requests.get('https://brasilapi.com.br/api/ddd/v1/{}'.format(pesquisa_ddd))
    dados = dados.json()

    state = dados['state']
    cities = dados['cities']

    print("Estado:{}\nCidades:{}".format(state, cities))

elif od == '5':
  os.system('clear')
  app = Flask(__name__)
  print(txt2)
  tft = """Escolha uma opção:
  [1]Local
  [2]em breve..."""
  print(tft)
  iin = input("\n:")
  if iin == '1':
    os.system('clear')
    pers = input('\ndigite uma mensagem personalizada:')
    os.system('clear')
    @app.route('/')
    def home():
      return pers

    app.run(host='0.0.0.0')


elif od == '6':
  print(txt2)
  print('ryan e thales gay kakakajak\n\n\n\n\n\n')



elif od == '0':

  print(txt2)
  contato = input("Digite seu whatsapp ou alguma forma para entrar em contato::\n")
  os.system('clear') or None
  print(txt2)
  nome = input("digite seu nome ou apelido:\n")
  os.system('clear') or None
  print(txt2)
  titulo = input("TITULO da mensagem:\n")
  os.system('clear') or None
  print(txt2)
  mensagem = input("digite a mensagem ou sugestão:\n")
  os.system('clear') or None

  print("Obrigado!!!,um sms foi enviado para mim com a seguinte mensagem:")

  msgrl = """
  ______________
  \ncontato:{}\n
  by: {}\n
  <{}>\n
  {}
  ---------------
  """.format(contato, nome, titulo, mensagem)
  print(msgrl)
  nmr = b + c + d + e + f + j + k + g + h + a + l + m + n + o


  print("\nentrarei em contato em breve!\n")

  account_sid = "AC10c2c35758589419fb170aac051fdba5"
  auth_token = "576b8f20381f39ffabb279eea378f9da"

  Client = Client(account_sid, auth_token)
  Client.messages.create(from_="+19842303432", body="{}".format(msgrl), to ="{}".format(nmr))



else:
  print("a ok")
  
pg = input('\nDeseja fazer uma nova consulta? [sim][nao]')
if pg == 'sim' or pg == 'SIM' or pg == 's' or pg == 'S':
  os.system('clear') or None
  os.system('python main.py') or None
elif pg == 'nao' or pg== 'NAO' or pg== 'n' or pg== 'N':
   varad = "Adeus em 3.."
   print(varad)
   time.sleep(1)
   varad = "Adeus em 32."
   print(varad)
   time.sleep(1)
   varad = "Adeus em 321"
   print(varad, 'fechando..')
   time.sleep(1)
   os.system('clear') or None
else:
   os.system('clear')
   print(txt2, '\n')
   print('tu e burro macaco?')
   time.sleep(2)
   os.system('clear')
   os.system('python main.py')
  