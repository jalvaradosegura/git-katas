def validations():
    with open("commits.txt", "r") as f:
        commits = f.readlines()

    if len(commits) != 4:
        print(
            "❌ The amount of commits is wrong, you are expected to have 4 and you "
            f"have:\n{len(commits)}"
        )
        raise SystemExit(1)

    for commit in commits:
        message = commit.split(" ", 1)[1].replace("\n", "")
        if "WIP" in message:
            print(
                f"❌ You cannot have git messages with 'WIP' in your final version:\n"
                f"{message}"
            )
            raise SystemExit(1)

        if len(message) > 50:
            print(
                "❌ The length of the commit message is longer than 50 characters:\n"
                f"{messsage}"
            )
            raise SystemExit(1)

        if message[0].isupper() is False:
            print(f"❌ This commit message does not start with uppercase:\n {message}")
            raise SystemExit(1)

        if message[-1] == ".":
            print(f"❌ This commit message is ending with a dot:\n {message}")
            raise SystemExit(1)
