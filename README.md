 Managing the Complete Machine Learning Lifecycle with MLflow
=============================================================
![](images/mlflow-workshop.png)
Part 2 of 3
-----------
Other parts:
- [Part 1](https://github.com/dmatrix/mlflow-workshop-part-1)
- [Part 3]()

Content for the MLflow Series
-----------------------------
Machine Learning (ML) development brings many new complexities beyond the traditional software development lifecycle. Unlike in traditional software development, ML developers want to try multiple algorithms, tools and parameters to get the best results, and they need to track this information to reproduce work. In addition, developers need to use many distinct systems to productionize models.

To solve these challenges, [MLflow](https://mlflow.org), an open source project, simplifies the entire ML lifecycle. MLflow introduces simple abstractions to package reproducible projects, track results, 
encapsulate models that can be used with many existing tools, and central respositry to share models,
accelerating the ML lifecycle for organizations of any size.

Goal and Objective
------------------
Aimed at beginner or intermediate level, this three-part series aims to educate data scientists or ML developer in how you 
leverage MLflow as a platform to track experiments, package projects to reproduce runs, use model flavors to deploy in diverse environments, and manage models in a central respository for sharing.

What you will learn
-------------------
Understand the three main components of open source MLflow——MLflow Tracking, MLflow Projects, MLflow Models, and Model Registry—and how each compopnent helps address challenges of the ML lifecycle.
 * How to use [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html) to record and query experiments: code, data, config, and results.
 * How to use [MLflow Projects](https://mlflow.org/docs/latest/projects.html) packaging format to reproduce runs
 * How to use [MLflow Models](https://mlflow.org/docs/latest/models.html) general format to send models to diverse deployment tools.
 * How to use [Model Registry](https://mlflow.org/docs/latest/model-registry.html) for collaborative model lifecycle management
 * How to use [MLflow UI](https://mlflow.org/docs/latest/tracking.html#tracking-ui) to visually compare and contrast experimental runs with different tuning parameters and evaluate metrics


Instructor
-----------

- [Jules S. Damji](https://www.linkedin.com/in/dmatrix/) [@2twitme](https://twitter.com/2twitme) 
---


MLflow workshop part 2
----------------------

In this part 2, we will cover:
 * Concepts and motivation behind MLflow Projects and Models
 * Tour of the the MLflow Project and Model API Documentation
 * MLflow CLI for Projects and APIs
 * Execute MLflow Project locally
 * Build an MLflow Project and share it for reproducible runs
 * Use the MLflow UI on the local host 

Prerequisites
-------------
* [Part 1](https://github.com/dmatrix/mlflow-workshop-part-1) of this series
* Knowledge of Python 3 and programming in general
* Preferably a UNIX-based, fully-charged laptop with 8-16 GB, with a Chrome or Firefox browser
* Familiarity with GitHub, git, and an account on Github
* Some knowledge of Machine Learning concepts, libraries, and frameworks 
     * scikit-Learn
     * pandas and Numpy
     * matplotlib
     * keras/TensorFlow
* PyCharm/IntelliJ or choice of syntax-based Python editor
* pip/pip3 or conda and Python 3 installed
* Knowledge on how to use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) or create [pipenv](https://pypi.org/project/pipenv/) enviroments 
* Loads of virtual laughter, curiosity, and a sense of humor ... :-)

Obtaining the Tutorial Material
--------------------------------

Familiarity with git is important so that you can get all the material easily during the tutorial and
workshop as well as continue to work on in your free time, after the session is over.

``` git clone git@github.com:dmatrix/mlflow-workshop-part-2.git or https://github.com/dmatrix/mlflow-workshop-part-2.git```

Documentation Resources
-----------------------

This tutorial will  refer to documentation: 

1. [MLflow](https://mlflow.org/docs/latest/index.html) 
2. [Numpy](https://numpy.org/devdocs/user/quickstart.html)
3. [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)
4. [Scikit-Learn](https://scikit-learn.org/stable/index.html)
5. [Keras](https://keras.io/optimizers/)
6. [TensorFlow](https://tensorflow.org)
7. [Matplotlib](https://matplotlib.org/3.2.0/tutorials/introductory/pyplot.html)

Installation and Setup environment
----------------------------------

1. ``` git clone git@github.com:dmatrix/mlflow-workshop-part-2.git or git clone https://github.com/dmatrix/mlflow-workshop-part-2.git```
2. `cd <your_cloned_directory>/mlflow-workshop-part-2`
3. Install MLflow and the required Python modules within our conda or pipenv environments if using it
    * `pip install -r req.txt` or `pip3 install -r req.txt`
5. `cd src`
6. If using PyCharm or IntelliJ, create a project and load source files in the project

Let's go!

Session Tutorials
-----------------

We'll use our local host run MLflow projects via GitHub URL

Tutorial 1 - Part 1 
-------------------

Let's run a shell script to run remote MLflow GitHub Project URI.
We will use MLflow CLI [mlflow run [OPTIONS] URI](https://mlflow.org/docs/latest/cli.html#mlflow-run)

[run_project_example_1.sh](src/run_project_example_1.sh)

1. After you've have setup your environment `cd <your_cloned_directory>/mlflow-workshop-part-2/src`
2. ```./run_project_example_1.sh```
3. This will create `./mlruns` directory with experiment ID 0, and all runs under it.

Tutorial 1 - Part 2
-------------------

Let's run the same experiment using MLflow Fluent API.
We will use programmtic interfeace [mlflow.run(...)](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.run)


[run_project_example_1.py](src/run_project_example_1.py)

1. After you've have setup your environment `cd <your_cloned_directory>/mlflow-workshop-part-2/src`
2. ```python run_project_example_1.py```
3. This will create more under the `mlruns` with experiment ID 0, and all new runs under it.
4. Launch MLflow UI to view and compare the runs.
 * `mlflow ui`
 * Got the brower and connect ```http://127.0.0.1:5000```

Tutorial 2 
----------

[run_simple_kerdas_lr.py](src/run_simple_keras_lr.py)

1. After you've have setup your environment `cd <your_cloned_directory>/mlflow-workshop-part-2/src`
2. ```python run_project_example_1.py```
3. This will create more under the `mlruns` with experiment ID 0, and all new runs under it.
4. Launch MLflow UI to view and compare the runs.
 * `mlflow ui`
 * Got the brower and connect ```http://127.0.0.1:5000```
 
 **Note**: We are loading a Keras Model as a pyfunc model and using pandas.DataFrame to do the prediction.
 This demonstrates the capability of model flavors as discussed in the lecture slides.

Homework/Lab Assignment
-----------------------

Using the above as examples:
 * Convert this Keras model or one of the models from the workshop series [Part 1](https://github.com/dmatrix/mlflow-workshop-part-1)
 convert it as a MLflow GitHub Project and execute using different modes of execution demonstrated here.
 * Supply differentarguments as model parameters. 
 * Use MLflow Tracking API for this [TensorFlow/Keras Regression Model](https://www.tensorflow.org/tutorials/keras/regression)
    * Using [mlflow.tensorfow.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.tensorflow.html#mlflow.tensorflow.autolog)

Cheers,
Jules
