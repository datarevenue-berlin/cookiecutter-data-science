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

If you see something similar to this everything worked well and you are
ready to start developing:

```txt
Alans-MBP:test_project kayibal$ docker-compose run controller Example
Starting test_project_dask-scheduler ... done
Starting test_project_luigid         ... done
Starting test_project_dask-worker_1  ... done
2018-05-30 18:53:39 INFO     luigi-interface Informed scheduler that task   Example_False_847ab9f492   has status   PENDING
2018-05-30 18:53:39 INFO     luigi-interface Informed scheduler that task   ClientUpload__99914b932b   has status   DONE
2018-05-30 18:53:39 INFO     luigi-interface Done scheduling tasks
2018-05-30 18:53:39 INFO     luigi-interface Running Worker with 1 processes
2018-05-30 18:53:39 INFO     luigi-interface [pid 1] Worker Worker(salt=869995943, workers=1, host=06c48c4fe678, username=root, pid=1) running   Example(no_remove_finished=False)
2018-05-30 18:53:39 INFO     root            /home/drtools/test_project/root_dir/data/raw/clickstream.csv
|CONTAINER| __main__ 2018-05-30 18:53:42 INFO Connected to scheduler
|CONTAINER| __main__ 2018-05-30 18:53:42 INFO Clickstream loaded:
|CONTAINER| id  page_id
|CONTAINER| 0  A   page-1
|CONTAINER| 1  B   page-2
|CONTAINER| 2  A   page-2
|CONTAINER| 3  B   page-1
2018-05-30 18:53:43 INFO     luigi-interface [pid 1] Worker Worker(salt=869995943, workers=1, host=06c48c4fe678, username=root, pid=1) done      Example(no_remove_finished=False)
2018-05-30 18:53:43 INFO     luigi-interface Informed scheduler that task   Example_False_847ab9f492   has status   DONE
2018-05-30 18:53:43 INFO     luigi-interface Worker Worker(salt=869995943, workers=1, host=06c48c4fe678, username=root, pid=1) was stopped. Shutting down Keep-Alive thread
2018-05-30 18:53:43 INFO     luigi-interface
===== Luigi Execution Summary =====

Scheduled 2 tasks of which:
* 1 present dependencies were encountered:
    - 1 ClientUpload()
* 1 ran successfully:
    - 1 Example(no_remove_finished=False)

This progress looks :) because there were no failed tasks or missing external dependencies

===== Luigi Execution Summary =====
```

Any data generated by your tasks will be persisted in to root_dir.

Code is ran inside docker containers which are seen as a logical task units in a
machine learning pipeline [see more](https://app.stiki.io/notes/16749-460-Tasks-as-Containers---Architecture)


## Changes
- Deploy on a docker + compose machine with a single command
- No more host python installation needed thanks to controller container (mdank)
- Fast and simple image building process
- Expressive and short commands which avoid boilerplate code
- Improved file handing with FileStructure class
- Fully configurable dask + luigi + logging 
- Out of the box luigi email notifications
- Ready to push package with git vc and versioneer versioning
- Clean and minimal logs: no more double logging
- Configured with code mapping to avoid rebuild on each code change
- Plug and play replaceable root data directory, scales easy to more (possibly remote) data

## Next Steps
- jupyter notebook
- aws templates
- ecs integration


### Running the tests
------------
Some tests might require you to have a docker daemon running locally.

    py.test tests
