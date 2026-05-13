import { useState } from "react"

import Nav from "../../components/Nav"
import NoteCard from "../../features/notes-page/components/NoteCard"
import searchImage from "../../features/notes-page/assets/search-img.png"

import { Note } from "../../config/note-page-conf"
import { useUserNotes } from "../../hooks/note-page-hooks"

export default function Notes() {
    const { noteList } = useUserNotes()
    const [search, setSearch] = useState("") 

    const filteredNotes = noteList.filter((note: Note) =>
        note.file_name.toLowerCase().includes(search.toLowerCase())
    )

    return (
        <>
            <Nav />
            <main className="flex flex-col gap-y-5">
                <div>
                    <h2>All Notes</h2>
                    <p>{ noteList.length } notes</p>
                </div>
                <div className="
                    bg-(--secondary-color) text-(--primary-color) py-1 rounded-lg
                    flex gap-x-2 px-4
                ">
                    <button className="p-1">
                        <img 
                            src={ searchImage } alt="Search Image Icon" 
                            className="w-4"
                        />
                    </button>
                    <input 
                        type="text" 
                        className="w-full text-(--primary-color) px-3"
                        placeholder="Search Input"
                        value={ search }
                        onChange={(e) => setSearch(e.target.value)}
                    />
                </div>
                <div className="flex flex-col gap-y-5">
                    <NoteCard 
                        notes={ filteredNotes }
                    />
                </div>
            </main>
        </>
    )
}