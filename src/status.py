"""Возвращает человекочитаемое состояние публикации."""
def format_status(version: str, deployed: bool) -> str:
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"
