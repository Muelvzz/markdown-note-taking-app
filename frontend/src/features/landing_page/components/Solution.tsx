import { cardData } from "./solutionData";
import { useState } from "react";
import { BsChevronCompactLeft, BsChevronCompactRight } from 'react-icons/bs';
import { RxDotFilled } from 'react-icons/rx';
import Card from "./Card";

export default function Solution() {
    const [currentIndex, setCurrentIndex] = useState(0);
    
    const arrowStyle = "hidden group-hover:block absolute top-[60%] translate-x-0 translate-y-[-50%] text-2xl rounded-full p-2 bg-black/50 text-white cursor-pointer z-10 hover:bg-black duration-300"

    const prevSlide = () => {
        const isFirstSlide = currentIndex === 0;
        const newIndex = isFirstSlide ? cardData.length - 1 : currentIndex - 1;
        setCurrentIndex(newIndex);
    };

    const nextSlide = () => {
        const isLastSlide = currentIndex === cardData.length - 1;
        const newIndex = isLastSlide ? 0 : currentIndex + 1;
        setCurrentIndex(newIndex);
    };

    const goToSlide = (slideIndex: number) => {
        setCurrentIndex(slideIndex);
    };

    return (
        <div className="w-full m-auto py-16 px-4 relative group">
            <h1 className="text-center mb-20">
                We get it. That's why we built this
            </h1>

            <div className="relative w-full h-full rounded-2xl bg-(--primary-color) flex duration-500">

                <div className={`${ arrowStyle } left-1`}>
                    <BsChevronCompactLeft onClick={prevSlide} size={20} />
                </div>

                <div className="w-full h-full flex justify-center items-center">
                    <Card 
                        image={cardData[currentIndex].image}
                        title={cardData[currentIndex].title}
                        description={cardData[currentIndex].description}
                    />
                </div>

                <div className={`${ arrowStyle } right-1`}>
                    <BsChevronCompactRight onClick={nextSlide} size={20} />
                </div>
            </div>

            <div className="flex justify-center py-4 px-1">
                {cardData.map((_, slideIndex) => (
                    <div
                        key={slideIndex}
                        onClick={() => goToSlide(slideIndex)}
                        className={`text-2xl cursor-pointer transition-colors duration-300 ${
                            currentIndex === slideIndex ? "text-black/50 scale-125" : "text-gray-400"
                        }`}
                    >
                        <RxDotFilled />
                    </div>
                ))}
            </div>
        </div>
    );
}