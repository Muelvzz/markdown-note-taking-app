import { useState, useEffect } from "react";
import { Note } from "../types/note-page-types";

import { fetchSavedNotes } from "../services/backend-api";

export const useUserNotes = () => {
  const [noteList, setNoteList] = useState<Note[]>([])

  const fetchItems = async () => {
    const response = await fetchSavedNotes();
    if (response?.data?.all_notes) {
      setNoteList(response.data.all_notes)
    }
  }
  useEffect(() => { fetchItems() }, [])

  return { noteList, setNoteList, fetchItems }
}