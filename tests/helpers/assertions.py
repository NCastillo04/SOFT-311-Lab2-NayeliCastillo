from datetime import datetime
from pathlib import Path
import re

def _sanitize_filename(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", value).strip("_") or "assertion"

def assert_with_screenshot(
        page,
        *,
        condition: bool,
        message: str,
        name: str = "assertion_failure",
        screenshots_dir: str | Path = "artifacts/screenshots",
) -> None:
    if condition:
        return

    output_dir = Path(screenshots_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = _sanitize_filename(name)
    screenshots_path = output_dir / f"{safe_name}_{timestamp}.png"
    page.screenshot(path=str(screenshots_path), full_page=True)

    raise AssertionError(f"{message}\nScreenshot: {screenshots_path}")

