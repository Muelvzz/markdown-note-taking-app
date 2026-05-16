import "../css/dropdown.css"

export default function DropdownInfo({ dropdownText }: { dropdownText: string }) {
    return (
        <>
            <div id="dropdown-card-container">
                <div id="dropdown-card">
                    { dropdownText }
                </div>
            </div>
        </>
    )
}