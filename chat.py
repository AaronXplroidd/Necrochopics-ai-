# necrochopics/chat.py

from rich.console import Console
from rich.panel import Panel
from necrochopics.utils import clear, autocorrect, progress_bar, log_error
from necrochopics.ai_client import kirim_ke_ai
from necrochopics.config import MAX_HISTORY

console = Console()

def mulai_chat():
    clear()
    console.print(Panel("[bold blue]Necrochopics.AI[/bold blue] - [green]CLI Artificial by legendryou[/green]", width=60))
    console.print("[dim]Ketik 'exit' untuk keluar, 'reset' untuk hapus riwayat.\n[/dim]")

    history = []

    while True:
        try:
            user_input = console.input("[bold yellow]YOU:[/] ").strip()
            if user_input.lower() in ["exit", "stop", "keluar"]:
                console.print("\n[bold red][!] Sesi dihentikan oleh user. Terima kasih dan sampai jumpa![/bold red]\n")
                break
            if user_input.lower() == "reset":
                history.clear()
                console.print("[green][Info] Riwayat chat telah di-reset.[/green]\n")
                continue
            if not user_input:
                continue

            user_input = autocorrect(user_input)
            history.append({"role": "user", "content": user_input})
            if len(history) > MAX_HISTORY * 2:
                history = history[-MAX_HISTORY * 2:]

            console.print("[bold cyan]AI:[/] Processing... 🚀")
            progress_bar("Tunggu Sebentar...")

            jawaban = kirim_ke_ai(history)
            console.print(Panel(jawaban, title="Necrochopics", subtitle="Jawaban", style="bold green"))
            history.append({"role": "assistant", "content": jawaban})

        except KeyboardInterrupt:
            console.print("\n\n[bold red][!] Session has bern stopped(Ctrl+C). sayonaraa![/bold red]")
            break
        except Exception as e:
            log_error(f"Loop error: {e}")
            console.print(f"\n[bold red][!] Eror 403, unknown:[/] {e}\n")
