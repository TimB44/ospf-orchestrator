import argparse
import subprocess
import sys

R1_NAME = "ospf-orchestrator-r1-1"
R2_NAME = "ospf-orchestrator-r2-1"
R3_NAME = "ospf-orchestrator-r3-1"
R4_NAME = "ospf-orchestrator-r4-1"
HA_NAME = "ospf-orchestrator-ha-1"
HB_NAME = "ospf-orchestrator-hb-1"

ROUTER_NAMES = [R1_NAME, R2_NAME, R3_NAME, R4_NAME]
HOST_NAMES = [HA_NAME, HB_NAME]


def start(_):
    print("start")
    proc = subprocess.Popen(["docker", "compose", "up"], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, text=True)
    proc.wait()


# Starts a docker command and returns the process 
def run_docker_cmd(container_name: str, cmd: list[str]) -> subprocess.Popen:
    proc = subprocess.Popen(["docker", "exec", "-it", container_name] + cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, text=True)
    return proc
    
def configure(_):
    print("Downloading ffr on routers")
    procs = [run_docker_cmd(r, ["./configure-scripts/ffrospf.sh"]) for r in ROUTER_NAMES]
    for proc in  procs:
        proc.wait();


    print("Configuring ospf on routers")
    procs = [run_docker_cmd(r, [f"./configure-scripts/setup-{r}.sh"]) for r in ROUTER_NAMES]
    for proc in procs:
        proc.wait()

    print("Configuring hosts")
    procs = [run_docker_cmd(h, [f"./configure-scripts/setup-{h}.sh"]) for h in HOST_NAMES]
    for proc in procs:
        proc.wait()


def stop(_):
    print("stop")
    proc = subprocess.Popen(["docker", "compose", "down"], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, text=True)
    proc.wait()



def route(args):
    dir = args.direction
    print(f"router = {dir}")
    pass


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
