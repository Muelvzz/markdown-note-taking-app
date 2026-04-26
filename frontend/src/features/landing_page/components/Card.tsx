import { cardData } from "./solutionData"

export default function Card({ image, title, description }: cardData) {
    return (
        <div className="
            bg-(--secondary-color) px-10 py-5 rounded-lg
            lg:ml-15 lg:mr-15 mt-10 flex flex-col gap-y-5
            text-(--primary-color)
            
        ">
            <div className="flex gap-x-2 items-center">
                <div className="
                    bg-(--primary-color) rounded-[50%] p-2
                ">
                    <img 
                        src={ image } alt={ image } 
                        className="w-6"
                    />
                </div>
                <div>
                    <h2>{ title }</h2>
                </div>
            </div>
            <div>
                <p className="ml-5">{ description }</p>
            </div>
        </div>
    )
}