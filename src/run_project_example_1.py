import mlflow
import warnings

#
# Short example how to run a MLflow GitHub Project programmatically using
# MLflow Fluent APIs https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.run
#

if __name__ == '__main__':

   # suppress any deprcated warnings
   warnings.filterwarnings("ignore", category=DeprecationWarning)
   ml_project_uri = "git://github.com/mlflow/mlflow-example.git"
   parameters = [{'alpha': 0.3},
                 {'alpha': 0.4},
                 {'alpha': 0.5}]

   # Iterate over three different runs with different parameters
   for param in parameters:
      print(f"Running with param = {param}"),
      res_sub = mlflow.run(ml_project_uri, parameters=param)
      print(f"status={res_sub.get_status()}")
      print(f"run_id={res_sub.run_id}")

