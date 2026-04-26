import LandingNav from "../../features/landing_page/components/LandingNav"
import Hero from "../../features/landing_page/components/Hero"
import Solution from "../../features/landing_page/components/Solution"
import Features from "../../features/landing_page/components/Features"
import GetStarted from "../../features/landing_page/components/GetStarted"

export default function LandingPage() {
    return (
        <>        
            <LandingNav />
            <main className="
                flex flex-col gap-y-10
            ">
                <Hero />
                <Solution />
                <Features />
                <GetStarted/>
            </main>
        </>
    )
}