# Introduction
This is a skeletal server-client file transfer program. A custom socket has been written to emulate an imperfect network (e.g. radio waves over the air), introducing byte errors to the payload. The severity of this can be set by `BYTE_ERROR_RATE` in `settings.py`

# Demo
`RUN_DEMO` in `settings.py` can be set to

- 1: A short string is sent from the server to the client
- 2: A test image is sent from the server to the client 

To run the demos, execute the following commands in order:
## Server
`python server.py`

## Client
`python client.py`