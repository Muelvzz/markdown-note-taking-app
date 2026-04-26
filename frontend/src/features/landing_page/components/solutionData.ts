import noteIcon from "../assets/notes-icon.png"
import convertIcon from "../assets/converting-icon.png"
import grammarIcon from "../assets/grammar-icon.png"

export type cardData = {
    image: string;
    title: string;
    description: string;
}

export const cardData: cardData[] = [
    {
        image: noteIcon,
        title: "Better notes organized",
        description: "Glint transforms cluttered local files into a structured digital library, using a centralized postgres database to ensure your thoughts are always searchable and never lost in a folder."
    },
    {
        image: convertIcon,
        title: "Converting markdown into notes",
        description: "By instantly parsing raw syntax into a beautiful HTML preview, Glint allows writers to enjoy the speed of Markdown without sacrificing the readability of a polished document."
    },
    {
        image: grammarIcon,
        title: "Improve grammar checking",
        description: "Glint eliminates the second-guessing of draft-writing by integrating real-time linguistic analysis directly into the workflow, ensuring every note is professional and error-free before it's ever saved."
    },
]