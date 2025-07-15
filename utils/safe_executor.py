import io
import sys

def run_safe_code(code: str) -> str:
    # Define only allowed safe built-in functions
    allowed_builtins = {
        "abs": abs,
        "all": all,
        "any": any,
        "enumerate": enumerate,
        "float": float,
        "int": int,
        "len": len,
        "list": list,
        "max": max,
        "min": min,
        "print": print,
        "range": range,
        "str": str,
        "sum": sum,
        "zip": zip
    }

    output = io.StringIO()
    sys_stdout = sys.stdout

    try:
        sys.stdout = output
        exec(code, {"__builtins__": allowed_builtins}, {})
    except Exception as e:
        return f"❌ Execution Error: {str(e)}"
    finally:
        sys.stdout = sys_stdout

    return output.getvalue().strip()
