import subprocess


async def launch_go_prompt(prompt):
    cmd = await subprocess.run(
        ["go", "run", "ai/main.go", "-p", prompt], capture_output=True
    )
    print(cmd.stdout.decode("utf-8"))

    return cmd
