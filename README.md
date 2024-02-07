# HDMI Matrix Control API

## Introduction

This is a simple REST API to switch input/outputs on an EZCOO HDMI Matrix with a USB connection. It has been tested with this model:

 - https://www.amazon.co.uk/HDMI-Matrix-Out-4K-60Hz/dp/B0B8H3JVP2

The micro USB port on the front is connected to a CH340 USB to serial adapter internally. The protocol is documented in https://www.easycoolav.com/u_file/1911/file/c8ecd75651.pdf.

## Installation

Install the dependencies using `pip install -r requirements.txt`. Then install a web server, I suggest uvicorn by running `pip install "uvicorn[standard]"`.

## Configuration

Configuration is done using either the `.env` file or through the environment.

Set `HDMI_MATRIX_DEVICE` to the serial device for the matrix, eg. `HDMI_MATRIX_DEVICE=COM5` or `HDMI_MATRIX_DEVICE=/dev/ttyS0`.

The API key is set using `API_KEY`.

## Docker

An easier way to run it is through Docker and docker compose. Create a docker-compose file like this:

```yaml
version: '3'
services:
  matrix:
    image: ghcr.io/mintopia/hdmi-matrix-api:develop
    ports:
      - 80:80
    devices:
      - /dev/ttyUSB0:/dev/ttyUSB0
    environment:
      - HDMI_MATRIX_DEVICE=/dev/ttyUSB0
      - API_KEY=swordfish
    restart: always
```

You can then start the API server by running `docker compose up -d`.

## Usage

Start the application using `uvicorn app.main:app`. It will now be listening on port 8000 and you can view the documentation at https://localhost:8000/docs or https://localhost:8000/redoc.

## Contributing

It's an open source project, and I'm happy to accept pull requests!

## License

The MIT License (MIT)

Copyright (c) 2024 Jessica Smith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
