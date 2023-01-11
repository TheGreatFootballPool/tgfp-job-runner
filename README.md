# tgfp-job-runner
Docker container for running scheduled jobs

## Description
This container will run a 'scheduler' daemon, when the daemon starts, it will dynamically read the contents of the `include`
It will install all packages in the pyproject.toml file using poetry

## Requirements for use
* Create folder called `scripts` with the following structure
   *  `__init__.py`
   * `jobs.py`
* Contents of `jobs.py`
```python
def load():
    pass
```

The `load()` function will be called by the schedule on startup to load the schedule of jobs to be run

see the `scripts` folder in this repo for an example implementation using sentry logging

### Build and Deploy instructions
When updating to newer version of `tgfp-nfl`:
* `poetry cache clear pypi --all`
* `poetry add tgfp-nfl:latest`
* `bump_version_and_publish.sh` 
  * https://github.com/johnsturgeon/tgfp-job-runner 
  * https://hub.docker.com/repository/docker/johnofcamas/tgfp-job-runner/general