import { NoteList } from "../../../types/note-page-types"
import { formatDateTime } from "../../../utils/formatDateTime"
import "../../../css/note-card.css"

import deleteImage from "../assets/delete-img.png"

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
              <div className="flex justify-between">
                <div>
                  <h3>{ note.file_name }</h3>
                </div>
                <div>
<<<<<<< HEAD
                  <button 
                    id="note-card-button-styles button"
                    type="button"
                    data-modal-target="popup-modal" 
                    data-modal-toggle="popup-modal"
                  >
=======
                  <button id="note-card-button-styles">
>>>>>>> 640c13c751897f1e1335f2eb7f4cb8519b91756c
                    <img src={ deleteImage } alt="Delete Image Icon" 
                      className="w-2 md:w-4 lg:w-6"
                    />
                  </button>
                </div>
              </div>
              <p>{ formatDateTime(note.created_at) }</p>
              <p>{ note.file_content.slice(0, 200) }</p>
            </div>
        </div>
      ))}
    </>
  )
}