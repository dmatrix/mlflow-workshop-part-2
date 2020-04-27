from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np
import pandas as pd
import mlflow
import mlflow.keras
import warnings
import mlflow.pyfunc

# source: https://androidkt.com/linear-regression-model-in-keras/
# Modified and extended

# Generate X, y data

X_fahrenheit = np.array(
   [-140, -136, -124, -112, -105, -96, -88, -75, -63, -60,
    -58, -40, -20, -10, 0, 30, 35, 48, 55, 69, 81, 89, 95,
    99,105, 110, 120, 135, 145, 158, 160, 165, 170, 175, 180,
    185, 187, 190, 195, 198, 202, 205, 207, 210, 215, 220], dtype=float)

y_celsius = np.array(
   [-95.55, -93.33, -86.66, -80, -76.11, -71.11, -66.66, -59.44, -52.77, -51.11,
    -50, -40, -28.88, -23.33, -17.77, -1.11, 1.66, 8.88, 12, 20,
    27.22, 31.66, 35, 37.22, 40.55, 43.33, 48.88, 57.22, 62.77, 70,
    71.11, 73.88, 76.66, 79.44, 82.22, 85, 86.11,87.77,90.55, 92.22,
    94.44, 96.11, 97.22, 98.88, 101.66, 104.44], dtype=float)

# Define the model
def baseline_model():
   model = Sequential([
      Dense(64, activation='relu', input_shape=[1]),
      Dense(64, activation='relu'),
      Dense(1)
   ])

   optimizer = optimizers.RMSprop(0.001)

   # Compile the model
   model.compile(loss='mean_squared_error',
                 optimizer=optimizer,
                 metrics=['mean_absolute_error', 'mean_squared_error'])
   return model

def mlflow_run(params, run_name="Keras Linear Regression"):

   # Start MLflow run and log everyting...
   with mlflow.start_run(run_name=run_name) as run:
      model = baseline_model()
      # single line of MLflow Fluent API obviates the need to log
      # individual parameters, metrics, model, artifacts etc...
      # https://mlflow.org/docs/latest/python_api/mlflow.keras.html#mlflow.keras.autolog
      mlflow.keras.autolog()
      model.fit(X_fahrenheit, y_celsius, batch_size=params['batch_size'], epochs=params['epochs'])
      run_id = run.info.run_uuid
      exp_id = run.info.experiment_id

      for f in [200, 206]:
         print(f"F={f}; C={model.predict([f])}")

      return (exp_id, run_id)

# Use the model
if __name__ == '__main__':
   # suppress any deprecated warnings
   warnings.filterwarnings("ignore", category=DeprecationWarning)

   params = {'batch_size': 5,
              'epochs': 1000}
   (exp_id, run_id) = mlflow_run(params)
   print(f"Finished Experiment id={exp_id} and run id = {run_id}")

   # Load this Keras Model Flavor as a pyfunc model flavor and make a prediction
   pyfunc_uri = f"runs:/{run_id}/model"
   pyfunc_model = mlflow.pyfunc.load_model(pyfunc_uri)
   print(f"Loading the Keras Model={pyfunc_uri} as Pyfunc Model")
   # Given Fahrenheit -> Predict Celcius
   # Create a pandas DataFrame with Fahrenheit unseen values
   # Get the Celius prediction
   df = pd.DataFrame(np.array([32, 212, 200, 206]))
   pred = pyfunc_model.predict(df)
   print(pred)
