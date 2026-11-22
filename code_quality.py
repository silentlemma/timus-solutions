#!/usr/bin/env python3
"""Run native checks and comment-preserving formatters for the public archive."""

import argparse
from collections import Counter
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
import io
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import tarfile
import uuid

ROOT = Path(__file__).resolve().parent
LANGUAGES = {".cpp": "cpp", ".go": "go", ".java": "java", ".py": "python", ".rs": "rust"}
TOOLS = {
    "golangci-lint": "GOLANGCI_LINT",
    "clang-format": "CLANG_FORMAT",
    "gofmt": "GOFMT",
    "ruff": "RUFF",
    "rustfmt": "RUSTFMT",
    "g++": "CXX",
    "go": "GO",
    "javac": "JAVAC",
    "rustc": "RUSTC",
}
FORMATTERS = {
    "cpp": "clang-format",
    "java": "clang-format",
    "go": "gofmt",
    "python": "ruff",
    "rust": "rustfmt",
}
CHECKERS = {"cpp": "g++", "java": "javac", "go": "golangci-lint", "python": "ruff", "rust": "rustc"}


@contextmanager
def exclusive_run(work):
    with (work / "run.lock").open("a+b") as handle:
        handle.seek(0, 2)
        if handle.tell() == 0:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        if os.name == "nt":
            import msvcrt

            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            if os.name == "nt":
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle, fcntl.LOCK_UN)


