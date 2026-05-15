export interface Note {
  id: string;
  file_name: string;
  content: string;
  created_at: string;
}

export type NoteList = {
  notes: Note[];
};
