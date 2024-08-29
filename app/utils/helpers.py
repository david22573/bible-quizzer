import subprocess


def ask_ai(prompt: str, model: str = "") -> str:
    prompt = f'"{prompt}"'
    if model:
        prompt = f"-m {model} {prompt}"
    sp = subprocess.run(f"./ai.exe -p {prompt}", capture_output=True, text=True)
    print(sp.stdout)
    return sp.stdout
