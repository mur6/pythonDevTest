FROM python:3.8
RUN apt-get update
RUN pip --no-cache-dir install cython
RUN git clone https://github.com/rkern/line_profiler.git && \
    cd line_profiler && \
    pip install .
RUN pip --no-cache-dir install poetry flake8 black
