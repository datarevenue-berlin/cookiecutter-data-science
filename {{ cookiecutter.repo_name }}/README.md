## {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── deploy             <- deployment configurations
    │   
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │                         Naming convention <model-type>-<param-desc>-<train-dates-hash>-<feature-hash>
    │   └── predictions    <- predictions on full test datasets. Naming convention a model description
    │                         and a '-' delimited date descriptor '<model-id>-2016-01-01'
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

1. Instantiate template: `cookiecutter https://github.com/datarevenue-berlin/project-template.git`
2. Install project locally (use venv): `pip install -e <project_name>`
3. Build project container: `docker build -t <project-name> .`
3. Start up local dask cluster `docker-compose -f <project-name>/deploy/docker-compose.yml up -d`
4. Run the example task: `luigi --module <project_name>.task Example`

Code is ran inside docker containers which are seen as a logical task unit in a
machine learning pipeline [see more](https://app.stiki.io/notes/16749-460-Tasks-as-Containers---Architecture)

