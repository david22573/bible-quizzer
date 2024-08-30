import subprocess


def ask_ai(instruction):
    sp = subprocess.Popen(
        ["./prompt", "-p"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = sp.communicate(input=instruction)

    if sp.returncode != 0:
        raise RuntimeError(f"Error running prompt: {stderr}")

    return stdout
