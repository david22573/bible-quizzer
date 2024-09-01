import subprocess


def ask_ai(prompt_path):
    sp = subprocess.Popen(
        ["./prompt", "-p", prompt_path],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    out, err = sp.communicate()

    if sp.returncode != 0:
        raise RuntimeError(f"Error running prompt: {err}")
    return out
