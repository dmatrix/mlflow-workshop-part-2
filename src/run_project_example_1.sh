#
# shell script to run GitHub Project using CLI, supplying
# different parameters alpha values.
# ElasticNet uses both Ridge and Lasso combined for regularization
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html
#
# Iterate over different values for the alpha parameters
#
for var in 0.3 0.4 0.5
do
   echo "Running with alpha=$var"
   mlflow run https://github.com/mlflow/mlflow-example -P alpha=$var
done
