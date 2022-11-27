# BUILD IMAGE --------------------------------------------------------

FROM rust as builder

# Update default packages
RUN apt-get update

# Get tools needed
RUN apt-get install -y git

# Get the simulation code
WORKDIR /rust-app
RUN git clone https://github.com/logos-co/consensus-research.git

# Compile it
WORKDIR /rust-app/consensus-research
RUN cargo build --profile release-opt --bin snow-family


# ACTUAL IMAGE ------------------------------------------------------
FROM python

COPY --from=builder /rust-app/consensus-research/target/release-opt/snow-family /usr/local/bin/snow-family

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:src"

ENTRYPOINT ["python", "src/main.py"]


