# commlib-cli

Broker-transparent CLI for ReqResp and PubSub communication using commlib-py.


# Installation

If you don't already have [commlib-py](https://github.com/robotics-4-all/commlib-py) please proceed before
installing this CLI.

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .

Or install in userspace in devel mode to easily apply repo updates

```bash
$ pip install -r requirements.txt
$ python setup.py develop --user
```

# Usage

To use it:

```
[I] ➜ commlib-cli --help
Usage: commlib-cli [OPTIONS] COMMAND [ARGS]...

  CLI for broker-based communication using commlib-py

Options:
  --host TEXT       Broker ip/domain
  -p, --port TEXT   Broker port
  -t, --btype TEXT  Broker port
  --vhost TEXT      AMQP Broker port
  --db INTEGER      Redis Broker port
  --username TEXT   Broker auth username
  --password TEXT   Broker auth password
  --help            Show this message and exit.

Commands:
  pub   Publisher
  rpcc  RPC Client
  rpcs  RPC Service
  sub   Subscriber

```

## Examples

### ReqResp/RPC Communication

In a terminal run the AMQP RPC Service

```bash
commlib-cli --btype amqp rpcs 'ops.motion.move_by_vel'
```

In a terminal call the AMQP RPC Service
```bash
commlib-cli --btype amqp rpcc 'ops.motion.move_by_vel' '{"linear_vel": 1.0, "angular_vel": 0.0}'
```

### PubSub Communication

In a terminal run the MQTT Subscriber

```bash
commlib-cli --btype mqtt sub 'sensors.temperature.tmps1'
```

In a terminal call the MQTT Publisher
```bash
commlib-cli --btype mqtt pub --rate 1 'sensors.temperature.tmps1' '{"temperature": 22.3}'
```
