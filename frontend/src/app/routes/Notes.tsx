import { useEffect, useState } from "react"

import Nav from "../../components/Nav"
import NoteCard from "../../features/notes-page/components/NoteCard"
import searchImage from "../../features/notes-page/assets/search-img.png"
import { fetchSavedNotes } from "../../services/backend-api"

interface Note {
    id: string
    file_name: string
    content: string
    created_at: string
}

export default function Notes() {
    const [noteList, setNoteList] = useState<Note[]>([])
    const [search, setSearch] = useState("")

    const fetchItems = async () => {
        const response = await fetchSavedNotes()
        if (response?.data?.all_notes) {
            setNoteList(response.data.all_notes)
        }
    }

    const handleSearch = (search: string) => { setSearch(search.toLowerCase())}

    useEffect(() => { fetchItems() }, [])

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
                        onChange={(e) => handleSearch(e.target.value)}
                    />
                </div>
                <div className="flex flex-col gap-y-5">
                    <NoteCard 
                        noteList={ noteList }
                        search={ search }
                    />
                </div>
            </main>
        </>
    )
}