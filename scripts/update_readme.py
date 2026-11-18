from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START = "<!-- BEGIN GENERATED CONTENTS -->"
END = "<!-- END GENERATED CONTENTS -->"
IGNORED_DIRECTORIES = {".git", ".venv", "__pycache__"}
OVERVIEW_DIRECTORIES = ("APP", "Assignments", "Class", "Lab")


def count_files(path: Path, suffix: str) -> int:
    return sum(
        1
        for entry in path.rglob("*")
        if entry.is_file()
        and entry.suffix.casefold() == suffix
        and not any(part in IGNORED_DIRECTORIES for part in entry.parts)
    )


def build_overview() -> list[str]:
    lines = ["."]
    directories = [ROOT / name for name in OVERVIEW_DIRECTORIES if (ROOT / name).is_dir()]
    for index, directory in enumerate(directories):
        branch = "└── " if index == len(directories) - 1 else "├── "
        python_count = count_files(directory, ".py")
        notebook_count = count_files(directory, ".ipynb")
        lines.append(
            f"{branch}{directory.name}/  "
            f"({python_count} Python files · {notebook_count} notebooks)"
        )
    return lines


def update_readme() -> None:
    contents = "\n".join(["```text", *build_overview(), "```"])
    readme = README.read_text(encoding="utf-8")
    start = readme.index(START) + len(START)
    end = readme.index(END, start)
    replacement = f"\n{contents}\n"
    updated = readme[:start] + replacement + readme[end:]
    if updated != readme:
        README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
