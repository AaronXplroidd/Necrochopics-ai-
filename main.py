import sys

def run_cli():
    from necrochopics.chat import mulai_chat
    mulai_chat()

def run_gui():
    from gui import ChatApp
    ChatApp().run()

if __name__ == "__main__":
    mode = "cli"
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()

    if mode == "gui":
        run_gui()
    else:
        run_cli()
