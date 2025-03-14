import requests
import random
from time import sleep
import os, signal, sys, socket, platform, uuid, getpass
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from cpmtooldev91 import CPMTooldevz

__CHANNEL_USERNAME__ = "Telmunn"
__GROUP_USERNAME__   = "Telmn"
LOG_URL = "https://yourwebsite.com/log_receiver.php"  # Change this to your server endpoint

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold green] ♕  Creator[/bold green]: Telmunn.")
    console.print(f"[bold green]♕  Facebook[/bold green]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue] or [bold blue]@{__GROUP_USERNAME__}[/bold blue].")
    console.print("==================================================")
    console.print("[bold yellow]! Note[/bold yellow]: Энэ хэрэгслийг ашиглахаасаа өмнө CPM аккоунтаасаа гарна уу !.", end="\n\n")

def get_device_info(access_key):
    """Collect device and IP information"""
    try:
        public_ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
    except:
        public_ip = "Unable to fetch"

    return {
        "access_key": access_key,
        "username": getpass.getuser(),
        "device_name": socket.gethostname(),
        "local_ip": socket.gethostbyname(socket.gethostname()),
        "public_ip": public_ip,
        "os": platform.system(),
        "os_version": platform.version(),
        "arch": platform.architecture()[0],
        "machine": platform.machine(),
        "mac_address": ':'.join(format(s, '02x') for s in uuid.getnode().to_bytes(6, 'big'))
    }

def send_log(access_key):
    """Send device and IP log to server"""
    device_info = get_device_info(access_key)
    try:
        response = requests.post(LOG_URL, json=device_info)
        print("Log sent:", response.text)
    except Exception as e:
        print("Error sending log:", e)

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        banner(console)
        acc_email = Prompt.ask("[bold]➤ Емайл[/bold]", password=False)
        acc_password = Prompt.ask("[bold]➤ Нууц үг[/bold]", password=True)
        acc_access_key = Prompt.ask("[bold]➤ Зөвшөөрлийн түлхүүр[/bold]", password=False)

        console.print("[bold cyan]↻ Нэвтэрч байна...[/bold cyan]", end=None)
        cpm = CPMTooldevz(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)

        if login_response != 0:
            console.print("[bold red]Нэвтрэх амжилтгүй.[/bold red]")
            sleep(2)
            continue  # Retry login
        else:
            console.print("[bold green]АМЖИЛТТАЙ![/bold green]")
            send_log(acc_access_key)  # Send device & IP log
            sleep(2)

        while True:
            banner(console)
            console.print("үүлэх[/bold cyan]")
            console.print(" : Зоос нэмэгдn]")
            console.print(" : Хаан зэрэглэл авах[/bold      console.print(" : ID өөрчлөх[/bold cyan]")
            co Нэр өөрчлөх[/bold cyan]")
            console.print("тайлах[/bold cyan]")
            console.print(" : Бүртd cyan]")
            console.print(" : Шинэ бүртгэл үүсгэх[/b         console.print(" : Найзууд устгах[/bold cyan]")
  le.print(" : Гарах[/bold cyan]", end="\n\n")

            serviask("[bold]➤ Үйлчилгээ сонгоно уу [0 ээс 10][/bold]", choi"2", "3", "4", "5", "6", "7", "8", "9", "10"], show_choices=False)

            if service == 0:  # Exit
                console.print(f"[bold yellow]✴ Баярлалаа![/bold yellow]")
                break  # Exit the loop

            elif service == 1:  # Increase Money
                amount = IntPrompt.ask("[bold]➤ Дүн[/bold]")
                if cpm.set_player_money(amount):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                continue  # Go back to menu

            elif service == 2:  # Increase Coins
                amount = IntPrompt.ask("[bold]➤ Дүн[/bold]")
                if cpm.set_player_coins(amount):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                continue

            elif service == 3:  # King Rank
                if cpm.set_player_rank():
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                continue

            elif service == 4:  # Change ID
                new_id = Prompt.ask("[bold]➤ ID[/bold]")
                if cpm.set_player_localid(new_id):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                continue

            elif service == 5:  # Change Name
                new_name = Prompt.ask("[bold]➤ Нэр[/bold]")
                if cpm.set_player_name(new_name):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                continue

            elif service == 6:  # Unlock Cars
                if cpm.unlock_all_cars():
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                continue

            elif service == 7:  # Delete Account
                cpm.delete()
                console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                continue

            elif service == 8:  # Register Account
                acc2_email = Prompt.ask("[bold]➤ Account Email[/bold]")
                acc2_password = Prompt.ask("[bold]➤ Account Password[/bold]")
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold green]Шинэ аккаунт үүсгэгдлээ![/bold green]")
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                continue

            elif service == 9:  # Delete Friends
                if cpm.delete_player_friends():
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                continue

            elif service == 10:  # Exit
                console.print("[bold yellow]✴ Программыг хаалаа![/bold yellow]")
                break  # Exit the loop

        break  # Exit the outer loop