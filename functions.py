def load_token(path):
    """
    Loads the bot token from the current directory
    """
    file = open(path, "r")
    token = str(file.read().splitlines()[0])
    file.close()
    return token
