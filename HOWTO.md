# GMD: The Practitioner’s Manual (v1.0GA)

## [OVERVIEW]
**Gemini’s MarkDown (GMD)** is a high-fidelity, identity-blind markdown environment. It is designed to be a "ghost" in your system—inheriting its authority from your environment and staying out of the way of your data.



## [CORE_COMMANDS]
* `ls`: Lists the archive with temporal sorting.
* `new [title]`: Generates a sequence-safe, timestamped note.
* `edit [path/filename]`: Opens an existing file for modification.
* `read [path/filename]`: Paged, high-contrast rendering of content.
* `find`: Deep-text search across the local archive.
* `create [path/to/file]`: Recursive directory and file initialization with a safety interlock.

---

## [THE_POWER_OF_TEMPORAL_COLLISION]
The most potent feature of GMD is not a complex database—it is a side effect of the `new` command’s filename structure:
`YYYYMMDD_HHMMSS_title.md`

Because GMD resolves filenames down to the **second**, the system treats every execution as an atomic event. This allows for **Multi-Stream Log Management** without any additional code overhead. It is not what the code does; it is how you use the side effect.

### Strategic Use Cases:
1.  **Project Pulse**: Run `gmd new dev_log` every time you hit a milestone. You end up with a chronological trail of your logic without ever having to "manage" versions.
2.  **Research Streams**: Use the same title (e.g., `research_notes`) for different sessions. The timestamping naturally stacks them in your `ls` view, providing a perfect audit trail of discovery.
3.  **Work/Timekeeping**: Fire `gmd new shift_start` and `gmd new shift_end`. The filesystem does the heavy lifting of tracking your hours; GMD simply provides the interface.



---

## [THE_PALETTE_ENGINE]
GMD v1.0GA introduces the **Fluid Palette**. It adapts to your workflow via `.pal` files.

### Usage Tips:
* **Customization**: Create a `workflow.pal` in your directory. Each line becomes a "page" in your `Ctrl+P` menu.
* **Geometry**: GMD is geometry-agnostic. If a line in your `.pal` file has 4 icons or 40, the UI scales to match.
* **Navigation**: Use `[` and `]` to flip through pages of icons. It is designed for rapid muscle memory.

---

## [SAFE_RECURSION: THE 'CREATE' COMMAND]
When using `gmd create`, the system performs a pre-flight check. If you are about to create a deep directory structure (e.g., `projects/2026/march/notes.md`), GMD will pause and present the plan in the **Deep Blue** status bar.

* **Confirm with 'y'**: Commits the path and jumps straight to the editor.
* **Abort with 'n'**: Clears the bar and leaves your filesystem untouched. 

---

## [PRO_TIPS_FOR_EFFICIENCY]
* **Mouse Support**: You can click to position the cursor or drag to select text within the editor.
* **The Snippet Library**: Use `Ctrl+L` to access the Markdown Library. It’s faster than typing table or code block syntax manually.
* **Identity Anonymity**: GMD stores notes in `~/.gmd_notes` by default, but it will always prioritize local `.pal` files in your current working directory. Use this to create "Project Zones" that carry their own iconography.
