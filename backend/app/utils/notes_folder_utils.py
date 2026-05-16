from pathlib import Path
import os

from . generate_file_id import generate_file_id

async def save_into_notes_folder(file_content):

  id = generate_file_id()
  path = Path(os.path.join("notes", f"{id}.md"))

  file_path = path.write_text(file_content, encoding="utf-8")

  return str(path)


async def read_notes_from_folder(queried_notes):
  for i in range(len(queried_notes)):
    query_note_filepath = Path(queried_notes[i]["file_path"])
    content = query_note_filepath.read_text(encoding="utf-8")

    queried_notes[i]["file_content"] = content

  return queried_notes


async def read_specific_notes_from_folder(file_path: str):
  path = Path(file_path)
  content = path.read_text(encoding="utf-8")

  return content


def delete_file_from_notes_folder(file_path: str):
  path = Path(file_path)
  path.unlink()