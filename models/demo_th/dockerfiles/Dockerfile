FROM mhubai/base:latest

# create environment variable with the model name
ENV MHUB_MODEL_NAME=demo_th

# install and system lybraries and dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     <library name> \
# && rm -rf /var/lib/apt/lists/* 

# install any python dependencies 
# RUN pip3 install --no-cache-dir \
#     <package name> 

# install model
RUN pip3 install git+https://github.com/mhubai/thresholder_demo.git

# load model definition
ARG MHUB_MODELS_REPO
RUN buildutils/import_mhub_model.sh ${MHUB_MODEL_NAME} ${MHUB_MODELS_REPO}

# specify entrypoint
ENTRYPOINT ["mhub.run"]
CMD ["--config", "/app/models/${MHUB_MODEL_NAME}/config/default.yml"]