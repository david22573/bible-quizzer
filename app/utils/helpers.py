import subprocess


def ask_ai(instruction):
    instruction = f'"{instruction}"'
    sp = subprocess.Popen(
        f"./prompt -p {instruction}",
        shell=True,
        text=True,
    )

    if sp.returncode != 0:
        raise RuntimeError(f"Error running prompt: {sp.output}")

    return sp.output
