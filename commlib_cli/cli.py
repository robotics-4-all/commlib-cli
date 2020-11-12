import click
import json
import time


@click.group()
@click.option('--host', '-h', default='localhost', help='Broker ip/domain')
@click.option('--port', '-p', default=None, help='Broker port')
@click.option('--btype', '-t', default='mqtt', help='Broker port')
@click.option('--vhost', default='/', help='AMQP Broker port')
@click.option('--db', default=0, help='Redis Broker port')
@click.option('--username', default='', help='Broker auth username')
@click.option('--password', default='', help='Broker auth password')
@click.pass_context
def cli(ctx, host, port, btype, vhost, db, username, password):
    """CLI for broker-based communication using commlib-py"""
    if btype == 'mqtt' and port is None:
        port = 1883
    elif btype == 'amqp' and port is None:
        port = 5672
    elif btype == 'redis' and port is None:
        port = 6379
    if btype == 'amqp' and username == '':
        username = 'guest'
        password = 'guest'

    ctx.ensure_object(dict)

    if btype == 'mqtt':
        from commlib.transports.mqtt import (
            Publisher, ConnectionParameters, Credentials
        )
        conn_params = ConnectionParameters(host=host,
                                           port=port)
    if btype == 'amqp':
        from commlib.transports.amqp import (
            Publisher, ConnectionParameters, Credentials
        )
        conn_params = ConnectionParameters(host=host,
                                           port=port,
                                           vhost=vhost)
    if btype == 'redis':
        from commlib.transports.redis import (
            Publisher, ConnectionParameters, Credentials
        )
        conn_params = ConnectionParameters(host=host,
                                           port=port,
                                           db=db)

    creds=Credentials(username=username,
                      password=password)
    conn_params.creds = creds
    ctx.obj['conn_params'] = conn_params
    ctx.obj['btype'] = btype


@cli.command(help='Publisher')
@click.pass_context
@click.option('--rate', default=1, help='Publishing rate in hz')
@click.argument('uri')
@click.argument('data')
def pub(ctx, rate, uri, data):
    data = json.loads(data)
    conn_params = ctx.obj['conn_params']
    btype = ctx.obj['btype']

    if btype == 'mqtt':
        from commlib.transports.mqtt import Publisher
    if btype == 'amqp':
        from commlib.transports.amqp import Publisher
    if btype == 'redis':
        from commlib.transports.redis import Publisher

    pub = Publisher(conn_params=conn_params, topic=uri)
    if rate == 0:
        pub.publish(data)
        return
    while True:
        pub.publish(data)
        time.sleep(1.0 / rate)


@cli.command(help='Subscriber')
@click.pass_context
@click.argument('uri')
def sub(ctx, uri):
    # click.echo(f'URI -> {uri}')
    conn_params = ctx.obj['conn_params']
    btype = ctx.obj['btype']

    if btype == 'mqtt':
        from commlib.transports.mqtt import Subscriber
    if btype == 'amqp':
        from commlib.transports.amqp import Subscriber
    if btype == 'redis':
        from commlib.transports.redis import Subscriber

    def on_message(data):
        print(data)

    sub = Subscriber(conn_params=conn_params, topic=uri, on_message=on_message)
    sub.run_forever()


@cli.command(help='RPC Service')
@click.pass_context
@click.argument('uri')
def rpcs(ctx, uri):
    ## Implements an Echo RPC Service
    conn_params = ctx.obj['conn_params']
    btype = ctx.obj['btype']

    if btype == 'mqtt':
        from commlib.transports.mqtt import RPCService
    if btype == 'amqp':
        from commlib.transports.amqp import RPCService
    if btype == 'redis':
        from commlib.transports.redis import RPCService

    def on_request(msg):
        print(msg)
        return msg

    rpc = RPCService(conn_params=conn_params, rpc_name=uri,
                     on_request=on_request)
    rpc.run_forever()


@cli.command(help='RPC Client')
@click.pass_context
@click.argument('uri')
@click.argument('data')
def rpcc(ctx, uri, data):
    data = json.loads(data)
    conn_params = ctx.obj['conn_params']
    btype = ctx.obj['btype']

    if btype == 'mqtt':
        from commlib.transports.mqtt import RPCClient
    if btype == 'amqp':
        from commlib.transports.amqp import RPCClient
    if btype == 'redis':
        from commlib.transports.redis import RPCClient

    rpc = RPCClient(conn_params=conn_params, rpc_name=uri)
    resp = rpc.call(data)
    print(resp)


def main():
    cli(obj={})
