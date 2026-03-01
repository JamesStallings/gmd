# GMD (Gemini Markdown)
Updated: 2026-02-27 09:14

### GMD : Gemini's MarkDown tool.

## Key Features
---
| Status | Feature | In Detail |
|---|---|---|
| ✅ | **Hybrid Architecture** | Combines `prompt_toolkit` for interactive editing with `rich` for professional markdown rendering |
| ✅ | **Truecolor Support** | Optimized for Alacritty and modern terminals with 24-bit color depth |
| ✅ | **Tool Pallette** | Provides a curated list of unicode icons for inclusion (ctrl+p), as well as a markdown assistant (ctrl+l) |
| ✅ | **System Integration** | Uses the native pager (`less`) for seamless scrolling and searching within long notes. |

 Usage
- `gmd ls`: List all notes in the archive.
- `gmd new <title>`: Create a new note with an interactive buffer.
- `gmd read <path>`: View rendered markdown with syntax highlighting.
- `gmd edit <path>`: Edit existing notes using the internal buffer.
- `gmd find`: Interactively search across all markdown files.

## Installation
1. Ensure you have Python 3.10+ installed.
2. Install dependencies: `pip install -r requirements.txt`
3. Alias the script or move it to your path: `chmod +x gmd.py && ln -s $(pwd)/gmd.py /usr/local/bin/gmd`

---
This tool was vibe coded by James G. Stallings II, with the heavy lifting done by Google, LLC's Gemini Large Language Model. Specifically, Gemini Pro.
It's a signatory example of what can be accomplished with these tools as long as you treat them as you would a friendly, slightly hung-over co-worker. Dont gab. Tell it what you need and keep exchanges short and concise.

This must also be curated in the model; the important thing to remember is, natural langauge and self expression are inefficient and nuanced,and as it happens, natural language os the tool to be used in 'vibe coding' with an LLM chat interface, so a careful balance must be struck. I'm not going to judge if you want a chatterbot girlfriend or some digital advisor; just dont mix it in with your development. In fact, keep your development conversations as focussed and concise as possible. Whenever it works in the prompt, try to express desires in terms of a *doublet of opposition*; that is to say, something like 'Add new feature 'X". Under no circumstances disturb 'Y' to do it".

It's also good to remember that it will likely still get it wrong and have be called on it - but giving it that instruction format is a very token efficient way of doing things, or so I'm told, and it does seem to limit *topical drift*.

The subcommand 'ls' reveals a hidden treasure: an implied journaling system. Any 'new' command creates a timestamped entry in the .gmdarchive folder. This may seem at odds with the ability to read and edit any markdown file (as long as you have file perms) but it's all in the workflow: create the file as a journal entry then copy it it out into namespace as it should be to do it's thing. Now you have an original source for the content, and the date and time it was made, right there in your journal.

I'm digging it - it's been added to another of my works in progress, which is nearing completion, and this tool really puts the polish on the project. So well, in fact, I dedcided it actually need to have it's own repo and be a thing all on its own.

Enjoy, be sure to examine the source, I had gemini populate a file with good solid inline comments for the repo.

Cheers! 🔥