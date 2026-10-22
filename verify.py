"""Check anonymous registry access and exact manifest identity; Python standard library only."""
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ACCEPT = ", ".join(["application/vnd.oci.image.index.v1+json", "application/vnd.docker.distribution.manifest.list.v2+json", "application/vnd.oci.image.manifest.v1+json", "application/vnd.docker.distribution.manifest.v2+json"])

def inspect(reference, tag):
    registry, repository = reference.split("/", 1)
    token_host = "https://ghcr.io/token" if registry == "ghcr.io" else "https://auth.docker.io/token"
    service = "ghcr.io" if registry == "ghcr.io" else "registry.docker.io"
    host = "ghcr.io" if registry == "ghcr.io" else "registry-1.docker.io"
    query = urlencode({"service": service, "scope": f"repository:{repository}:pull"})
    with urlopen(token_host + "?" + query, timeout=30) as response:
        auth = json.load(response)
    request = Request(f"https://{host}/v2/{repository}/manifests/{tag}", headers={"Accept": ACCEPT, "Authorization": "Bearer " + auth.get("token", auth.get("access_token", ""))})
    with urlopen(request, timeout=30) as response:
        data = response.read()
    return "sha256:" + hashlib.sha256(data).hexdigest()

if __name__ == "__main__":
    releases = json.loads(Path(__file__).with_name("releases.json").read_text())["images"]
    results = []
    for image in releases:
        for registry in ["dockerHub", "ghcr"]:
            digest = inspect(image[registry], image["tag"])
            assert digest == image["digest"], (image["name"], registry, digest, image["digest"])
            results.append({"image": image["name"], "registry": registry, "digest": digest, "anonymous": True})
    print(json.dumps(results, indent=2))
