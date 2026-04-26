import LandingNav from "../../features/landing_page/components/LandingNav"
import Hero from "../../features/landing_page/components/Hero"
import Solution from "../../features/landing_page/components/Solution"

export default function LandingPage() {
    return (
        <>        
            <LandingNav />
            <main className="
                flex flex-col gap-y-10
            ">
                <Hero />
                <Solution />
            </main>
        </>
    )
}