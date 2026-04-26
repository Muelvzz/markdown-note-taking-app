import featureGrammar from "../assets/feature-grammar.webp"
import featurePrivacy from "../assets/feature-privacy.webp"
import featureRender from "../assets/feature-render.webp"
import featureUpload from "../assets/feature-upload.webp"

export type featureData = {
    image: string
    title: string
    description: string
}

export const feature: featureData[] = [
    {
        image: featureGrammar,
        title: "Grammar Refinement",
        description: "Your Markdown files will undergo further analysis to eliminate errors and ensure every note maintains a professional tone."
    },
    {
        image: featurePrivacy,
        title: "Data Privacy",
        description: "Safely commit your documents to our secure database, ensuring your notes stay organized and accessible only to you."
    },
    {
        image: featureRender,
        title: "Aesthetic Rendering",
        description: "Transform raw Markdown syntax into beautifully formatted HTML previews with a single click, bridging the gap between code and content."
    },
    {
        image: featureUpload,
        title: "Seamless File Ingestion",
        description: "Effortlessly import existing documents from your local machine with a streamlined, one-tap upload interface."
    },
]