import re

# List of blocked patterns using regex for broader detection
BLOCKED_PATTERNS = {
    r"\bimport\b": "🚫 'import' statements are not allowed. Try writing pure beginner-friendly code!",
    r"\bos\b": "⚠️ File system access via 'os' is not allowed.",
    r"\bsys\b": "⚠️ System-level access via 'sys' is blocked.",
    r"\beval\b": "⚠️ 'eval' is unsafe and not allowed.",
    r"\bexec\b": "⚠️ 'exec' can be dangerous and is blocked.",
    r"\bopen\b": "⚠️ File read/write is disabled.",
    r"\bsubprocess\b": "🚫 Running subprocesses is not allowed.",
    r"__import__": "🚫 Dynamic imports are blocked.",
    r"\binput\b": "⚠️ 'input()' is blocked for stability.",
    r"\bshutil\b": "⚠️ File system operations not allowed.",
    r"\bsocket\b": "⚠️ Network access is restricted.",
    r"\bthread\b": "⚠️ Threading is disabled for safety.",
    r"\btensorflow\b": "🚫 ML libraries are not supported in PyTosh.",
    r"\btorch\b": "🚫 ML libraries are not supported in PyTosh.",
    r"\bnumpy\b": "🚫 External numerical libraries are not allowed.",
    r"\bexit\(\)": "⚠️ exit() is blocked.",
    r"\bquit\(\)": "⚠️ quit() is blocked.",
    r"\brm\b": "🚫 Shell command 'rm' is blocked.",
    r"\bcurl\b": "🚫 Shell command 'curl' is blocked.",
    r"\bwget\b": "🚫 Shell command 'wget' is blocked.",
    r"/etc/": "🚫 Accessing system files is not allowed.",
    r"\bPopen\b": "⚠️ subprocess.Popen is not allowed.",
    r"\bsystem\b": "⚠️ os.system() is blocked.",
    r"\bpathlib\b": "⚠️ File path libraries are disabled.",
    r"\bglob\b": "⚠️ File search access is blocked."
}


def is_safe_code(code: str) -> bool:
    """Returns False if any blocked pattern is found in the code."""
    for pattern in BLOCKED_PATTERNS.keys():
        if re.search(pattern, code):
            return False
    return True


def get_block_reason(code: str) -> str:
    """Returns the first reason why the code is considered unsafe."""
    for pattern, reason in BLOCKED_PATTERNS.items():
        if re.search(pattern, code):
            return reason
    return "❌ Unsafe code detected."
