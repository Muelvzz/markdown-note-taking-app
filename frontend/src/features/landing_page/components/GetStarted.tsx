import { useNavigate } from "react-router-dom"

export default function GetStarted() {
    const navigate = useNavigate()

    function handleLogin() {
        navigate("/home");
    }

    return (
        <button onClick={ handleLogin }>Get Started</button>
    )
}