def docker_run(args):
    docker = shutil.which("docker")
    if not docker:
        raise ValueError("Docker is required.")
    definition = ROOT / "tools" / "code_quality"
    fingerprint = sha256(
        b"".join((definition / n).read_bytes() for n in ("Dockerfile", "requirements.txt"))
    ).hexdigest()[:16]
    image = "timus-code-quality:" + fingerprint
    work = args.root.resolve() / ".run" / "code-quality"
    work.mkdir(parents=True, exist_ok=True)
    with exclusive_run(work):
        run_id = uuid.uuid4().hex
        selected = collect(args.root.resolve(), args.problems, args.languages)
        if not selected:
            raise ValueError("No source files selected.")
        (work / "selected.json").write_text(
            json.dumps([p.relative_to(args.root.resolve()).as_posix() for p in selected]),
            encoding="utf8",
        )
        before = {}
        archive = work / "sources.tar"
        with tarfile.open(archive, "w") as output:
            for path in selected + [
                args.root.resolve() / n for n in (".clang-format", "ruff.toml")
            ]:
                data = path.read_bytes()
                name = path.relative_to(args.root.resolve()).as_posix()
                before[name] = sha256(data).hexdigest()
                entry = tarfile.TarInfo(name)
                entry.size = len(data)
                output.addfile(entry, io.BytesIO(data))
        exists = subprocess.run(
            [docker, "image", "inspect", image],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if exists.returncode:
            subprocess.run(
                [
                    docker,
                    "build",
                    "--platform",
                    "linux/amd64",
                    "-t",
                    image,
                    "-f",
                    str(definition / "Dockerfile"),
                    str(ROOT),
                ],
                check=True,
            )
        cache_volume = "timus-quality-" + sha256(str(ROOT).encode()).hexdigest()[:12]
        command = [
            docker,
            "run",
            "--rm",
            "--platform",
            "linux/amd64",
            "--network",
            "none",
            "--read-only",
            "--cpus",
            "1",
            "--memory",
            "1g",
            "--pids-limit",
            "128",
            "--tmpfs",
            "/tmp:rw,exec,size=256m",
            "--tmpfs",
            "/workspace:rw,size=128m",
            "--mount",
            "type=bind,source=" + str(work) + ",target=/reports",
            "--mount",
            "type=volume,source=" + cache_volume + ",target=/cache",
            "--mount",
            "type=bind,source="
            + str(ROOT / "code_quality.py")
            + ",target=/quality/code_quality.py,readonly",
            "--mount",
            "type=bind,source="
            + str(definition / "comment_language.py")
            + ",target=/quality/comment_language.py,readonly",
            "-e",
            "RUFF_CACHE_DIR=/cache/ruff",
            "-e",
            "GOCACHE=/cache/go",
            "-e",
            "GOLANGCI_LINT_CACHE=/cache/golangci",
            image,
            "python",
            "/quality/code_quality.py",
            args.mode,
        ]
        command += (
            args.problems
            + [
                "--inside",
                "--archive",
                "/reports/sources.tar",
                "--selected",
                "/reports/selected.json",
                "--root",
                "/workspace",
                "--languages",
            ]
            + args.languages
        )
        command += ["--jobs", str(args.jobs)]
        command += ["--run-id", run_id]
        code = subprocess.run(command).returncode
        for name, digest in before.items():
            if sha256((args.root.resolve() / name).read_bytes()).hexdigest() != digest:
                raise ValueError("Sources changed while checking: " + name)
        report_path = work / (args.mode + "-report.json")
        if code not in (0, 1) or not report_path.exists():
            return code or 2
        report = json.loads(report_path.read_bytes())
        if report.get("run_id") != run_id or not report.get("complete"):
            raise ValueError("Container did not produce a complete report for this invocation.")
        if args.mode == "format":
            report["applied"] = False
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf8")
            expected = {v["file"]: v for v in report["changed"]}
            with tarfile.open(work / "formatted.tar") as formatted:
                members = formatted.getmembers()
                if {m.name for m in members} != set(expected) or len(members) != len(expected):
                    raise ValueError("Unexpected formatter output.")
                data = {m.name: formatted.extractfile(m).read() for m in members}
            for name, value in data.items():
                if name not in before or sha256(value).hexdigest() != expected[name]["after"]:
                    raise ValueError("Formatter output hash mismatch.")
            for name, value in data.items():
                path = args.root.resolve() / name
                if sha256(path.read_bytes()).hexdigest() != expected[name]["before"]:
                    raise ValueError("Source changed before applying format: " + name)
                temp = path.with_name(path.name + ".format.tmp")
                with temp.open("xb") as handle:
                    handle.write(value)
                try:
                    shutil.copymode(path, temp)
                    os.replace(temp, path)
                finally:
                    temp.unlink(missing_ok=True)
            report["applied"] = True
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf8")
        return code


def collect(root, problems, languages):
    folders = []
    if problems:
        for number in sorted(set(problems)):
            if not re.fullmatch(r"[0-9]{4}", number):
                raise ValueError("Invalid problem number: " + number)
            first = int(number) // 100 * 100
            folder = root / f"{first}-{first + 99}" / number
            if not folder.is_dir():
                raise ValueError("Problem directory missing: " + str(folder))
            folders.append(folder)
    else:
        for group in sorted(root.iterdir()):
            if group.is_dir() and re.fullmatch(r"[0-9]{4}-[0-9]{4}", group.name):
                folders.extend(
                    p for p in sorted(group.iterdir()) if p.is_dir() and p.name.isdigit()
                )
    files = {
        p
        for folder in folders
        for p in folder.rglob("*")
        if p.is_file()
        and p.suffix in LANGUAGES
        and not any(part.startswith(".") for part in p.relative_to(root).parts)
    }
    if not problems:
        files.update(root.glob("*.py"))
        files.update((root / "tools" / "code_quality").glob("*.py"))
    return sorted(p for p in files if LANGUAGES[p.suffix] in languages)


def tools_for(mode, languages):
    names = {FORMATTERS[language] for language in languages}
    if mode == "lint":
        names.update(CHECKERS[language] for language in languages)
    result = {}
    for name in sorted(names):
        configured = os.environ.get(TOOLS[name], name)
        found = shutil.which(configured)
        if not found:
            raise ValueError(f"Missing {name}. Install it or set {TOOLS[name]} to its executable.")
        result[name] = found
    return result


def run(command, root, env=None):
    return subprocess.run(
        command,
        cwd=root,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf8",
        errors="replace",
    )


def batches(files):
    batch = []
    length = 0
    for path in files:
        size = len(str(path)) + 3
        if batch and length + size > 16000:
            yield batch
            batch = []
            length = 0
        batch.append(str(path))
        length += size
    if batch:
        yield batch


def formatter(tool, language, files, root, write):
    if language in ("cpp", "java"):
        args = [tool, "--style=file:" + str(root / ".clang-format")]
        args += ["-i"] if write else ["--dry-run", "--Werror"]
    elif language == "go":
        args = [tool, "-w" if write else "-l"]
    elif language == "python":
        args = [tool, "format", "--config", str(root / "ruff.toml")]
        if not write:
            args.append("--check")
    else:
        args = [tool, "--edition", "2021"]
        if not write:
            args.append("--check")
    issues = []
    for batch in batches(files):
        process = run(args + batch, root)
        output = process.stdout.strip()
        if process.returncode or (language == "go" and not write and output):
            issues.append(output or f"{language} formatter exited {process.returncode}")
    return issues


def check_file(path, root, tools, work):
    language = LANGUAGES[path.suffix]
    env = os.environ.copy()
    with tempfile.TemporaryDirectory(prefix=language + "-", dir=work) as directory:
        temp = Path(directory)
        source = path
        if language == "cpp":
            command = [
                tools["g++"],
                "-std=c++17",
                "-fsyntax-only",
                "-Wall",
                "-Wextra",
                "-Werror",
                str(path),
            ]
        elif language == "java":
            source = temp / "Main.java"
            source.write_bytes(path.read_bytes())
            command = [tools["javac"], "-Xlint:all", "-Werror", "-d", str(temp), str(source)]
        else:
            command = [
                tools["rustc"],
                "--edition",
                "2021",
                "--emit=metadata",
                "-D",
                "warnings",
                "--out-dir",
                str(temp),
                "--crate-name",
                "solution",
                str(path),
            ]
        process = run(command, root, env)
        if not process.returncode:
            return None
        output = process.stdout.replace(str(source), str(path))
        return {
            "file": path.relative_to(root).as_posix(),
            "language": language,
            "output": output.strip(),
            "exit_code": process.returncode,
        }


def check_go_files(paths, root, tools, work):
    if not paths:
        return []
    packages = work / "go-packages"
    packages.mkdir(exist_ok=True)
    mapping = {}
    for source in paths:
        key = "p" + sha256(source.relative_to(root).as_posix().encode()).hexdigest()[:16]
        assert key not in mapping
        mapping[key] = source
        folder = packages / key
        folder.mkdir(exist_ok=True)
        (folder / "main.go").write_bytes(source.read_bytes())
    env = os.environ.copy()
    env["GO111MODULE"] = "off"
    env["GOGC"] = "50"
    command = [tools["golangci-lint"], "run", "--no-config", "--disable-all",
               "--enable=govet,staticcheck,ineffassign,unused", "--concurrency=1",
        "--max-issues-per-linter=0",
        "--max-same-issues=0",
               "--timeout=15m", "--out-format=json", "./..."]
    print(f"Checking {len(paths)} isolated Go packages in one golangci-lint run.", flush=True)
    process = run(command, packages, env)
    try:
        output = json.loads(process.stdout)
    except ValueError:
        return [{"language": "go", "check": "golangci-lint",
                 "output": process.stdout, "exit_code": process.returncode}]
    failures = {}
    for issue in output.get("Issues") or []:
        position = issue["Pos"]
        key = Path(position["Filename"]).parent.name
        if key not in mapping:
            raise ValueError("Unknown golangci-lint package path: " + position["Filename"])
        source = mapping[key].relative_to(root).as_posix()
        message = f"{source}:{position['Line']}:{position['Column']}: {issue['Text']} ({issue['FromLinter']})"
        failures.setdefault(source, []).append(message)
    result = [{"file": path, "language": "go", "output": "\n".join(messages), "exit_code": 1}
              for path, messages in sorted(failures.items())]
    if process.returncode not in (0, 1) or (process.returncode and not result):
        result.append({"language": "go", "check": "golangci-lint",
                       "output": process.stdout, "exit_code": process.returncode})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("lint", "format", "comments"))
    parser.add_argument("--inside", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--selected", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--archive", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--run-id", default="", help=argparse.SUPPRESS)
    parser.add_argument("problems", nargs="*")
    parser.add_argument(
        "--languages", nargs="+", choices=sorted(FORMATTERS), default=sorted(FORMATTERS)
    )
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be positive")
    root = args.root.resolve()
    if not args.inside:
        try:
            return docker_run(args)
        except (ValueError, OSError, subprocess.CalledProcessError) as error:
            parser.exit(2, str(error) + "\n")
    if args.archive:
        with tarfile.open(args.archive) as archive:
            archive.extractall(root, filter="data")
    try:
        if args.selected:
            names = json.loads(args.selected.read_text(encoding="utf8"))
            if any(Path(n).is_absolute() or ".." in Path(n).parts for n in names):
                raise ValueError("Invalid selected source path.")
            files = [root / name for name in names]
        else:
            files = collect(root, args.problems, args.languages)
        if not files:
            raise ValueError("No source files selected.")
        languages = sorted({LANGUAGES[p.suffix] for p in files})
        tools = tools_for(args.mode, languages) if args.mode != "comments" else {}
    except ValueError as error:
        parser.exit(2, str(error) + "\n")
    work = root / ".run" / "code-quality"
    work.mkdir(parents=True, exist_ok=True)
    before = {p: sha256(p.read_bytes()).hexdigest() for p in files}
    original = {p: p.read_bytes() for p in files} if args.mode == "format" else {}
    groups = {
        language: [p for p in files if LANGUAGES[p.suffix] == language] for language in languages
    }
    failures = []
    for language, sources in groups.items() if args.mode != "comments" else []:
        print(f"{language}: {len(sources)} files, {FORMATTERS[language]}", flush=True)
        for issue in formatter(
            tools[FORMATTERS[language]], language, sources, root, args.mode == "format"
        ):
            print(issue, flush=True)
            failures.append({"language": language, "check": "format", "output": issue})
    from comment_language import check_comments, comments, release_models

    if args.mode in ("lint", "comments"):
        for count, path in enumerate(files, 1):
            for issue in check_comments(path):
                relative = path.relative_to(root).as_posix()
                print(f"{relative}:{issue['line']}: {issue['reason']}: {issue['text']}", flush=True)
                failures.append({"file": relative, "check": "comment_language", **issue})
            if count % 1000 == 0:
                print(f"Checked comments in {count}/{len(files)} files.", flush=True)
    release_models()
    if args.mode == "lint":
        for path in files:
            if b"\r\n" in path.read_bytes():
                failures.append(
                    {
                        "file": path.relative_to(root).as_posix(),
                        "check": "line_endings",
                        "output": "Use LF line endings",
                    }
                )
    if args.mode == "lint":
        python = groups.get("python", [])
        for batch in batches(python):
            process = run(
                [tools["ruff"], "check", "--config", str(root / "ruff.toml")] + batch, root
            )
            if process.returncode:
                print(process.stdout, flush=True)
                failures.append({"language": "python", "check": "ruff", "output": process.stdout})
        go_failures = check_go_files(groups.get("go", []), root, tools, work)
        for issue in go_failures:
            failures.append(issue)
            print(issue.get("file", "golangci-lint") + "\n" + issue["output"], flush=True)
        native = [p for p in files if p.suffix not in (".py", ".go")]
        print(f"Checking {len(native)} standalone programs with {args.jobs} workers.", flush=True)
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            results = pool.map(lambda p: check_file(p, root, tools, work), native)
            for count, issue in enumerate(results, 1):
                if issue:
                    failures.append(issue)
                    print(issue["file"] + "\n" + issue["output"], flush=True)
                if count % 100 == 0:
                    print(f"Checked {count}/{len(native)} programs.", flush=True)
    if args.mode == "format":
        for path in files:
            old_comments = Counter(
                re.findall(
                    r"\w+",
                    " ".join(
                        v for _, v in comments(original[path].decode("utf-8-sig"), path.suffix)
                    ),
                )
            )
            data = path.read_bytes().replace(b"\r\n", b"\n")
            new_comments = Counter(
                re.findall(
                    r"\w+", " ".join(v for _, v in comments(data.decode("utf-8-sig"), path.suffix))
                )
            )
            if old_comments - new_comments:
                path.write_bytes(original[path])
                failures.append(
                    {
                        "file": path.relative_to(root).as_posix(),
                        "check": "comment_preservation",
                        "output": "Formatter removed comment words",
                    }
                )
            elif data != path.read_bytes():
                path.write_bytes(data)
    changed = [
        {
            "file": p.relative_to(root).as_posix(),
            "before": old,
            "after": sha256(p.read_bytes()).hexdigest(),
        }
        for p, old in before.items()
        if old != sha256(p.read_bytes()).hexdigest()
    ]
    report = {
        "run_id": args.run_id,
        "mode": args.mode,
        "files": len(files),
        "languages": {k: len(v) for k, v in groups.items()},
        "changed": changed,
        "failures": failures,
        "passed": not failures,
    }
    (work / (args.mode + "-report.json")).write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf8"
    )
    if args.archive:
        if args.mode == "format":
            with tarfile.open("/reports/formatted.tar", "w") as formatted:
                for item in changed:
                    formatted.add(root / item["file"], arcname=item["file"], recursive=False)
        report["complete"] = True
        (Path("/reports") / (args.mode + "-report.json")).write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf8")
    if args.mode != "format" and changed:
        raise RuntimeError("A lint tool changed a source file.")
    print(f"{len(files)} files, {len(changed)} changed, {len(failures)} failed checks.", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
