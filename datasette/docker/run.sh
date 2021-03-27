set -e

docker build -f Dockerfile -t $(basename $(pwd)) .
# docker run -it --rm -w /app -v $(pwd):/app -p 8001:8001 --entrypoint /bin/bash $(basename $(pwd))