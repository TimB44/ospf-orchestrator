import argparse
import subprocess
import sys

def start(args):
    print("start")


def configure(args):
    print("conf")


def stop(args):
    print("stop")



def route(args):
    print(f"router = {args}")


# MAIN ------------------------
# Set up CLI interface
parser = argparse.ArgumentParser(
    description="Simple network orchestrator used to move traffic between router paths")
subparsers = parser.add_subparsers(dest="command", required=True)

parser_start = subparsers.add_parser(
    "start", help="Start all docker containers")
parser_start.set_defaults(func=start)

parser_conf = subparsers.add_parser("configure", help="Configure network")
parser_conf.set_defaults(func=configure)

parser_stop = subparsers.add_parser("stop", help="Stop all docker containers")
parser_stop.set_defaults(func=stop)

parser_route = subparsers.add_parser("route", help="Route traffic")
parser_route.add_argument("direction", choices=[
                         "north", "south"], help="Choose router path")
parser_route.set_defaults(func=route)

args = parser.parse_args()
args.func(args)
