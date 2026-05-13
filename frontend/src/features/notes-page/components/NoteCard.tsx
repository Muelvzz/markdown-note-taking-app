import { NoteList } from "../../../config/note-page-conf"

export default function NoteCard({ notes }: NoteList) {

  return (
    <>
      {notes.map((note) => (
        <div 
            key={ note.id }
            className="
            bg-(--primary-color) text-(--secondary-color)
            text-left p-3 border rounded-lg
            ">
            <div className="flex flex-col gap-y-2">
              <h3>{ note.file_name }</h3>
              <p>{ note.created_at }</p>
              <p>{ note.content.slice(0, 200) }</p>
            </div>
        </div>
      ))}
    </>
  )
}