from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/<string:value>', methods=['GET'])
def get_value(value):
	#Recebe o valor como String e trasforma em Inteiro
	value = int(value)
	#Inicializa variavel vazia para armazenar o numero por extenso
	s = ""
	
	#Verifica se o valor passado eh negativo para imprimir o 'menos'
	if(value < 0):
		s = "menos "
		#Transforma o valor em positivo
		value = value * (-1)

	#Verifica se o valor esta acima de mil para imprimir o 'mil' apos a casa da milhar
	if(value >= 1000):
		#Passa para extenso os valores acima da casa da milhar (divisao inteira)
		#antes verifica se eh 'um', se o for, usa-se apenas mil, sem o um
		if(convert(value/1000) != 'um'):
			s = s + convert(value/1000) + " "
		#Adiciona ao final o 'mil e ' para o caso de ter mais numeros na casa da centena, dezena ou unidade
		s = s + "mil e "

	#Verifica se nao ha valores na casa da centena, dezena ou unidade.
	#Caso nao exista, retira o ' e ' apos o mil
	if((value%1000) == 0):
		s = s[:-3]
	#Caso contrario, permanece o ' e ' e adiciona o valor por extenso da centena, dezena e unidade
	else:
		s = s + convert(value%1000)

	#Transforma a saida em json, com a chave 'extenso'
	return jsonify({'extenso': s})


#Metodo convert trabalha com valores de 1 a 999
#int value
#return string s -> valor em extenso
def convert(value):
	#inicializa variavel para retornar o valor por extenso
	s = ""
	#captura o valor da centena
	c = value/100
	#captura o valor da dezena
	d = (value%100)/10
	#captura o valor da unidade
	u = value%10

	#Verifica se o valor da centena eh diferente de zero
	if (c!=0):
		#se for, converte-o e adiciona o ' e ' ao final, como separador
		s = s + convert_centena(c, d, u) + " e "
	
	#Verifica se o valor da dezena eh diferente de zero
	if (d!=0):
		#se for, converte-o e adiciona o ' e ' ao final, como separador
		s = s + convert_dezena(d, u) + " e "
	elif(d==0 and u==0 and c!=0):
		#caso o valor da dezena e da unidade sejam nulos e a centena nao o seja, retira o ' e ' adicionado
		s = s[:-3]

	#Verifica se o valor da unidade eh diferente de zero mas se a dezena eh igual a 1
	if(u!=0 and d==1):
		#Retira o 'e' porque com dezena unitaria o nome dos numeros da unidade nao sao 'lidos' no portugues
		s = s[:-3]
	elif (u!=0 and d!=1):
		#caso a deseja nao seja 1 e a unidade seja diferente de 0, adiciona-se o valor por extenso da unidade
		s = s + convert_unidade(u)
	elif(u==0 and d!=0):
		#caso o valor da unidade seja zero e o da dezena diferente de zero, retira-se o ' e '
		s = s[:-3]
	
	#Retorna o valor por extenso final Centena + Dezena + Unidade
	return s

#Converte o valor da centena para extenso
#int c - centena
#int d - dezena
#int u - unidade
#return string s - valor por extenso
def convert_centena(c, d, u):
	#Se o valor da centena for 1 e unidade e dezena forem 0, entao o numero eh 'cem'
	if(c==1 and d==0 and u==0):
		return "cem"
	#caso o valor da dezena ou da unidade seja diferente de 0, entao le-se como 'cento'
	elif(c==1 and (d!=0 or u!=0)):
		return "cento"
	#todos os demais tem-se apenas uma forma de leitura por extenso
	elif(c==2):
		return "duzentos"
	elif(c==3):
		return "trezentos"
	elif(c==4):
		return "quatrocentos"
	elif(c==5):
		return "quinhentos"
	elif(c==6):
		return "seiscentos"
	elif(c==7):
		return "setecentos"
	elif(c==8):
		return "oitocentos"
	elif(c==9):
		return "novecentos"
	else:
		return ""

#Converte o valor da dezena para seu valor em extenso
#int d - dezena
#int u - unidade
#return string s - Valor por extenso
def convert_dezena(d, u):
	#Verifica-se os casos excepcionais onde a casa da dezena eh igual a 1
	#Nestes casos precisa-se verificar os valores das unidades para poder realizar a conversao
	if(d==1 and u==0):
		return "dez"
	elif(d==1 and u==1):
		return "onze"
	elif(d==1 and u==2):
		return "doze"
	elif(d==1 and u==3):
		return "treze"
	elif(d==1 and u==4):
		return "catorze"
	elif(d==1 and u==5):
		return "quinze"
	elif(d==1 and u==6):
		return "dezesseis"
	elif(d==1 and u==7):
		return "dezessete"
	elif(d==1 and u==8):
		return "dezoito"
	elif(d==1 and u==9):
		return "dezenove"
	#A partir do vinte (dezena igual a 2 em diante), nao ha necessidade do valor da unidade para conversao
	elif(d==2):
		return "vinte"
	elif(d==3):
		return "trinta"
	elif(d==4):
		return "quarenta"
	elif(d==5):
		return "cinquenta"
	elif(d==6):
		return "sessenta"
	elif(d==7):
		return "setenta"
	elif(d==8):
		return "oitenta"
	elif(d==9):
		return "noventa"
	else:
		return ""

#Converte o valor da unidade para seu respectivo valor em extenso
#int u - unidade
#return string s - Valor por extenso
def convert_unidade(u):
	if(u == 0):
		return ""
	elif(u==1):
		return "um"
	elif(u==2):
		return "dois"
	elif(u==3):
		return "tres"
	elif(u==4):
		return "quatro"
	elif(u==5):
		return "cinco"
	elif(u==6):
		return "seis"
	elif(u==7):
		return "sete"
	elif(u==8):
		return "oito"
	elif(u==9):
		return "nove"
	else:
		return ""

#Inicializa o servidor usando o Flask no localhost
if (__name__ == "__main__"):
	app.run(host='0.0.0.0',port = 5000)
