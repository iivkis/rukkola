FROM alpine:latest

WORKDIR /app

# RUN apk add --no-cache build-base

# RUN apk add patchelf

# RUN apk add cargo

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin:${PATH}"

RUN uv python install

# RUN uv tool install maturin[patchelf]

# COPY ./rukkola-rc ./rukkola-rc

# RUN cd ./rukkola-rc && uv run maturin build

COPY pyproject.toml .python-version ./

RUN uv sync

COPY . .

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]