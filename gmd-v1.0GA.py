#!/usr/bin/env python3
import os
import sys
import argparse
import re
from pathlib import Path
from datetime import datetime

# UI and Logic
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style as PTStyle
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import Condition

# Rendering
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.panel import Panel

# --- CONFIGURATION ---
NOTES_DIR = Path.home() / ".gmd_notes"
NOTES_DIR.mkdir(parents=True, exist_ok=True)

console = Console(color_system="truecolor", force_terminal=True)

pt_style = PTStyle.from_dict({
    'prompt': '#00ffaf bold',
    'bottom-toolbar': 'bg:#222222 #00ffaf',
    'bottom-toolbar.text': '#eeeeee',
    'bottom-toolbar.status': 'bg:#005faf #eeeeee bold', 
})

# --- v1.0GA PALETTE ENGINE ---
class PaletteEngine:
    def __init__(self, init_data):
        if any(isinstance(i, list) for i in init_data):
            self.palettes = init_data
        else:
            self.palettes = [init_data]
        self.current_set_idx = 0
        self.load_local_palette()

    @property
    def current_set(self):
        return self.palettes[self.current_set_idx]

    def next_set(self):
        if len(self.palettes) > 1:
            self.current_set_idx = (self.current_set_idx + 1) % len(self.palettes)

    def prev_set(self):
        if len(self.palettes) > 1:
            self.current_set_idx = (self.current_set_idx - 1) % len(self.palettes)

    def load_from_file(self, path):
        p = Path(path)
        if p.exists():
            try:
                content = p.read_text(encoding="utf-8").splitlines()
                new_sets = [list(line.strip()) for line in content if line.strip()]
                if new_sets:
                    self.palettes = new_sets
                    self.current_set_idx = 0
            except Exception: pass

    def load_local_palette(self):
        pal_files = list(Path('.').glob("*.pal"))
        if pal_files:
            self.load_from_file(pal_files[0])

# --- DATA ---
ICONS = ["🚀", "💡", "🔥", "🛠️", "📝", "✅", "⚠️", "🧠", "📦", "🌐", "🔒", "🎨"]

SNIPPETS = {
    "H1": "# Header 1",
    "H2": "## Header 2",
    "Bold": "**Bold Text**",
    "Italic": "*Italic Text*",
    "Code": "```python\n# Code Block\nprint('Hello World')\n```",
    "Link": "[Title](https://url.com)",
    "Table": "| Head | Head |\n|---|---|\n| Cell | Cell |",
    "List": "* Item 1\n* Item 2",
    "Quote": "> Blockquote",
    "Rule": "---"
}
SNIPPET_KEYS = list(SNIPPETS.keys())

