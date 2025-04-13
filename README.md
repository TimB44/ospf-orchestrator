# PA3 OSPF Network Orchestrator

Author: Timothy Blamires  
UID: u1414110  

## Overview

This project creates and configures an OSPF-enabled network in Docker. It allows routing traffic between two routes (north/south) with 0% packet loss.

## Project structure
All Docker containers use the same Dockerfile, which is simple and closely based on the one provided. The Dockerfile copies all the shell scripts from `configure-scripts/` into each container. The orchestrator script then runs these scripts inside the appropriate containers to configure the routers and hosts.

The `docker-compose.yml` file is also based on the example provided but has been extended to include more routers and network links.

## Prerequisites

- Docker and Docker Compose installed
- Bash shell
- Internet connection (to download routing software during setup)

## Setup Instructions

1. Run the installation script provided by the instructors.

2. Start the containers using the orchestrator:
   ```bash
   python3 orchestrator.py start
   ```

3. Configure the network using the orchestrator. This will initially route packets through the northern path:
   ```bash
   python3 orchestrator.py configure
   ```

4. Swap between the north and south routes:
   ```bash
   python3 orchestrator.py route [north|south]
   ```

5. Stop the containers:
   ```bash
   python3 orchestrator.py stop
   ```


