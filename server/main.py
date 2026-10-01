import hashlib
import string
import random
from pathlib import Path
from fastapi.responses import FileResponse

from fastapi import FastAPI


DATA_FILE = Path("serverdata/randomletters.txt")
rand_data = "".join(random.choices(string.ascii_letters + string.digits + " ", k=1024))
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(DATA_FILE, "w") as f:
    f.write(rand_data)

app = FastAPI()


@app.get("/file")
def get_file():
    with open(DATA_FILE, "rb") as f:
        checksum = hashlib.sha256(f.read()).hexdigest()
        print("sent cheksum", checksum)

    return FileResponse(
        DATA_FILE,
        media_type="application/octet-stream",
        filename="random.txt",
        headers={"X-Checksum-SHA256": checksum},
    )
