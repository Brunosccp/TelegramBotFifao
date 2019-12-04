from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from csvReader import CSVReader

class Predictor:

	model: LinearRegression
	poly_features: PolynomialFeatures


	def __init__(self):
		print("Começo do treinamento")

		data = CSVReader()
		trainingX = data.getXTest()
		trainingY = data.getYTest()

		self.poly_features = PolynomialFeatures(degree=3)
		polyX = self.poly_features.fit_transform(trainingX)

		# fit final model
		self.model = LinearRegression()
		self.model = self.model.fit(polyX, trainingY)
		print("Final do Treinamento")

	def predict(self, player):
		predictX = [[player.overall, player.age, player.position, player.preferredFoot]]
		polyPredictX = self.poly_features.fit_transform(predictX)

		predictY = self.model.predict(polyPredictX)

		print("X=%s, Predicted=%s" % (predictX, predictY))

		return predictY
