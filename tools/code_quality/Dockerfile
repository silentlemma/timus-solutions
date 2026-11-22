FROM gcc:13.2@sha256:15c73bc59ae88b3fd563ef2ec4a8743a8848a9f74362b6d116c4543c4844b6e0 AS cpp
FROM golang:1.14@sha256:1a7173b5b9a3af3e29a5837e0b2027e1c438fd1b83bbee8f221355087ad416d6 AS go
FROM eclipse-temurin:8-jdk@sha256:e80636b3f64e28efb1211789c0d35409839ad3e4d2048c666866765f5739fd8c AS java
FROM rust:1.75-slim@sha256:70c2a016184099262fd7cee46f3d35fec3568c45c62f87e37f7f665f766b1f74 AS rust
RUN rustup component add rustfmt --toolchain 1.75.0

FROM python:3.12-slim-bookworm@sha256:935c3c5b12357a7e10caa9c1e6ca5692344d97cf229832ef584be2cec9fc03df
RUN apt-get update && apt-get install -y --no-install-recommends binutils libc6-dev libgmp10 libmpfr6 libmpc3 libisl23 libstdc++6 libzstd1 zlib1g libfontconfig1 make && rm -rf /var/lib/apt/lists/*
COPY --from=cpp /usr/local/bin/ /usr/local/bin/
COPY --from=cpp /usr/local/lib/ /usr/local/lib/
COPY --from=cpp /usr/local/lib64/ /usr/local/lib64/
COPY --from=cpp /usr/local/libexec/ /usr/local/libexec/
COPY --from=cpp /usr/local/include/ /usr/local/include/
COPY --from=go /usr/local/go/ /usr/local/go/
COPY --from=java /opt/java/openjdk/ /opt/java/openjdk/
COPY --from=rust /usr/local/rustup/ /usr/local/rustup/
COPY --from=rust /usr/local/cargo/ /usr/local/cargo/
ENV PATH="/usr/local/go/bin:/opt/java/openjdk/bin:/usr/local/cargo/bin:${PATH}" JAVA_HOME="/opt/java/openjdk" RUSTUP_HOME="/usr/local/rustup" CARGO_HOME="/usr/local/cargo" LD_LIBRARY_PATH="/usr/local/lib64" PYTHONDONTWRITEBYTECODE=1 PYTHONUTF8=1 GO111MODULE=off GOMAXPROCS=1
COPY tools/code_quality/requirements.txt /quality/requirements.txt
RUN pip install --no-cache-dir -r /quality/requirements.txt
RUN python -c "import urllib.request; urllib.request.urlretrieve('https://github.com/golangci/golangci-lint/releases/download/v1.40.1/golangci-lint-1.40.1-linux-amd64.tar.gz','/tmp/golangci.tar.gz')" && echo "7c133b4b39c0a46cf8d67265da651f169079d137ae71aee9b5934e2281bd18d3  /tmp/golangci.tar.gz" | sha256sum -c - && tar -xzf /tmp/golangci.tar.gz -C /tmp && cp /tmp/golangci-lint-1.40.1-linux-amd64/golangci-lint /usr/local/bin/ && rm -rf /tmp/golangci*
RUN g++ -dumpfullversion | grep '^13.2.0$' && go version | grep 'go1.14.15 ' && javac -version 2>&1 | grep 'javac 1.8.0_' && rustc --version | grep '^rustc 1.75.0 ' && rustfmt --version && ruff --version && clang-format --version && golangci-lint --version
