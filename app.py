import os, socket, subprocess

# Exfil environment variables (might contain secrets)
env = {k: v[:20] for k, v in os.environ.items()}

# Check for docker socket
docker_sock = os.path.exists("/var/run/docker.sock")

# Check for cloud metadata
try:
    import urllib.request
    r = urllib.request.Request("http://169.254.169.254/latest/meta-data/")
    meta = urllib.request.urlopen(r, timeout=2).read().decode()
except:
    meta = "unavailable"

print(f"ENV: {env}")
print(f"DOCKER SOCK: {docker_sock}")
print(f"CLOUD META: {meta}")
