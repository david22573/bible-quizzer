import subprocess


def ask_ai(instruction):
    instruction = f'"{instruction}"'
    sp = subprocess.Popen(
        f"./prompt -p {instruction}",
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    out, err = sp.communicate()

    if sp.returncode != 0:
        raise RuntimeError(f"Error running prompt: {err}")

    return out
