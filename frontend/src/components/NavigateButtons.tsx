import { useNavigate } from "react-router-dom"

type propType = {
    idButton: string
    goToLink: string
    buttonText: string
}

export default function NavigateButtons({ idButton, goToLink, buttonText }: propType) {

    const navigate = useNavigate()
    function handleGoToLink() { navigate(`/${ goToLink }`) }

    return (
        <>
            <button id={ idButton } onClick={ handleGoToLink }>{ buttonText }</button>
        </>
    )
}