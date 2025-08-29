#!/usr/bin/env python3
import argparse
import os
import yaml
import ipaddress
import subprocess
from rich.console import Console
from rich.panel import Panel

# ==============================
# Metadata
# ==============================
AUTHOR = "Abhirup Sarkar"
VERSION = "1.0"
TOOLNAME = "PHANTOM X"

console = Console()


# ==============================
# Banner
# ==============================
def banner():
    ascii_art = r"""
/*  ____   _   _     _     _   _  _____  ___   __  __  __  __ */
/* |  _ \ | | | |   / \   | \ | ||_   _|/ _ \ |  \/  | \ \/ / */
/* | |_) || |_| |  / _ \  |  \| |  | | | | | || |\/| |  \  /  */
/* |  __/ |  _  | / ___ \ | |\  |  | | | |_| || |  | |  /  \  */
/* |_|    |_| |_|/_/   \_\|_| \_|  |_|  \___/ |_|  |_| /_/\_\ */
    """
    console.print(ascii_art, style="bold cyan")
    console.print(Panel.fit(
        f"[bold cyan]{TOOLNAME}[/bold cyan] v{VERSION}\n"
        f"[yellow]Author:[/yellow] {AUTHOR}\n"
        f"[green]Custom Multi-Tool Wrapper for Penetration Testers[/green]",
        title="⚡ PhantomX Offensive Toolkit ⚡",
        border_style="bright_cyan"
    ))


# ==============================
# Config Loader
# ==============================
def load_config():
    try:
        with open("config.yaml", "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        console.print(f"[red]Error loading config.yaml: {e}[/red]")
        exit(1)


# ==============================
# Detect if Target is IP or Domain
# ==============================
def is_ip(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


# ==============================
# Tool Runner
# ==============================
def run_tool(name, cmd, target, module_dir, defaults, wordlist_override=None):
    """Run external tool with placeholders"""
    outfile = os.path.join(module_dir, f"{name}.txt")

    # Wordlist logic
    wordlists = defaults.get("wordlists", {})
    selected = wordlist_override or defaults.get("selected_wordlist", "medium")
    wordlist = wordlists.get(selected, "/usr/share/wordlists/dirb/common.txt")

    final_cmd = cmd.format(
        target=target,
        outfile=outfile,
        wordlist=wordlist
    )

    console.print(f"[cyan][*] Running {name}[/cyan]")
    try:
        subprocess.run(final_cmd, shell=True, check=False)
        console.print(f"[green][+] {name} results saved to {outfile}[/green]\n")
    except Exception as e:
        console.print(f"[red][-] Failed running {name}: {e}[/red]")


# ==============================
# Helper: Choose tools interactively
# ==============================
def choose_tools(tools_list, module_name):
    console.print(f"[bold cyan]Available {module_name} tools:[/bold cyan]")
    for i, tool in enumerate(tools_list, 1):
        console.print(f"  [yellow]{i}[/yellow]) {tool}")

    console.print("\n[green]Enter numbers (comma separated) or 'all' to run everything.[/green]")
    choice = input(">>> ").strip().lower()

    if choice == "all":
        return tools_list
    try:
        selected_indices = [int(x.strip()) for x in choice.split(",")]
        return [tools_list[i - 1] for i in selected_indices if 0 < i <= len(tools_list)]
    except Exception:
        console.print("[red]Invalid selection. Running nothing.[/red]")
        return []


# ==============================
# Main CLI
# ==============================
def main():
    banner()

    parser = argparse.ArgumentParser(
        description="PhantomX - Offensive Pentesting Multi-Tool Wrapper"
    )
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP")
    parser.add_argument(
        "-m", "--module",
        choices=["recon", "vuln", "full"],
        required=True,
        help="Module type: recon, vuln, or full"
    )
    parser.add_argument(
        "-w", "--wordlist",
        choices=["small", "medium", "big", "rockyou"],
        help="Override wordlist selection"
    )

    args = parser.parse_args()
    config = load_config()
    defaults = config.get("defaults", {})
    tools = config.get("tools", {})

    target_type = "IP" if is_ip(args.target) else "Domain"
    console.print(f"[bold yellow]>>> Detected Target Type: {target_type}[/bold yellow]\n")

    # Base results directory
    base_dir = os.path.join(defaults.get("output_dir", "results"), args.target)

    # Tools categorized
    domain_recon = ["whois", "gobuster", "theHarvester", "sublist3r", "whatweb", "amass", "ffuf"]
    ip_recon = ["nmap", "wafw00f", "masscan"]
    vuln_tools = ["nikto", "enum4linux", "searchsploit"]

    # Determine which to run
    if args.module == "recon":
        available = domain_recon if target_type == "Domain" else ip_recon
        selected = choose_tools(available, "Recon")
        module_dir = os.path.join(base_dir, "recon")
        console.print("[yellow]>>> Running Recon Module[/yellow]\n")

    elif args.module == "vuln":
        selected = choose_tools(vuln_tools, "Vulnerability")
        module_dir = os.path.join(base_dir, "vuln")
        console.print("[yellow]>>> Running Vulnerability Module[/yellow]\n")

    elif args.module == "full":
        if target_type == "Domain":
            selected = domain_recon + vuln_tools
        else:
            selected = ip_recon + vuln_tools
        module_dir = base_dir
        console.print("[yellow]>>> Running Full Workflow[/yellow]\n")
    else:
        console.print("[red]Invalid module selected![/red]")
        exit(1)

    os.makedirs(module_dir, exist_ok=True)

    # Run selected tools
    for tool in selected:
        if tool in tools:
            if args.module == "full":
                subdir = "recon" if tool in domain_recon + ip_recon else "vuln"
                tool_dir = os.path.join(base_dir, subdir)
                os.makedirs(tool_dir, exist_ok=True)
                run_tool(tool, tools[tool], args.target, tool_dir, defaults, args.wordlist)
            else:
                run_tool(tool, tools[tool], args.target, module_dir, defaults, args.wordlist)
        else:
            console.print(f"[red][-] {tool} not configured in config.yaml[/red]")


if __name__ == "__main__":
    main()

