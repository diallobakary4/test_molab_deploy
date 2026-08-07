FROM ghcr.io/prefix-dev/pixi:0.70.1 AS build
WORKDIR /app
COPY . .
RUN pixi install --locked -e default
RUN pixi shell-hook -e default -s bash > /shell-hook
RUN echo "#!/bin/bash" > /app/entrypoint.sh
RUN cat /shell-hook >> /app/entrypoint.sh
RUN echo 'exec "$@"' >> /app/entrypoint.sh

FROM ubuntu:24.04 AS production
RUN userdel ubuntu && useradd -m -u 1000 user
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /app
COPY --from=build /app/.pixi/envs/default /app/.pixi/envs/default
COPY --from=build --chmod=0755 /app/entrypoint.sh /app/entrypoint.sh
COPY . /app
RUN chown -R user:user /app
USER user
EXPOSE 7860
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["marimo", "run", "notebooks/demo_drug_discovery.py", \
     "--host", "0.0.0.0", "--port", "7860"]
