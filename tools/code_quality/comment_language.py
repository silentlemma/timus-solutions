"""Extract comment prose while keeping program string literals separate."""

import ast
from functools import lru_cache
import io
import re
import tokenize
import unicodedata


def comments(text, suffix):
    if suffix == ".py":
        result = [
            (t.start[0], t.string[1:])
            for t in tokenize.generate_tokens(io.StringIO(text).readline)
            if t.type == tokenize.COMMENT
        ]
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                value = ast.get_docstring(node, clean=False)
                if value is not None:
                    result.append((node.body[0].lineno, value))
        return sorted(result)
    if suffix == ".java":
        text = re.sub(r"\\u+([0-9a-fA-F]{4})", lambda m: chr(int(m[1], 16)), text)
    found = []
    i = 0
    while i < len(text):
        start = i
        if suffix == ".cpp":
            raw = re.match(r'R"([^\s()\\]{0,16})\(', text[i:])
            if raw:
                end = text.find(")" + raw[1] + '"', i + raw.end())
                i = len(text) if end < 0 else end + len(raw[1]) + 2
                continue
        if suffix == ".rs":
            raw = re.match(r'(?:br|cr|r)(#*)"', text[i:])
            if raw:
                end = text.find('"' + raw[1], i + raw.end())
                i = len(text) if end < 0 else end + len(raw[1]) + 1
                continue
            if text[i] == "'":
                lifetime = re.match(r"'[A-Za-z_][A-Za-z_0-9]*", text[i:])
                if lifetime and (
                    i + lifetime.end() == len(text) or text[i + lifetime.end()] != "'"
                ):
                    i += lifetime.end()
                    continue
        if text.startswith("//", i):
            end = text.find("\n", i)
            while end >= 0 and suffix == ".cpp" and text[:end].rstrip("\r").endswith("\\"):
                end = text.find("\n", end + 1)
            i = len(text) if end < 0 else end
            found.append((text.count("\n", 0, start) + 1, text[start + 2 : i]))
        elif text.startswith("/*", i):
            depth = 1
            i += 2
            while i < len(text) and depth:
                if text.startswith("/*", i) and suffix == ".rs":
                    depth += 1
                    i += 2
                elif text.startswith("*/", i):
                    depth -= 1
                    i += 2
                else:
                    i += 1
            found.append((text.count("\n", 0, start) + 1, text[start + 2 : i - 2]))
        elif text[i] == chr(96) and suffix == ".go":
            end = text.find(chr(96), i + 1)
            i = len(text) if end < 0 else end + 1
        elif text[i] in ('"', "'"):
            quote = text[i]
            if (
                suffix == ".cpp"
                and quote == "'"
                and i
                and text[i - 1].isalnum()
                and i + 1 < len(text)
                and text[i + 1].isalnum()
            ):
                i += 1
                continue
            i += 1
            while i < len(text):
                if text[i] == "\\":
                    i += 2
                elif text[i] == quote:
                    i += 1
                    break
                else:
                    i += 1
        else:
            i += 1
    return found


@lru_cache(maxsize=1)
def detector():
    from lingua import LanguageDetectorBuilder

    return LanguageDetectorBuilder.from_all_spoken_languages().build()


@lru_cache(maxsize=8192)
def language_scores(text):
    return detector().compute_language_confidence_values(text)


def release_models():
    language_scores.cache_clear()
    if detector.cache_info().currsize:
        detector().unload_language_models()
        detector.cache_clear()


def check_comments(path):
    from lingua import Language

    result = []
    for line, value in comments(path.read_text(encoding="utf-8-sig"), path.suffix):
        foreign = []
        for word in re.findall(r"[^\W\d_]+", value, re.UNICODE):
            for char in word:
                name = unicodedata.name(char, "")
                if (
                    char.isalpha()
                    and ord(char) > 127
                    and "LATIN" not in name
                    and "MATHEMATICAL" not in name
                    and "DOUBLE-STRUCK" not in name
                    and not ("GREEK" in name and len(word) == 1)
                ):
                    foreign.append(char)
        if foreign:
            result.append(
                {"line": line, "text": value.strip(), "reason": "Non-English script in comment"}
            )
            continue
        words = re.findall(r"[^\W\d_]{2,}", value, re.UNICODE)
        if len(words) < 5:
            continue
        scores = language_scores(" ".join(words))
        if (
            len(scores) > 1
            and scores[0].language != Language.ENGLISH
            and scores[0].value >= 0.9
            and scores[0].value - scores[1].value >= 0.25
        ):
            result.append(
                {
                    "line": line,
                    "text": value.strip(),
                    "reason": "Comment classified as " + scores[0].language.name,
                }
            )
    return result
