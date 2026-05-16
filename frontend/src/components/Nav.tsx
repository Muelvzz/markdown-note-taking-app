import logo from '../assets/logo.webp'
import NavigateButtons from './NavigateButtons'

export default function Nav() {
    return (
        <>
            <nav id='main-navigation'
                className='flex justify-between items-center'
            >
                <div className='flex justify-between gap-x-2 lg:gap-x-5 items-center'>
                    <div>
                        <img src={logo} alt="Logo image" className='w-24'/>
                    </div>
                    <NavigateButtons
                        idButton="no-style-button"
                        goToLink=''
                        buttonText='Home'
                    />
                    <NavigateButtons
                        idButton="no-style-button"
                        goToLink='notes'
                        buttonText='Notes'
                    />
                </div>
                <div>
                    <NavigateButtons
                        idButton=""
                        goToLink='upload'
                        buttonText='Upload'
                    />
                </div>
            </nav>
        </>
    )
}