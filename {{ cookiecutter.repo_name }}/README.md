## {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   │   ├── train      <- <min-date>-<max-date>-<dates-hash>-<feature-hash>.parquet
    │   │   └── test       <- <date>-<feature-hash>.parquet
    │   └── raw            <- The original, immutable data dump.
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
    │   ├── experiments    <- use to run a whole experiment one folder per experiment
    │   │                     with a executable pipeline.py and evaluation.py script
    │   └── backtest       <- contains nicely polished notebooks that explain and
    │                         visualize backtests to assess performance of a system.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
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

# IS24 User Scoring Application

## Get Started

The master server for this project is reachable under `{{cookiecutter.project_name}}.datarevenue.ml`. The only exposed port is 22 which is used for ssh connection. By default datarevenue employees github public keys and usernames are used to authenticate on the server.


### Port Forwarding
Many services provide web interfaces which are accesible over certain ports. To access them from a local machine you have to setup port forwarding.
This can be achieved by adding the following snippet into you `~/.ssh/config` file:

```
Host {{cookiecutter.project_name}}
    HostName {{cookiecutter.project_name}}.datarevenue.ml
    User <your-github-username>
    IdentityFile ~/.ssh/id_rsa
    
    # Jupyterhub
    LocalForward 8000 127.0.0.1:8000
    
    # Luigi scheduler interface
    LocalForward 8082 127.0.0.1:8082
    
    # Dask-Scheduler interface
    LocalForward 8787 127.0.0.1:8787
    LocalForward 8788 127.0.0.1:8788
    
    # Dask-Worker interface
    LocalForward 8789 127.0.0.1:8789
    
    # Disable host key checking
    # this is somewhat insecure but ok
    UserKnownHostsFile /dev/null
    StrictHostKeyChecking no
```

By executing `ssh {{cookiecutter.project_name}}` all services should be available under `localhost:<service-port>`.


## Development
This application comes with preconfigured docker containers to execute without hassle. All necessary files to build and run containers in correct configurations are included in the deployment directory.

### Services
This app consists of multiple services that are used to run the algorithms

#### Worker
A worker container basically to run scripts or luigi tasks in

#### Dask-scheduler
The central dask-scheduler. We use dask as ETL and concurrency library mostly to process big amounts of data or train machine learning models.

#### Dask-worker
The dask-worker is the container in which dask graphs will be computed in.

#### Luigid
The luigi central scheduler. We use luigi to specify dependencies and handle
orchestration of high level tasks. E.g. automate model search or automate daily predictions.

### JupyterHub

This project uses jupyterhub to give access to notebook servers. To get a jupyterhub session you need to add a password to your useraccount to do this ssh into you account and execute `sudo passwd <username>`. Now you should be able to login into jupyterhub under `localhost:8000`.

#### Sharing notebooks
To share a notebook you must copy the file with to someones home directory or into a shared directory. Alternatively you can commit the notebooks as it should be done with important and CLEAN notebooks.

## Automatic release building
To release a new version for live you should tag your commit and run `deploy/build_release.sh` this will create a wheel distribution of the project and all it's dependencies. Subsequently this wheel distribution will be installed into a minimal container image and tagged as `drtools/is24de-worker:<COMMIT-SHA>`. After completing all tests this image can be pushed using `docker-compose push`

### Deploy to staging env

The following steps illutrate how to build a release and deploy it to the staging env.

- Tag the commmit you would like to deploy with e.g: `git tag -a v2.1.0pre -m "Awesome new release"`
- Push the tag `git push --tags`

Usually the following steps are executed on the server.

- Shut down the dev environment with `docker-compose stop` 
- now from within the deploy dir run `./build_release v2.1.0pre`. This will build a release based on your commit and create a new docker image named: `drtools/is24de-worker:v2.1.0pre`
- Finally by executing `./stage_scoring v2.1.0pre` will run this new container in a staging env locally and if this succeeds it will create a new datapipeline which executes the application daily in the same environment as production.
