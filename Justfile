# Alpha System Prompt Template Generator

# Install dependencies
deps:
    uv add jinja2

# Render Claude Code system prompt
claude-code: setup
    uv run python render.py claude_code.j2 output/claude_code_prompt.md

# Render Claude Desktop system prompt  
claude-desktop: setup
    uv run python render.py claude_desktop.j2 output/claude_desktop_prompt.md

# Render all prompts
all: claude-code claude-desktop

# Create output directory if it doesn't exist
setup:
    mkdir -p output

# Clean generated files
clean:
    rm -rf output/