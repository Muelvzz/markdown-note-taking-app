import { featureData } from "./featureData"

export default function Card2({ image, title, description }: featureData) {
    return (
        <>
            <div className="
            p-5 rounded-lg mt-10 flex flex-col gap-y-5
            border-b-4 border-(--secondary-color)-500
            h-full
            
        ">
            <div className="flex gap-x-2 items-center">
                <div className="
                    bg-(--secondary-color) rounded-full p-2
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
        </>
    )
}