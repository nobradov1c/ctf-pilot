# Forensics

## Docker

- `docker history --no-trunc <image_id>` - show used commands
- [dive](https://github.com/wagoodman/dive) - explore layer contents
- [skopeo](https://github.com/containers/skopeo) - inspect properties and configuration
  - `skopeo inspect docker-daemon:hackinglab/jumphost:latest`
  - `skopeo inspect --config docker-daemon:hackinglab/jumphost:latest`
- `/var/lib/docker/overlay2` - layers location
