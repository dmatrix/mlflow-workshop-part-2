import mlflow
import warnings
import mlflow.pyfunc
import pandas as pd
import numpy as np

#
# Short example how to run a MLflow GitHub Project programmatically using
# MLflow Fluent APIs https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.run
#

if __name__ == '__main__':

   # Suppress any deprcated warnings
   warnings.filterwarnings("ignore", category=DeprecationWarning)
   params = {'batch_size': 10, 'epochs': 1000}
   ml_project_uri = "git://github.com/dmatrix/mlflow-workshop-project-expamle-1.git"

   # Iterate over three different runs with different parameters
   print(f"Running with param = {params}")
   res_sub = mlflow.run(ml_project_uri, parameters=params)
   print(f"status={res_sub.get_status()}")
   print(f"run_id={res_sub.run_id}")

   # Load this better Keras Model with TF 2.x Flavor as a pyfunc model flavor and make a prediction
   pyfunc_uri = f"runs:/{res_sub.run_id}/model"
   pyfunc_model = mlflow.pyfunc.load_model(pyfunc_uri)
   print(f"Loading the Keras Model={pyfunc_uri} as Pyfunc Model")


   # Given Fahernheight -> Predict Celcius
   # Create a pandas DataFrame with Fahrenheit unseen values
   # Get the Celius prediction
   df = pd.DataFrame(np.array([32, 212, 200, 206]))
   pred = pyfunc_model.predict(df)
   print(pred)