class GMD:
    def __init__(self):
        self.kb = KeyBindings()
        self.palette = PaletteEngine(ICONS)
        self.show_palette = False
        self.show_snippets = False
        self.palette_index = 0
        self.snippet_index = 0
        self.status_message = ""
        self._setup_keybindings()
        
        self.session = PromptSession(
            style=pt_style, 
            key_bindings=self.kb,
            bottom_toolbar=self._get_toolbar,
            mouse_support=True
        )

    def _setup_keybindings(self):
        @self.kb.add('c-p')
        def _(event):
            self.status_message = ""
            self.show_palette = not self.show_palette
            self.show_snippets = False 
            
        @self.kb.add('c-l')
        def _(event):
            self.status_message = ""
            self.show_snippets = not self.show_snippets
            self.show_palette = False 

        @self.kb.add('[', filter=Condition(lambda: self.show_palette))
        def _(event):
            self.palette.prev_set(); self.palette_index = 0

        @self.kb.add(']', filter=Condition(lambda: self.show_palette))
        def _(event):
            self.palette.next_set(); self.palette_index = 0

        @self.kb.add('right', filter=Condition(lambda: self.show_palette or self.show_snippets))
        def _(event):
            if self.show_palette:
                self.palette_index = (self.palette_index + 1) % len(self.palette.current_set)
            else:
                self.snippet_index = (self.snippet_index + 1) % len(SNIPPET_KEYS)

        @self.kb.add('left', filter=Condition(lambda: self.show_palette or self.show_snippets))
        def _(event):
            if self.show_palette:
                self.palette_index = (self.palette_index - 1) % len(self.palette.current_set)
            else:
                self.snippet_index = (self.snippet_index - 1) % len(SNIPPET_KEYS)

        @self.kb.add('enter', filter=Condition(lambda: self.show_palette or self.show_snippets))
        def _(event):
            if self.show_palette:
                event.current_buffer.insert_text(self.palette.current_set[self.palette_index])
                self.show_palette = False
            else:
                key = SNIPPET_KEYS[self.snippet_index]
                event.current_buffer.insert_text(SNIPPETS[key])
                self.show_snippets = False

    def _get_toolbar(self):
        if self.status_message:
            return [('class:bottom-toolbar.status', f" {self.status_message} ")]
        if self.show_palette:
            cur_set = self.palette.current_set
            self.palette_index %= len(cur_set)
            parts = [f" >{icon}< " if i == self.palette_index else f" {icon} " for i, icon in enumerate(cur_set)]
            page_info = f" [{self.palette.current_set_idx + 1}/{len(self.palette.palettes)}]"
            return f"ICONS{page_info}: {''.join(parts)} | [ [ ] Nav | [Enter] Punch"
        if self.show_snippets:
            parts = [f" >{k}< " if i == self.snippet_index else f" {k} " for i, k in enumerate(SNIPPET_KEYS)]
            return f"SNIPPETS: {''.join(parts)} | [Enter] Insert Snippet"
        return " [Ctrl+P] Icons | [Ctrl+L] MD Library | [Esc+Enter] Save"

    def _resolve_path(self, path_str: str) -> Path:
        path = Path(path_str)
        if not path.is_file() and (NOTES_DIR / path_str).exists():
            return NOTES_DIR / path_str
        return path

    def list_notes(self):
        notes = sorted(NOTES_DIR.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
        table = Table(title=f"GMD Archive: {NOTES_DIR}", title_style="bold cyan", border_style="dim")
        table.add_column("Filename", style="green"); table.add_column("Modified", style="dim"); table.add_column("Title", style="bold white")
        for path in notes:
            mtime = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
            title = path.stem.split('_', 2)[-1].replace('_', ' ').title()
            table.add_row(path.name, mtime, title)
        console.print(table)

    def read_note(self, path_str: str):
        path = self._resolve_path(path_str)
        if not path.exists() or not path.is_file():
            console.print(f"[bold red]Error:[/] Path '{path_str}' not found."); return
        content = path.read_text(encoding="utf-8")
        os.environ["LESS"] = "-R -F -X"
        with console.pager(styles=True):
            md = Markdown(content, code_theme="monokai")
            console.print(Panel(md, title=f"[bold cyan]{path.name}[/]", border_style="green", padding=(1, 2)))

    def create_note(self, title: str):
        console.print(f"[bold green]New Note:[/] {title}")
        content = self.session.prompt("> ", multiline=True)
        if not content.strip(): return
        fn = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{title.lower().replace(' ', '_')}.md"
        path = NOTES_DIR / fn
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{content}")
        console.print(f"✔ [bold green]Created:[/] {path}")

    def create_file_at_path(self, path_str: str):
        path = Path(path_str).resolve()
        parents_needed = not path.parent.exists()
        file_needed = not path.exists()
        
        actions = []
        if parents_needed: actions.append(f"Create path: {path.parent}")
        if file_needed: actions.append(f"Create file: {path.name}")
        
        if not actions:
            self.edit_note(str(path)); return

        self.status_message = f"{' | '.join(actions)} -- Proceed? (y/n)"
        
        choice = self.session.prompt("").strip().lower()
        if choice == 'y':
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
            self.status_message = "" 
            self.edit_note(str(path))
        else:
            self.status_message = ""
            console.print("[yellow]Aborted.[/]")

    def edit_note(self, path_str: str):
        path = self._resolve_path(path_str)
        if not path.exists():
            console.print(f"[bold red]Error:[/] Path '{path_str}' not found."); return
        content_lines = path.read_text(encoding="utf-8").splitlines()
        body = "\n".join(content_lines[3:]) if len(content_lines) > 3 else "\n".join(content_lines)
        console.print(f"[bold green]Editing:[/] {path.name}")
        new_body = self.session.prompt(default=body, multiline=True)
        header = content_lines[0] if content_lines else "# Untitled"
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"{header}\nUpdated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{new_body}")
        console.print(f"✔ [bold green]Updated:[/] {path}")

    def interactive_find(self):
        query = self.session.prompt("🔍 Find: ")
        if not query: return
        notes = NOTES_DIR.glob("*.md")
        query = query.lower()
        count = 0
        for path in notes:
            content = path.read_text(encoding="utf-8")
            if query in content.lower():
                count += 1
                console.print(f"📄 [bold green]{path.name}[/]")
                for line in content.splitlines():
                    if query in line.lower():
                        display_line = line.strip().replace(query, f"[bold yellow]{query}[/]")
                        console.print(f"  [dim]↳ {display_line}[/]")
        if count == 0: console.print("[red]No matches found.[/]")

def main():
    parser = argparse.ArgumentParser(prog="gmd")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("ls"); subparsers.add_parser("find")
    subparsers.add_parser("read").add_argument("path"); subparsers.add_parser("edit").add_argument("path")
    subparsers.add_parser("create").add_argument("path")
    new_p = subparsers.add_parser("new"); new_p.add_argument("title", nargs="+")

    args = parser.parse_args(); gmd = GMD()
    if args.command == "ls": gmd.list_notes()
    elif args.command == "find": gmd.interactive_find()
    elif args.command == "read": gmd.read_note(args.path)
    elif args.command == "edit": gmd.edit_note(args.path)
    elif args.command == "create": gmd.create_file_at_path(args.path)
    elif args.command == "new": gmd.create_note(" ".join(args.title))
    else: parser.print_help()

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: console.print("\n[bold red]Interrupted.[/]")


