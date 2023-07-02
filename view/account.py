import modal.account as modal_account


def login(username, password):
    user = modal_account.find_by_username(username=username)
    if user is not None:
        if password == user.password.strip():
            return [True, user.username, user.name]

    return [False]