import searchNone from "../assets/search-none.png"

export default function NoSearchesFound() {
  return (
    <div className="flex flex-col justify-center 
      text-center items-center min-h-dvh">
      <div className="flex justify-center">
        <img src={ searchNone } alt="Search None Icon" 
        className="w-16"
        />
      </div>
      <h3>No notes found...</h3>
    </div>
  )
}