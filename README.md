# Legacy Java and observability composition

Historical Docker Compose reference by [Daniel Duran](https://www.dan1el64.com/). This is not the recommended portfolio starter; see [Hexagonal Architecture Labs](https://github.com/dan1el64/hexagonal-architecture-labs).

## Configuration cleanup

The owner confirmed that previously committed credentials were test values. The current source removes the tracked `.env`, literal passwords, private server configuration and authenticated Git clone build arguments. Configuration now comes from an ignored local `.env`; only `.env.example` is tracked.

The historical commit still contains the old test values. This change does not rewrite shared Git history or revoke credentials. If any historical test value was reused elsewhere, change it at that service before treating it as safe. Never use real credentials in this legacy demo.

## Inspect locally

```sh
cp .env.example .env
# Replace CHANGE_ME values with separate local-only values.
python3 scripts/check-config.py
docker compose config --quiet
```

`docker compose up -d` starts the historical observability stack and MinIO. Images are intentionally inherited from the legacy project; this cleanup is not an upgrade or a production security certification. Ports bind to localhost. The Elasticsearch 7.6.2 stack is old and should not be exposed publicly.

The optional application is disabled by default. To use it, build an authorized Java 11 application locally, place its JAR at `artifacts/app.jar`, configure a reachable database, then run `docker compose --profile legacy-app up --build`. No application source or JAR is provided here. Logs use relative local folders, not a specific server path.

Do not put GitHub tokens in build arguments, environment files committed to Git, or authenticated clone URLs. This repository's CI validates configuration and checks for literal credential assignments; it does not deploy anything.
