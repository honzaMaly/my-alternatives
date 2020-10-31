# This configuration is inspired by: https://pythonspeed.com/articles/activate-conda-dockerfile/

# use official Docker image for CONDA
FROM continuumio/miniconda3

WORKDIR /app

# copy ENV configuration
COPY docker_configuration .

# copy everything within the folder (except ignore files)
COPY . .

# add channel to conda
RUN conda config --add channels conda-forge

# copy configuration

# create the Python environment:
RUN conda env create -f environment.yml

# make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "my-alternatives", "/bin/bash", "-c"]

# The code to run when container is started:
ENTRYPOINT ["conda", "run", "-n", "my-alternatives", "python", "run_service.py"]