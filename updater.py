import paramiko
import json
from datetime import datetime
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "nodes.json"
LOG_FILENAME = Path(__file__).parent / "update_log.txt"

def load_nodes(config_path):
    try:
        with open(config_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading config file: {e}")
        return []

def update_node(node, log_file):
    log_file.write(f"\n--- Connecting to {node['host']} ---\n")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=node["host"],
            username=node["username"],
            key_filename=node["key_filename"]
        )

        commands = [
            "DEBIAN_FRONTEND=noninteractive apt-get update -y",
            "DEBIAN_FRONTEND=noninteractive apt-get upgrade -y"
        ]

        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()

            log_file.write(f"\nRunning: {command}\n{output}")
            if error:
                log_file.write(f"Error:\n{error}\n")

        client.close()

    except Exception as e:
        log_file.write(f"[FAILED to connect to {node['host']}]: {e}\n")

def main():
    nodes = load_nodes(CONFIG_PATH)

    if not nodes:
        print("No nodes found in configuration. Exiting.")
        return

    with open(LOG_FILENAME, "a") as log_file:
        log_file.write(f"\n=== Update Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        for node in nodes:
            update_node(node, log_file)

if __name__ == "__main__":
    main()
