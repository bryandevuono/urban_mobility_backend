from logger import log_event

def logout_user() -> bool:
    from um_members import welcome_screen
    welcome_screen()
    log_event(f"User has logged out", "0")