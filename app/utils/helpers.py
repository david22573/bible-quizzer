import subprocess


def ask_ai(instruction):
    instruction = f'"{instruction}"'
    sp = subprocess.Popen(
        f"./prompt -p {instruction}",
        shell=True,
        text=True,
    )

    out, err = sp.communicate()

    if sp.returncode != 0:
        raise RuntimeError(f"Error running prompt: {err}")

    return out
