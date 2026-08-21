from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START = "<!-- BEGIN GENERATED CONTENTS -->"
END = "<!-- END GENERATED CONTENTS -->"
IGNORED_DIRECTORIES = {".git", ".venv", "__pycache__"}


def display_name(path: Path) -> str:
    return path.name + ("/" if path.is_dir() else "")


def build_tree(path: Path, prefix: str = "") -> list[str]:
    entries = sorted(
        (
            entry
            for entry in path.iterdir()
            if entry.name != "README.md"
            and not (entry.is_dir() and entry.name in IGNORED_DIRECTORIES)
        ),
        key=lambda entry: (entry.is_file(), entry.name.casefold()),
    )
    lines = []
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        branch = "└── " if is_last else "├── "
        lines.append(f"{prefix}{branch}{display_name(entry)}")
        if entry.is_dir():
            child_prefix = prefix + ("    " if is_last else "│   ")
            lines.extend(build_tree(entry, child_prefix))
    return lines


def update_readme() -> None:
    contents = "\n".join(["```text", ".", *build_tree(ROOT), "```"])
    readme = README.read_text(encoding="utf-8")
    start = readme.index(START) + len(START)
    end = readme.index(END, start)
    replacement = f"\n{contents}\n"
    updated = readme[:start] + replacement + readme[end:]
    if updated != readme:
        README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    update_readme()