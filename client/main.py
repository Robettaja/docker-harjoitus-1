import argparse
import hashlib
import requests
from pathlib import Path


def calculate_checksum(path):
    sha256 = hashlib.sha256()

    with open(path, "rb") as f:
        checksum = hashlib.sha256(f.read()).hexdigest()

    return checksum


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Server URL")
    args = parser.parse_args()

    response = requests.get(f"{args.url}/file")
    response.raise_for_status()

    output_file = Path("clientdata/received.txt")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "wb") as f:
        f.write(response.content)

    server_checksum = response.headers.get("X-Checksum-SHA256")
    client_checksum = calculate_checksum(output_file)

    print(f"Server checksum: {server_checksum}")
    print(f"Client checksum: {client_checksum}")

    if server_checksum == client_checksum:
        print("Checksum OK")
    else:
        print("Checksum mismatch!")


if __name__ == "__main__":
    main()
