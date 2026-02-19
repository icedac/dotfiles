#!/usr/bin/env python3
"""
Quarkdown Tooling Script

Installation, compilation, and preview tools for Quarkdown documents.

Usage:
    python qd_tools.py install           # Install Quarkdown
    python qd_tools.py compile <file>    # Compile a .qd file
    python qd_tools.py preview <file>    # Compile with live preview
    python qd_tools.py pdf <file>        # Export to PDF
    python qd_tools.py create <name>     # Create new project
    python qd_tools.py status            # Check installation status
"""

import subprocess
import sys
import os
import shutil
import platform
from pathlib import Path
from typing import Optional


class QuarkdownTools:
    """Quarkdown installation and compilation tools."""

    def __init__(self):
        self.system = platform.system().lower()
        self.quarkdown_cmd = self._find_quarkdown()

    def _find_quarkdown(self) -> Optional[str]:
        """Find quarkdown executable."""
        cmd = shutil.which("quarkdown")
        if cmd:
            return cmd

        # Check common installation paths
        paths = [
            "/opt/quarkdown/bin/quarkdown",
            "/usr/local/bin/quarkdown",
            os.path.expanduser("~/.local/bin/quarkdown"),
        ]

        for path in paths:
            if os.path.exists(path):
                return path

        return None

    def status(self) -> bool:
        """Check if Quarkdown is installed and show status."""
        print("=" * 50)
        print("Quarkdown Installation Status")
        print("=" * 50)

        if self.quarkdown_cmd:
            print(f"[OK] Quarkdown found: {self.quarkdown_cmd}")
            try:
                result = subprocess.run(
                    [self.quarkdown_cmd, "--version"],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print(f"     Version: {result.stdout.strip()}")
            except Exception:
                pass
            return True
        else:
            print("[X] Quarkdown not found")
            print("\nTo install, run: python qd_tools.py install")
            return False

    def install(self) -> bool:
        """Install Quarkdown based on the operating system."""
        print("Installing Quarkdown...")

        if self.quarkdown_cmd:
            print(f"Quarkdown already installed at: {self.quarkdown_cmd}")
            return True

        if self.system == "darwin":
            return self._install_macos()
        elif self.system == "linux":
            return self._install_linux()
        elif self.system == "windows":
            return self._install_windows()
        else:
            print(f"Unsupported system: {self.system}")
            return False

    def _install_macos(self) -> bool:
        """Install on macOS using Homebrew."""
        print("Detected macOS. Installing via Homebrew...")

        # Check if Homebrew is installed
        if not shutil.which("brew"):
            print("Homebrew not found. Installing Homebrew first...")
            try:
                subprocess.run(
                    '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
                    shell=True,
                    check=True
                )
            except subprocess.CalledProcessError:
                print("Failed to install Homebrew. Please install it manually.")
                return False

        try:
            print("Adding Quarkdown tap...")
            subprocess.run(
                ["brew", "install", "quarkdown-labs/quarkdown/quarkdown"],
                check=True
            )
            self.quarkdown_cmd = shutil.which("quarkdown")
            print("Quarkdown installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to install via Homebrew: {e}")
            return self._install_script()

    def _install_linux(self) -> bool:
        """Install on Linux using install script or Homebrew."""
        print("Detected Linux. Installing...")

        # Try Homebrew first if available
        if shutil.which("brew"):
            try:
                subprocess.run(
                    ["brew", "install", "quarkdown-labs/quarkdown/quarkdown"],
                    check=True
                )
                self.quarkdown_cmd = shutil.which("quarkdown")
                print("Quarkdown installed successfully!")
                return True
            except subprocess.CalledProcessError:
                pass

        return self._install_script()

    def _install_script(self) -> bool:
        """Install using the official install script."""
        print("Installing via official install script...")
        print("Note: This may require sudo privileges.")

        try:
            subprocess.run(
                'curl -fsSL https://raw.githubusercontent.com/quarkdown-labs/get-quarkdown/refs/heads/main/install.sh | sudo env "PATH=$PATH" bash',
                shell=True,
                check=True
            )
            self.quarkdown_cmd = shutil.which("quarkdown") or "/usr/local/bin/quarkdown"
            print("Quarkdown installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Installation failed: {e}")
            print("\nManual installation:")
            print("1. Download from: https://github.com/iamgio/quarkdown/releases/latest")
            print("2. Unzip and add bin/ to PATH")
            return False

    def _install_windows(self) -> bool:
        """Install on Windows using Scoop."""
        print("Detected Windows. Installing via Scoop...")

        if not shutil.which("scoop"):
            print("Scoop not found. Please install Scoop first:")
            print("  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser")
            print("  irm get.scoop.sh | iex")
            return False

        try:
            subprocess.run(["scoop", "bucket", "add", "java"], check=True)
            subprocess.run(
                ["scoop", "bucket", "add", "quarkdown",
                 "https://github.com/quarkdown-labs/scoop-quarkdown"],
                check=True
            )
            subprocess.run(["scoop", "install", "quarkdown"], check=True)
            self.quarkdown_cmd = shutil.which("quarkdown")
            print("Quarkdown installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to install via Scoop: {e}")
            return False

    def _check_java(self) -> bool:
        """Check if Java 17+ is installed."""
        java = shutil.which("java")
        if not java:
            print("Warning: Java not found. Quarkdown requires Java 17+")
            return False

        try:
            result = subprocess.run(
                ["java", "-version"],
                capture_output=True,
                text=True
            )
            version_output = result.stderr or result.stdout
            print(f"Java found: {version_output.split(chr(10))[0]}")
            return True
        except Exception:
            return False

    def compile(self, file_path: str, output_dir: str = "./output") -> bool:
        """Compile a Quarkdown file."""
        if not self._ensure_installed():
            return False

        file_path = Path(file_path).resolve()
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            return False

        if not file_path.suffix == ".qd":
            print(f"Warning: Expected .qd file, got: {file_path.suffix}")

        print(f"Compiling: {file_path}")

        try:
            cmd = [self.quarkdown_cmd, "c", str(file_path), "-o", output_dir]
            subprocess.run(cmd, check=True)
            print(f"Output saved to: {output_dir}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Compilation failed: {e}")
            return False

    def preview(self, file_path: str) -> bool:
        """Compile with live preview (watch mode + browser)."""
        if not self._ensure_installed():
            return False

        file_path = Path(file_path).resolve()
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            return False

        print(f"Starting live preview: {file_path}")
        print("Press Ctrl+C to stop")

        try:
            cmd = [self.quarkdown_cmd, "c", str(file_path), "-p", "-w"]
            subprocess.run(cmd)
            return True
        except KeyboardInterrupt:
            print("\nPreview stopped.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Preview failed: {e}")
            return False

    def pdf(self, file_path: str, output_dir: str = "./output") -> bool:
        """Export to PDF."""
        if not self._ensure_installed():
            return False

        file_path = Path(file_path).resolve()
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            return False

        print(f"Exporting to PDF: {file_path}")

        try:
            cmd = [self.quarkdown_cmd, "c", str(file_path), "--pdf", "-o", output_dir]
            subprocess.run(cmd, check=True)
            print(f"PDF saved to: {output_dir}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"PDF export failed: {e}")
            print("\nNote: PDF export requires Node.js and Puppeteer.")
            print("Install with: npm install -g puppeteer")
            return False

    def create_project(self, name: str, doc_type: str = "paged") -> bool:
        """Create a new Quarkdown project with modular structure."""
        project_dir = Path(name)

        if project_dir.exists():
            print(f"Error: Directory already exists: {project_dir}")
            return False

        print(f"Creating project: {name}")

        # Create directories
        project_dir.mkdir(parents=True)
        (project_dir / "images").mkdir()
        (project_dir / "code").mkdir()
        (project_dir / "diagrams").mkdir()

        # main.qd
        main_content = f""".theme {{paperwhite}} layout:{{latex}}
.doctype {{{doc_type}}}

.includeall
    - setup.qd
    - content.qd
"""
        (project_dir / "main.qd").write_text(main_content)

        # setup.qd
        setup_content = f""".docname {{{name.replace('_', ' ').title()}}}
.docauthor {{Author}}
.doclang {{English}}

.footer
    {name.replace('_', ' ').title()}

.center
    #! .docname
    .docauthor

---

.abstract
    Brief description of this document.

.tableofcontents
"""
        (project_dir / "setup.qd").write_text(setup_content)

        # content.qd
        content_content = """# Introduction

.loremipsum

## Background

This is your first section.

.box {Getting Started} type:{tip}
    Edit this file to add your content.

<<<

# Conclusion

Summary of your document.
"""
        (project_dir / "content.qd").write_text(content_content)

        print(f"Project created: {project_dir}")
        print("\nStructure:")
        print(f"  {name}/")
        print("    main.qd      # Entry point")
        print("    setup.qd     # Metadata & TOC")
        print("    content.qd   # Your content")
        print("    images/      # Image assets")
        print("    code/        # Code snippets")
        print("    diagrams/    # Mermaid diagrams")
        print(f"\nTo compile: python qd_tools.py preview {name}/main.qd")
        return True

    def _ensure_installed(self) -> bool:
        """Ensure Quarkdown is installed."""
        if not self.quarkdown_cmd:
            print("Quarkdown is not installed.")
            response = input("Install now? [Y/n]: ").strip().lower()
            if response in ("", "y", "yes"):
                return self.install()
            return False
        return True


def main():
    """Main entry point."""
    tools = QuarkdownTools()

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "install":
        success = tools.install()
        sys.exit(0 if success else 1)

    elif command == "status":
        success = tools.status()
        tools._check_java()
        sys.exit(0 if success else 1)

    elif command == "compile":
        if len(sys.argv) < 3:
            print("Usage: python qd_tools.py compile <file.qd> [output_dir]")
            sys.exit(1)
        output_dir = sys.argv[3] if len(sys.argv) > 3 else "./output"
        success = tools.compile(sys.argv[2], output_dir)
        sys.exit(0 if success else 1)

    elif command == "preview":
        if len(sys.argv) < 3:
            print("Usage: python qd_tools.py preview <file.qd>")
            sys.exit(1)
        success = tools.preview(sys.argv[2])
        sys.exit(0 if success else 1)

    elif command == "pdf":
        if len(sys.argv) < 3:
            print("Usage: python qd_tools.py pdf <file.qd> [output_dir]")
            sys.exit(1)
        output_dir = sys.argv[3] if len(sys.argv) > 3 else "./output"
        success = tools.pdf(sys.argv[2], output_dir)
        sys.exit(0 if success else 1)

    elif command == "create":
        if len(sys.argv) < 3:
            print("Usage: python qd_tools.py create <project_name> [paged|slides|plain]")
            sys.exit(1)
        doc_type = sys.argv[3] if len(sys.argv) > 3 else "paged"
        success = tools.create_project(sys.argv[2], doc_type)
        sys.exit(0 if success else 1)

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
