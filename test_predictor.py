from ai_models.predictor import Predictor

predictor = Predictor()

result = predictor.predict("uploads/faces/face_0.jpg")

print(result)