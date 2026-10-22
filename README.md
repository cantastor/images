# Cantastor images

Public release metadata for Cantastor's microsandbox images. The desktop application repository remains separate and private.

| Package | Purpose |
| --- | --- |
| `ghcr.io/cantastor/inference-proxy` | CLIProxyAPI inference service |
| `ghcr.io/cantastor/agent-microsandbox-slim` | Agent handoffs and review |
| `ghcr.io/cantastor/agent-microsandbox-office` | Agent image with LibreOffice |
| `ghcr.io/cantastor/agent-microsandbox-editor` | OpenVSCode editor |

See [releases.json](releases.json) for exact tags, digests, architectures and Docker Hub mirrors. Agent/editor releases preserve the complete upstream manifest lists and attestations. Proxy 8.0.38 currently supports Linux amd64 only. Prefer digest-pinned downloads; tag names alone are not integrity guarantees.

## Mirrors

Both registries distribute identical manifests for the listed release. Cantastor's Automatic source tries GHCR first, then Docker Hub on failure. Users may explicitly choose either registry without changing the software version. Public packages can be pulled without a GitHub account.

## Licenses and source

Images contain multiple independent software packages, not one blanket license. Preserve the license notices supplied inside each image, including Debian's `/usr/share/doc/*/copyright` and `/usr/share/common-licenses`. CLIProxyAPI 8.0.38 is [MIT licensed](https://github.com/router-for-me/CLIProxyAPI/blob/v8.0.38/LICENSE); its notice is included at `/usr/share/doc/cli-proxy-api/LICENSE`. The management UI is a separately maintained upstream component.

Redistributors must meet each component's applicable source-distribution obligations. This initial release index is not a complete source archive or dependency-license audit. Contact the maintainers through this repository's issues for corresponding-source requests. Provider service terms apply independently of software licenses; image availability is not permission to use any provider's subscription credentials.

## Publishing

The release workflow copies immutable Docker Hub manifests to GHCR with all platforms and digest preservation. Package visibility is set separately in GitHub package settings, and each package is linked to this repository. Never place credentials or Cantastor user data in build contexts, image layers, this repository or workflow logs.
