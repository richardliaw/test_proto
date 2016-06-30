## Installation for CapnProto and Protobuf

1. First install Docker
2. clone directory to somewhere; cd into directory
3. `docker build -t test_proto .`
4. `docker run -it test_proto bash`
5. `cd example`

### Demos
For protobuf demos, do the following:
1. `cd protobuf`
2. `protoc --python_out=. addressbook.proto`
3. `python addressbook_test.py`

For python capnp demos, do the following from within the repo directory:
1. `cd capnproto`
2. `python addressbook.py`

For Capnp RPC, 
1. Open two terminals - one of which is running docker container (or augment the dockerfile to include tmux)
2. On the other, find out the name of that docker using `docker ps` - e.g. "clever_lichterman"
3. `docker exec -it [name] bash`
4. On one terminal, `cd capnproto; python thread_server.py`
5. On other, `cd capnproto; python thread_client.py`

Enjoy.
