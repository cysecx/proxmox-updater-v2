# Proxmox Updater v2

An automated Python tool to remotely update Proxmox VE nodes over SSH. Designed to simplify routine maintenance by securely connecting to multiple servers and running updates with logs stored locally.

## ✨ Features

- Connects to remote Proxmox VE nodes using SSH key authentication
- Runs system update and upgrade commands
- Logs output to a local file (`update_log.txt`)
- Works with multiple nodes defined in a JSON file

---

## 🚀 Installation

> Make sure you have Python 3.7+ and `git` installed on your server or local machine.

1. **Clone the repository and run the setup script:**

```bash
git clone https://github.com/cysecx/proxmox-updater-v2.git && cd proxmox-updater-v2 && ./install.sh


## This will:

Install all Python dependencies using pip

Create a virtual environment (optional)

Prepare the updater for use


##⚙️ Configuration

Edit the nodes.json file to define your Proxmox nodes.

[
  {
    "host": "YOUR_SERVER_IP",
    "username": "USERNAME",
    "key_filename": "PATH_TO_SSHKEY" Example: "key_filename": "/home/user/.ssh/id_rsa"
  },
  {
    "host": "YOUR_SERVER_IP",
    "username": "USERNAME",
    "key_filename": "PATH_TO_SSHKEY" #Example: "key_filename": "/home/user/.ssh/id_rsa"
 }
]


##🔐 Make sure your SSH key file exists and is readable. If the file requires a passphrase, ensure SSH agent is running or use a passphrase-less key stored securely.


##🧪 Running the Updater

Once setup is complete and your nodes.json is configured, run:

python3 main.py

This will:

Loop through each node in nodes.json

Connect via SSH using the private key

Run the system update commands (apt update && apt full-upgrade -y)

Save the output in update_log.txt "cat update_log.txt


##📦 Requirements

Installed automatically via requirements.txt:

paramiko

python-dotenv (if using environment files)

You can manually install dependencies by running:

pip install -r requirements.txt


##📝 Notes

This tool is intended for technical users and homelab admins.

Always test SSH access separately before running the script.

Recommended to run the updater using a service account or restrict root SSH access to keys only.


##📁 Directory Structure

proxmox-updater-v2/
├── main.py
├── nodes.json
├── requirements.txt
├── update_log.txt
└── install.sh


##💡 Future Improvements

Add GUI or web dashboard

Track update status per node

Email or webhook alerts for failed updates


## 📫 Contact

Maintained by @cysecx
Contributions welcome!

