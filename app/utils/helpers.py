import subprocess


async def launch_go_prompt(p):
    p = f'"{p}"'
    subprocess.run(f"cd ai && go run main.go -p {p}", shell=True)
