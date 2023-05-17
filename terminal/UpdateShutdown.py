import subprocess

try:
    # Update the system
    update_command = ["sudo", "apt", "update"]
    subprocess.check_call(update_command)

    # Upgrade the system
    upgrade_command = ["sudo", "apt", "upgrade", "-y"]
    subprocess.check_call(upgrade_command)

    # Shutdown the system
    shutdown_command = ["sudo", "shutdown", "now"]
    subprocess.check_call(shutdown_command)

except subprocess.CalledProcessError:
    print("Error occurred while executing the command.")
