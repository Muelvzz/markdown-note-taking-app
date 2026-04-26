import { feature } from "./featureData"
import Card2 from "./Card2"

export default function Features() {
    return (
        <div>
            <h1 className="text-center">Features that you will love</h1>
            <div className="grid grid-cols-2 gap-5 mt-10">
                { feature.map((feature) => (
                    <div key={feature.image}>
                        <Card2
                            image={feature.image}
                            title={feature.title}
                            description={feature.description}
                        />
                    </div>
                )) }
            </div>
        </div>
    )
}