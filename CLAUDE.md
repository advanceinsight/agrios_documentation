# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the official documentation repository for **AgriOS**, an open-source agritech platform for managing farm operations. The documentation is built with Sphinx and hosted on Read the Docs.

## Build Commands

All commands are run from the `docs/` directory:

```bash
cd docs

# Build HTML documentation
make html

# Clean build artifacts
make clean

# View all available Sphinx targets
make help
```

Output is generated in `docs/build/html/`.

## Dependencies

Install documentation dependencies:
```bash
pip install -r docs/requirements.txt
```

Key dependencies: `sphinx`, `furo` (theme), `myst-parser` (Markdown support)

## Documentation Structure

```
docs/source/
├── index.rst           # Main entry point with toctree
├── conf.py             # Sphinx configuration
├── _static/            # Logos, custom CSS
├── user/               # End-user guides (farmers, sales, inventory, etc.)
├── implementer/        # Deployment and implementation guides
├── database/           # Installation, hosting, versioning
├── developer/          # Developer docs, Odoo integration, module reference
├── partner/            # Partner information
└── other/              # Changelog, roadmap
```

## Writing Documentation

- **Both RST and Markdown are supported** - the `myst_parser` extension enables Markdown
- New pages must be added to the appropriate `toctree` in `index.rst` or a parent file
- Theme is **Furo** with custom CSS in `_static/css/custom.css`
- Brand colors: `#458A77` (light mode), `#5FD0B0` (dark mode)

## Deployment

Documentation automatically deploys to Read the Docs on push to `main`. Configuration is in `.readthedocs.yaml`.
