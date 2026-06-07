FROM ghcr.io/prefix-dev/pixi:0.70.1 AS build

ARG PIXI_ENV=default
ARG NB_USER=jovyan
ARG NB_UID=1000

ENV HOME=/home/${NB_USER}
WORKDIR ${HOME}

COPY . ${HOME}

# Install the locked Pixi environment.
RUN pixi install --locked -e ${PIXI_ENV}

# Create activation wrapper; this is adapted from Pixi's container docs.
RUN pixi shell-hook -e ${PIXI_ENV} -s bash > /shell-hook
RUN printf '#!/bin/bash\n' > /entrypoint.sh \
 && cat /shell-hook >> /entrypoint.sh \
 && printf '\nexec "$@"\n' >> /entrypoint.sh \
 && chmod +x /entrypoint.sh


 FROM ubuntu:22.04
#  FROM ubuntu:24.04 # joywant

ARG PIXI_ENV=default
ARG NB_USER=jovyan
ARG NB_UID=1000

ENV USER=${NB_USER}
ENV NB_UID=${NB_UID}
ENV HOME=/home/${NB_USER}
ENV SHELL=/bin/bash
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=${HOME}/.pixi/envs/${PIXI_ENV}/bin:${PATH}

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    bash \
    ca-certificates \
    tini \
 && rm -rf /var/lib/apt/lists/* \
 && useradd --create-home --shell /bin/bash --uid ${NB_UID} ${NB_USER}

WORKDIR ${HOME}

COPY --from=build ${HOME}/.pixi/envs/${PIXI_ENV} ${HOME}/.pixi/envs/${PIXI_ENV}
COPY --from=build --chmod=0755 /entrypoint.sh /entrypoint.sh
COPY . ${HOME}

USER root
RUN chown -R ${NB_UID}:${NB_UID} ${HOME} /entrypoint.sh
USER ${NB_USER}

EXPOSE 8888

ENTRYPOINT ["/entrypoint.sh"]
CMD ["jupyter", "notebook", "--NotebookApp.default_url=/lab/"]