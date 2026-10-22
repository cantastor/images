# A separate microsandbox payload; no provider credentials are baked into this image.
FROM docker.io/library/debian:trixie-slim
ARG TARGETARCH
ARG VERSION=8.0.38
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl \
    && rm -rf /var/lib/apt/lists/*
RUN case "$TARGETARCH" in \
      amd64) arch=amd64; sha=05690c53245a149230a8b7d64085ed96036275a72414d0097f88bb6314acb39b ;; \
      arm64) arch=aarch64; sha=a1282bbbaa3a9ca9e5c36865d1a840e2902b783bbda4894935c04befdb623c29 ;; \
      *) exit 1 ;; esac \
    && curl -fL --retry 3 "https://github.com/router-for-me/CLIProxyAPI/releases/download/v${VERSION}/CLIProxyAPI_${VERSION}_linux_${arch}.tar.gz" -o /tmp/proxy.tar.gz \
    && echo "$sha  /tmp/proxy.tar.gz" | sha256sum -c - \
    && mkdir /tmp/proxy && tar -xzf /tmp/proxy.tar.gz -C /tmp/proxy \
    && install -m755 /tmp/proxy/cli-proxy-api /usr/local/bin/cli-proxy-api \
    && mkdir -p /usr/share/doc/cli-proxy-api \
    && cp /tmp/proxy/LICENSE /usr/share/doc/cli-proxy-api/LICENSE \
    && rm -rf /tmp/proxy /tmp/proxy.tar.gz
EXPOSE 8317
ARG DASHBOARD_VERSION=1.26.7
RUN mkdir -p /opt/cli-proxy-api/static /usr/share/doc/cli-proxy-api-dashboard \
    && curl -fL --retry 3 "https://github.com/router-for-me/Cli-Proxy-API-Management-Center/releases/download/v${DASHBOARD_VERSION}/management.html" -o /opt/cli-proxy-api/static/management.html \
    && echo "8c9c6b7d3fb311e6aad5d06e1993e53a2d28389e640448a1bc6304ed20b057b5  /opt/cli-proxy-api/static/management.html" | sha256sum -c - \
    && curl -fL --retry 3 "https://raw.githubusercontent.com/router-for-me/Cli-Proxy-API-Management-Center/v${DASHBOARD_VERSION}/LICENSE" -o /usr/share/doc/cli-proxy-api-dashboard/LICENSE
ENV MANAGEMENT_STATIC_PATH=/opt/cli-proxy-api/static
CMD ["/usr/local/bin/cli-proxy-api", "-config", "/var/lib/cantastor-proxy/config.yaml"]
