import myLogo from '../../../assets/logo.png'
import GetStartedBtn from './GetStartedBtn'

export default function LandingNav() {

    return (
        <nav
            className='
                flex justify-between mt-1 
                items-center
                '
        >
            <div>
                <img 
                    src={ myLogo } alt="Logo Picture" 
                    className='w-[6rem]'
                />
            </div>
            <div className='
                mr-2
            '>
                <GetStartedBtn />
            </div>
        </nav>
    )
}