# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible tas as containers project structure for doing, sharing and deploying data science work

Inspired by on [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/)

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── root_dir           <- The root filesystem mapping directory. This 
    │   │                     can be and will be replaced with remote file-
    │   │                     systems to scale the application up to real world
    │   │                     data.
    │   ├── models         <- Trained and serialized models, model predictions, or model summaries
    │   │   │                 Naming convention <model-type>-<param-desc>-<train-dates-hash>-<feature-hash>
    │   │   └── predictions<- predictions on full test datasets. Naming convention a model description
    │   │                     and a '-' delimited date descriptor '<model-id>-2016-01-01'
    │   └── data
    │       ├── external   <- Data from third party sources.
    │       ├── interim    <- Intermediate data that has been transformed.
    │       ├── processed  <- The final, canonical data sets for modeling.
    │       └── raw        <- The original, immutable data dump.
    │
    ├── deploy             <- deployment configurations
    │   
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     the creator's initials, and a short `-` delimited description, e.g.
    │   │                     `1.0-jqp-initial-data-exploration`.
    │   ├── exploratory    <- excluded from version control use for fast drafts
    │   └── experiments    <- use to run a whole experiment one folder per experiment
    │                         with a executable pipeline.py and evaluation.py script
    │
    ├── references         <- Publications, Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── dataset.py
    │   │
    │   ├── features       <- All kind of feature files
    │   │   └──features.csv
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── tasks          <- Long/Recurrent running luigi tasks
    │   │
    │   ├── tests          <- integration and unittests
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
--------

### Requirements to use the cookiecutter template:
-----------
 - Python>=3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### Start a new project
Make sure you have docker and docker-compose installed and the docker 
daemon running.

```bash
# Instantiate template
cookiecutter https://github.com/datarevenue-berlin/project-template.git

# cd into project
cd <repo_name>

# Build/Pull images and run example task
docker-compose -f docker-compose.yml run controller Example
```

Code is ran inside docker containers which are seen as a logical task units in a
machine learning pipeline [see more](https://app.stiki.io/notes/16749-460-Tasks-as-Containers---Architecture)

### Running the tests
------------
Some tests might require you to have a docker daemon running locally.

    py.test tests
