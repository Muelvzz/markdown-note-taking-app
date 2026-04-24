import { BrowserRouter, Routes, Route } from "react-router-dom";
import { lazy, Suspense } from "react";

import LandingPage from "./routes/LandingPage";
import Loading from "../components/Loading";
import NotFound from "./routes/NotFound";

function Router() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<LandingPage />}/>
                
                <Route path="*" element={<NotFound />}/>
            </Routes>

            {/* <Suspense fallback={<Loading />}>
                <Routes>
                    <Route path="*" element={<NotFound />}/>
                </Routes>
            </Suspense> */}
        </BrowserRouter>
    )
}

export default Router;