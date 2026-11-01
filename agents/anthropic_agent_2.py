from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic, beta_tool

client = Anthropic()


load_dotenv()

@beta_tool
def get_password_reset_steps() -> str:
    """Returns the steps to reset a company account password."""
    return(
        "To reset your password: "
        "1. Go to https://accounts.company.com/reset. "
        "2. Enter your company email address. "
        "3. Check your email for a reset link (expires in 15 minutes). "
        "4. Follow the link and choose a new password. "
        "5. If the link does not arrive, check your span folder or contact IT."
    )

@beta_tool
def get_vpn_troubleshooting_steps() -> str:
    """Returns troubleshooting steps for VPN connection issues"""
    return(
        "VPN troubleshooting steps: "
        "1. Confirm you are connected to the internet before launching the VPN client."
        "2. Check that your VPN client is up to date - version 4.2 or later is required "
        "3. Try disconnecting and reconnecting "
        "4. If the issue persists, restart your machine and try again"
        "5. If you  are on a public network, some ports may be blocked - try a mobile hotspot."
        "6. Contact IT if the problem continues after these steps."
    )

@beta_tool
def get_software_install_guide(software_name:str) -> str:
    """Returns installation instructions for a specified software package."""
    guides = {
        "slack": "To install Slack: visit https://slack.com/downloads, download the installer for your OS",
        "zoom": "To install Zoom: visit https://zoom.us/download",
        "vscode": "To install VS Code: visit https://code.visualstudio.com"
    }
    name = software_name.lower()
    return guides.get(
        name, f"No installation guide for '{software_name}'. Please contact IT fir assistance."
    )




def main():
    querys=["what are the steps to reset my password?","my vpn is not working?", "how do i install slack?"]

    for query in querys:
        print(query)
        runner = client.beta.messages.tool_runner(
            model="claude-opus-4-6",
            max_tokens=1024,
            tools=[get_software_install_guide,get_vpn_troubleshooting_steps,get_password_reset_steps],
            messages=[{"role": "user", "content":query}],
        )
        print(runner.until_done().content)


if __name__ == "__main__":
    main()
