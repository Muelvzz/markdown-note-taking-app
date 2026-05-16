from pathlib import Path
import os

from . generate_file_id import generate_file_id

async def save_into_notes_folder(file_content):

  id = generate_file_id()
  path = Path(os.path.join("notes", f"{id}.md"))

  file_path = path.write_text(file_content, encoding="utf-8")

  return str(f"backend\{path}")
