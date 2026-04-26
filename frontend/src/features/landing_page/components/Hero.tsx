import GetStartedBtn from "./GetStartedBtn"
import heroImg from '../assets/hero-img.jpg'

export default function Hero() {
    return (
        <div className="
            w-full flex flex-col 
            gap-y-5
        ">
            <div className="
                text-center mt-10
            ">
                <h1>Polished notes from <span className="text-(--secondary-color)">Markdown</span> to <span className="text-(--secondary-color)">Masterpiece</span></h1>
                <p className="
                    mb-5 mt-3
                ">Glint transforms your Markdown notes into masterpieces with intuitive tools, making every idea shine from raw thought to polished brilliance.</p>
                <GetStartedBtn />
            </div>
            <div>
                <img 
                    src={ heroImg } alt="Hero Image" 
                    className="rounded-lg"
                />
            </div>
        </div>
    )
}