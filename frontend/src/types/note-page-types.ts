export interface Note {
  id: string;
  file_name: string;
  file_content: string;
  created_at: string;
}

export type NoteList = {
  notes: Note[];
};
