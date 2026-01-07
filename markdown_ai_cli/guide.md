# 🤖 Project: Markdown-AI CLI
A command-line tool for reading, formatting, and enhancing Markdown files with the power of LLMs.

## 🎯 Learning Objectives
- **CLI Design:** Mastering arguments, flags, and subcommands.
- **File I/O:** Safely reading and writing to the local filesystem.
- **API Integration:** Handling asynchronous requests to AI providers.
- **Developer Experience (DX):** Building beautiful terminal interfaces (TUIs).

---

## 🏗️ The Roadmap & To-Do List

### Phase 1: The Foundation (Local Reader)
- [ ] Initialize project with a virtual environment (`venv`).
- [ ] Create a `view` command that opens an `.md` file.
- [ ] Render the file content beautifully in the terminal (No raw text!).
- [ ] Handle `FileNotFound` and `PermissionError` gracefully.

### Phase 2: The Brain (LLM Integration)
- [ ] Setup `.env` support for API Key security.
- [ ] Implement a `chat` or `ask` command to send file context to an LLM.
- [ ] Add a **Loading Spinner** to keep the terminal interactive during API calls.
- [ ] Implement **Streaming** (Output words as they are generated).

### Phase 3: The Editor (File Operations)
- [ ] Add an `--inplace` flag to save AI responses back to the original file.
- [ ] Create a `summarize` shortcut command.
- [ ] Implement a `config` command to save user preferences (Model type, API keys).
- [ ] **Challenge:** Support piping (e.g., `cat file.md | python main.py ask "Review this"`).

---

## 🛠️ Tech Stack (Suggested)
| Component | Library |
| :--- | :--- |
| **Logic** | Python 3.10+ |
| **CLI Framework** | `Typer` or `Click` |
| **UI/Formatting** | `Rich` |
| **AI SDK** | `OpenAI` or `Anthropic` |
| **Environment** | `python-dotenv` |
