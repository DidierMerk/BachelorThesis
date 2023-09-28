FROM gitlab-registry.cern.ch/ai-ml/kubeflow_images/pytorch-notebook-gpu-1.8.1:v0.6.1-33

USER root

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -Ur /requirements.txt --no-cache-dir

USER jovyan

RUN git clone https://github.com/hqucms/weaver.git

# The following line is mandatory:
CMD ["sh", "-c", \
     "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser \
      --allow-root --port=8888 --LabApp.token='' --LabApp.password='' \
      --LabApp.allow_origin='*' --LabApp.base_url=${NB_PREFIX}"]
