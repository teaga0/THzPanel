import json
import requests
import os
import time

os.system('pip install requests') or None
os.system('pip install json') or None
os.system('clear') or None


txt = """
╔════╦╗░╔╗░░░╔═══╗░░░░░░░░░░ ╔╗╔╗
║╔╗╔╗║║░║║░░░║╔═╗║░░░░░░░░░░░║╠╝╚╗
╚╝║║╚╣╚═╝╠═══╣║░╚╬══╦═╗╔══╦╗╔╣╠╗╔╬══╗
░░║║░║╔═╗╠══║║║░╔╣╔╗║╔╗╣══╣║║║║║║║╔╗║
░░║║░║║░║║║══╣╚═╝║╚╝║║║╠══║╚╝║╚╣╚╣╔╗║
░░╚╝ ╚╝░╚╩═══╩═══╩══╩╝╚╩══╩══╩═╩═╩╝╚╝

 o que deseja?
[1]ip
[2]cep
[3]cnpj"""
print(txt)
od = input(":")
 
os.system('clear') or None

if od == '1':
  pesquisa_ip = input("digite um ip:")
  
  os.system('clear') or None

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
 

elif od == '2':

  os.system('clear') or None

  pesquisa_cep = input("digite um cep:")

  os.system('clear') or None

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
  pesquisa_cnpj = input("Digite um cnpj (sem'.'ou '/' '):\n")

  os.system('clear') or None

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
else:
  print("a ok")
  
pg = input('Deseja fazer uma nova consulta? [sim][nao]')
if pg == 'sim':
  os.system('clear') or None
  os.system('python main.py') or None
elif pg == 'nao':
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