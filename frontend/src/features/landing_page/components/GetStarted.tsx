import GetStartedBtn from "./GetStartedBtn"

export default function GetStarted() {
    return (
        <div className="text-center">
            <div className="mt-10 text-center flex flex-col gap-y-3 mb-5">
                <h1>Get Started Today</h1>
                <p>Use Glint as your note-taking app - anytime, anywhere!</p>
            </div>
            <GetStartedBtn />
        </div>
    )
}