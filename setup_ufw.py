import subprocess
import sys
import os

def run_command(command):
    print(f"Executing: {' '.join(command)}")
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(f"Error output: {result.stderr}", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

def main():
    if os.geteuid() != 0:
        print("This script must be run as root to configure UFW.")
        print("Here are the commands that would be executed:")
        print("  sudo ufw default deny incoming")
        print("  sudo ufw default allow outgoing")
        print("  sudo ufw allow 22/tcp")
        print("  sudo ufw allow 80/tcp")
        print("  sudo ufw allow 8082/tcp")
        print("  sudo ufw --force enable")
        print("  sudo ufw status verbose")
        sys.exit(1)

    print("=== Configuring UFW Firewall ===")
    # Set default policies
    run_command(["ufw", "default", "deny", "incoming"])
    run_command(["ufw", "default", "allow", "outgoing"])

    # Allow specific ports
    run_command(["ufw", "allow", "22/tcp"])
    run_command(["ufw", "allow", "80/tcp"])
    run_command(["ufw", "allow", "8082/tcp"])

    # Enable UFW
    run_command(["ufw", "--force", "enable"])

    # Verify status
    print("\n=== UFW Configuration Status ===")
    run_command(["ufw", "status", "verbose"])

if __name__ == "__main__":
    main()