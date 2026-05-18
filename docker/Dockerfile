# Stage 1: Build Chrono
FROM ubuntu:22.04 as builder

RUN apt-get update && apt-get install -y \
    build-essential cmake git libeigen3-dev \
    libgl1-mesa-dev libxi-dev libxmu-dev \
    libbullet-dev libomp-dev

RUN git clone --depth 1 --branch 8.0 https://github.com/projectchrono/chrono.git \
    && cd chrono && mkdir build && cd build \
    && cmake .. -DENABLE_MODULE_HYDRO=ON -DENABLE_MODULE_VEHICLE=OFF \
    && make -j$(nproc) && make install

# Stage 2: Runtime
FROM ubuntu:22.04

COPY --from=builder /usr/local/lib/libChrono*.so /usr/local/lib/
COPY --from=builder /usr/local/include/chrono* /usr/local/include/

RUN apt-get update && apt-get install -y \
    python3 python3-pip libgl1-mesa-glx libomp5 \
    && pip3 install numpy h5py

COPY . /app/SINOSHOP-Sandbox
WORKDIR /app/SINOSHOP-Sandbox

EXPOSE 8080

CMD ["python3", "scripts/web_demo.py", "--port", "8080"]