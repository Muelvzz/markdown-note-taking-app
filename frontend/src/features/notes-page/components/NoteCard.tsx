type Note = {
    id: string
    file_name: string
    content: string
    created_at: string
}

type NoteList = {
  noteList: Note[]
  search: string
}

export default function NoteCard({ noteList, search }: NoteList ) {

  const filteredSavedNotes = noteList.filter((note) => 
    note.file_name.toLowerCase().includes(search.toLowerCase())
  )

  return (
    <>
      {filteredSavedNotes.map((note) => (
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