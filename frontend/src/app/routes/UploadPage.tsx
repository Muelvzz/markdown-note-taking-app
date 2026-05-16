import { useState , DragEvent, ChangeEvent } from "react"
import Nav from "../../components/Nav"
import DropdownInfo from "../../components/DropdownInfo"

import { requestUploadFile } from "../../services/backend-api"

export default function UploadPage() {
    const [isDragging, setIsDragging] = useState(false)
    const [showInfo, setShowInfo] = useState(false)
    const [dropdownText, setDropdownText] = useState("")

    const handleDragOver = (e: DragEvent<HTMLElement>) => {
        e.preventDefault()
        setIsDragging(true)
    }

    const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0]
        if (file) { processFile(file) }
    }

    const processFile = async (file: File) => {
        setShowInfo(true)

        if (file && file.name.endsWith('.md')) { 
            await requestUploadFile(file)
            setDropdownText(`${ file.name } has been added to the Notes`)
        }
        else { setDropdownText("Please upload a Markdown (.md) file.") }

        setTimeout(() => setShowInfo(false), 2000)
    }

    const handleDragLeave = () => { setIsDragging(false) }

    const handleDrop = (e: DragEvent<HTMLElement>) => {
        e.preventDefault()
        e.stopPropagation()
        setIsDragging(false)

        const file = e.dataTransfer.files?.[0]
        if (file) processFile(file)
    }

    return (
        <>
            { showInfo && <DropdownInfo dropdownText={ dropdownText }/> }
            <Nav />
            <main 
                onDragOver={ handleDragOver }
                onDragLeave={ handleDragLeave }
                onDrop={ handleDrop }
                className={`flex flex-col justify-center 
                items-center h-screen gap-y-4
                ${isDragging ? "bg-[#0000007D] rounded-sm" : ""}`}>
                <h2 className="text-center">Start Uploading your <br />Markdown Files</h2>
                <div>
                    <label htmlFor="file-upload">
                        Upload File
                    </label>
                    <input 
                        id="file-upload"
                        type="file"
                        accept=".md"
                        onChange={ handleFileChange }
                        className="hidden"
                    />
                </div>
                <p>{ isDragging ? "Release to drop" : "or drop a file..." }</p>
            </main>
        </>
    )
}