from pathlib import Path

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