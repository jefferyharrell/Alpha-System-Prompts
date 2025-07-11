#!/usr/bin/env python3
"""Template rendering script for Alpha System Prompts."""

import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def get_version() -> str:
    """Load version from __version__.py."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("version", "__version__.py")
    version_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(version_module)
    return version_module.__version__


def render_template(template_name: str, output_path: str):
    """Render a Jinja2 template and write the output."""
    # Set up Jinja2 environment with the current directory as the base
    env = Environment(loader=FileSystemLoader('.'))
    
    # Load version
    version = get_version()
    
    # Load and render the template with version context
    template = env.get_template(f'output_templates/{template_name}')
    rendered = template.render(version=version)
    
    # Write the output
    output_file = Path(output_path)
    output_file.write_text(rendered)
    print(f"Rendered {template_name} -> {output_path} (v{version})")


def main():
    if len(sys.argv) != 3:
        print("Usage: python render.py <template_name> <output_path>")
        print("Example: python render.py claude_code.j2 claude_code_prompt.md")
        sys.exit(1)
    
    template_name = sys.argv[1]
    output_path = sys.argv[2]
    
    render_template(template_name, output_path)


if __name__ == "__main__":
    main()