#
# shell script to run GitHub Project using CLI
#
# Iterate over different values for the parameters
#
for var in 0.3 0.4 0.4
do
   echo "Running with alpha=$var"
   mlflow run https://github.com/mlflow/mlflow-example -P alpha=$var
done
s
