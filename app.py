from fastapi import FastAPI # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from schema.prediction_response import PredictionResponse
from schema.user_input import UserInput
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

# human readable home endpoint
@app.get('/')
def home():
    return {'message': 'Welcome to the Insurance Premium Prediction API.'}

# machine readable health check endpoint
@app.get('/health')
def health_check():
    return {'status': 'ok',
            'message': 'The API is healthy and ready to accept requests.',
            'version': MODEL_VERSION,
            'model': 'Random Forest Classifier',
            'description': 'This API predicts insurance premium categories based on user input data.',
            'contact': 'For support, contact'}

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }


    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})



