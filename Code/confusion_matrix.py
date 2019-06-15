def calcAcuracia(matriz):
	acuracia = (matriz[0][0] + matriz[1][1])/(matriz[0][0] + matriz[1][1] + matriz[0][1] + matriz[1][0])*100
	print(f"\nAcuracia: {acuracia:.2f} %")

def calcRecall(matriz):
	recall = (matriz[0][0])/(matriz[0][0] + matriz[1][0])*100
	print(f"Recall: {recall:.2f} %")


def calcPrecisao(matriz):
	precisao = (matriz[0][0])/(matriz[0][0] + matriz[0][1])*100
	print(f"Precisao: {precisao:.2f} %")


def calcFScore(matriz):
	fscore = ((((matriz[0][0])/(matriz[0][0] + matriz[0][1]) * (matriz[0][0])/(matriz[0][0] + matriz[1][0])) *2)/ ((matriz[0][0])/(matriz[0][0] + matriz[0][1]) + (matriz[0][0])/(matriz[0][0] + matriz[1][0]))) * 100
	print(f"FScore: {fscore:.2f} %")



	'''

				positivo(predito) negativo(predito)

	positivo		 PP					PN
	negativo		 NP					NN

	PP -> Valores positivos que o modelo determinou como positivo
	PN -> Valores positivos que o modelo determinou como negativo
	NP -> Valores negativos que o modelo determinou como positivo
	NN -> Valores negativos que o modelo determinou como negativo

	Acuracia -> % dos valores testados que modelo conseguiu acertar
	Recall -> % dos valores positivos que o modelo acertou no total de positivos das amostras testadas
	Precisao -> % dos valores positivos que o modelo acertou no total de positivos que ele indicou
	FScore -> média harmonica do Recall e da Precisao, quanto maior, maior a confiabilidade da acuracia (não entendi direito saporra)


	'''