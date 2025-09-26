FROM alpine:latest

WORKDIR /app

RUN apk add --no-cache build-base

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin:${PATH}"



ADD https://sh.rustup.rs /rust-installer.sh
RUN sh /rust-installer.sh -y && rm /rust-installer.sh
ENV PATH="/root/.cargo/bin:${PATH}"

RUN uv python install
RUN uv tool install maturin

COPY ./rukkola-rc ./rukkola-rc

RUN cd ./rukkola-rc && uv run maturin develop

COPY pyproject.toml .python-version ./

RUN uv sync

COPY . .

CMD uv run uvicorn rukkola.src:main --host 0.0.0.0 --port 8000 --reload