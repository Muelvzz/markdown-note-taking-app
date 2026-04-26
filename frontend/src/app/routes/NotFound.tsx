import { useNavigate } from "react-router-dom"

export default function NotFound() {
    const navigate = useNavigate()

    function handleGoBack() { navigate("/") }

    return (
        <div className="
            flex justify-center items-center
            h-screen flex-col
        ">
            <h2>Server Address Not Found</h2>
            <h3>The address you want to find does not exist.</h3>
            <button onClick={ handleGoBack }>Go back...</button>
        </div>
    )
}