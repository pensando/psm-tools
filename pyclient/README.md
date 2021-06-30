## Using PSM python client

1. Clone the repo (in any directory)
```
git clone https://github.com/pensando/psm-tools
cd psm-tools/pyclient
```

2. Run the python3 environment to make client libraries
```
make run-container
```


Inside the container run `make` to generate the api client.
```
root@6de26ac2cb83:/pyclient# make
```

3. Run python client apps to confirm all is good
```
./apps/cluster_ping.py
```

## Advanced operations
* For non interactive mode, you must do a few additional setup
1. Create ~/.psm/config.json file with PSM coordinates
```
$ cat ~/.psm/config.json
{
  "psm-ip": "psm's ip address",
}
```

2. Specify the PSM credentials either by setting PSM_USER and PSM_PASSWORD variables or modify the ~/.psm/config.json as follows
```
{
  "psm-ip": "psm's ip address",
  "token": "psm user's jwt token"
}
```

* Building docker container
```
docker build . -t pyclient:0.1
```

* Running python code natively (not in docker container)
You'll need to install python3, pip, java and maven as documented in the Dockerfile, and set $PYTHONPATH 

## Contributor's Guide
Contributors are welcome. Please follow the following guidelines to contrbute to this repo
* Please follow [this git workflow](./docs/git-workflow.md) to submit a pull-request
* Rebase to the main branch
* Pass all unit tests `make tests`
* At least one approval on the pull request
