# commlib-cli

CLI for broker-based communication using commlib-py


# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


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
