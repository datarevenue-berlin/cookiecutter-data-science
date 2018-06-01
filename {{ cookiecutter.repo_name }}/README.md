## {{cookiecutter.project_name}}

{{cookiecutter.description}}

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


## Get Started

1. Set MODULES_PATH this is the absolute path to the directory that contains the current project as well as dependencies like sparsity and drtools `MODULES_PATH="$(dirname $PWD)"`
1. Run the example task: `docker-compose run controller Example`

This will run the project in development environment. This means that code from
your host is mapped to the respective directories in the container, avoiding to
rebuild images on every code change. 

To run without dev mode it is sufficient to specify the `-f docker-compose.yml`
option this will disable dev mode and run the project in default mode which
only maps the root_dir into the container.

## Debug

To get a shell inside a task you can use 

`docker-compose run controller Debug`

This will execute a dummy task which just sleeps for 24h. To get the interactive
shell look up the container id and run:

`docker exec -ti <container_id> bash`


## Architecture
[see more](https://app.stiki.io/notes/16749-460-Tasks-as-Containers---Architecture)

