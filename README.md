 Managing the Complete Machine Learning Lifecycle with MLflow
=============================================================
![](images/mlflow-workshop.png)
Part 2 of 3
-----------
Other parts:
- [Part 1](https://github.com/dmatrix/mlflow-workshop-part-1)
- [Part 3](https://github.com/dmatrix/mlflow-workshop-part-3)

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
Understand the four main components of open source MLflow——MLflow Tracking, MLflow Projects, MLflow Models, and Model Registry—and how each compopnent helps address challenges of the ML lifecycle.
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

```git clone git@github.com:dmatrix/mlflow-workshop-part-2.git or git clone https://github.com/dmatrix/mlflow-workshop-part-2.git```

Documentation Resources
-----------------------

This tutorial will refer to documentation: 

1. [MLflow](https://mlflow.org/docs/latest/index.html)
3. [Numpy](https://numpy.org/devdocs/user/quickstart.html)
4. [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)
5. [Scikit-Learn](https://scikit-learn.org/stable/index.html)
6. [Keras](https://keras.io/optimizers/)
7. [TensorFlow](https://tensorflow.org)
8. [Matplotlib](https://matplotlib.org/3.2.0/tutorials/introductory/pyplot.html)

Installation and Setup environment
----------------------------------

1. ```git clone git@github.com:dmatrix/mlflow-workshop-part-2.git or git clone https://github.com/dmatrix/mlflow-workshop-part-2.git```
2. `cd <your_cloned_directory>/mlflow-workshop-part-2`
3. Install MLflow and the required Python modules within your [conda activated environment](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) or [pipenv environment](https://pypi.org/project/pipenv) if using it
    * `pip install -r req.txt` or `pip3 install -r req.txt`
5. `cd src`
6. If using PyCharm or IntelliJ, create a project and load source files in the project
7. [How to use PyCharm and MLflow](https://www.youtube.com/watch?v=yzn1hNkQuWA&feature=youtu.be)

Let's go!

Session Tutorials
-----------------

We'll use localhost (or your laptop) to run MLflow projects via GitHub URL, as experiment runs.

Tutorial 1 - Part 1 
-------------------

Let's run a shell script to run remote MLflow GitHub Project URI.
We will use MLflow CLI [mlflow run [OPTIONS] URI](https://mlflow.org/docs/latest/cli.html#mlflow-run)

[run_project_example_1.sh](src/run_project_example_1.sh)

1. 1. Let's visit what it looks like...
 * [MLflow Project: Wine Example](https://github.com/mlflow/mlflow-example)
2. After you've have setup your environment `cd <your_cloned_directory>/mlflow-workshop-part-2/src`
3. Run the shell script using MLfow CLI
    * ```./run_project_example_1.sh```
    * This will create `./mlruns` directory and logs all runs under it.
4. Check the source for this MLflow Git Hub Project
 * Launch this in the browser: [MLflow Project Wine Example](https://github.com/mlflow/mlflow-example)
5. Launch MLflow UI to view and compare the runs.
 * `mlflow ui`
 * Got the brower and connect ```http://127.0.0.1:5000```

Tutorial 1 - Part 2
-------------------

Let's run the same experiment using MLflow Fluent API.
We will use programmtic interfeace [mlflow.run(...)](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.run)

[run_project_example_1.py](src/run_project_example_1.py)

1. After you've have setup your environment `cd <your_cloned_directory>/mlflow-workshop-part-2/src`
2. Run the python script 
 * ```python run_project_example_1.py```
 * This will create `./mlruns` directory and log all runs under it.
4. Launch MLflow UI to view and compare the runs.
 * `mlflow ui`
 * Got the brower and connect ```http://127.0.0.1:5000```

Tutorial 2 - Part 1
-------------------

[run_simple_kerdas_lr.py](src/run_simple_keras_lr.py)

1. After you've have setup your environment `cd <your_cloned_directory>/mlflow-workshop-part-2/src`
2. Let's look at the source and see what's we doing...
 * load into your favorite editor or PyCharm
2. ```python run_project_example_1.py``` or run it from PyCharm
3. This will create `./mlruns` directory and log all runs under it.
4. Launch MLflow UI to view and compare the runs.
 * `mlflow ui`
 * Got the brower and connect ```http://127.0.0.1:5000```
 
 **Note**: We are loading a Keras Model as a pyfunc model and using pandas.DataFrame to do the prediction.
 This demonstrates the capability of model flavors as discussed in the lecture slides.
 
 Tutorial 2 - Part 2
 -------------------
 This is the same example as above in Tutorial 2 (part 1) but converted into an MLflow Project
1. Let's visit what it looks like... 
 * [MLflow Project: Keras Example](https://github.com/dmatrix/mlflow-workshop-project-expamle-1)
1. After you've have setup your environment `cd <your_cloned_directory>/mlflow-workshop-part-2/src`
2. Run with default paramerters
   * ```mlflow run git@github.com:dmatrix/mlflow-workshop-project-expamle-1.git```
3. Run with parameters
   * ```mlflow run git@github.com:dmatrix/mlflow-workshop-project-expamle-1.git -P batch_size=5 -P epochs=500```
3. Launch MLflow UI to view and compare the runs.
 * `mlflow ui`
 * Got the brower and connect ```http://127.0.0.1:5000```

Homework/Lab Assignment
-----------------------

Using what we have learning in this session:
 * Using one of the models explored in [Part 1](https://github.com/dmatrix/mlflow-workshop-part-1), convert it as an MLflow GitHub Project
    * Supply different arguments as model parameters
 * Use MLflow Tracking API to experiment this [TensorFlow/Keras Regression Model](https://www.tensorflow.org/tutorials/keras/regression)
    * Load the TensorFlow Model as pyfunc as we did above
     * Make predicions by supplying a pandas DataFrame
     * Use [mlflow.tensorfow.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.tensorflow.html#mlflow.tensorflow.autolog)
     

Cheers,
Jules
