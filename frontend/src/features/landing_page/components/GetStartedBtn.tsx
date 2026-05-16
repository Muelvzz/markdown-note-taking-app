import { useNavigate } from "react-router-dom"

export default function GetStartedBtn() {
    const navigate = useNavigate()

    function handleLogin() { navigate("/upload"); }

    return (
        <button onClick={ handleLogin }>Get Started</button>
    )
}