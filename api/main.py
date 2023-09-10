from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

from utils.files import generate_random_data

app = FastAPI()


@app.get("/generate_random_file/")
async def generate_random_file(size_bytes: int):
    if size_bytes <= 0:
        raise HTTPException(status_code=400, detail="Size must be greater than zero")

    def generate_lines():
        chunk_size = 1024  # You can adjust the chunk size as needed
        remaining_size = size_bytes
        while remaining_size > 0:
            # Generate a chunk of random data
            chunk = generate_random_data(min(chunk_size, remaining_size))
            yield chunk
            remaining_size -= len(chunk)

    response = StreamingResponse(
        generate_lines(),
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename=random_data.txt"},
    )
    return response
