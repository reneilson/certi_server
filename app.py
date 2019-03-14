from flask import Flask
from flask import jsonify

app = Flask(__name__)

#@app.route("/")
#def hello():
#	return "Hello World!"


@app.route('/<string:value>', methods=['GET'])
def get_value(value):
	value = int(value)
	s = ""
	if(value < 0):
		s = "menos "
		value = value * (-1)
	if(value >= 1000):
		s = s + convert(value/1000) + " mil e "
	
	if((value%1000) == 0):
		s = s[:-3]
	else:
		s = s + convert(value%1000)
	return jsonify({'extenso': s})

def convert(value):
	s = ""
	c = value/100
	d = (value%100)/10
	u = value%10
	if (c!=0):
		s = s + convert_centena(c, d, u) + " e "

	if (d!=0):
		s = s + convert_dezena(d, u) + " e "
	elif(c!=0):
		s = s[:-3]

	if (u!=0):
		s = s + convert_unidade(d, u)
	elif(d!=0):
		s = s[:-3]

	return s

def convert_centena(c, d, u):
	if(c==1 and d==0 and u==0):
		return "cem"
	elif(c==1 and (d!=0 or u!=0)):
		return "cento"
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

def convert_dezena(d, u):
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

def convert_unidade(d, u):
	if(d == 1):
		return ""
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
			
		

if (__name__ == "__main__"):
	app.run(host='0.0.0.0',port = 5000)
