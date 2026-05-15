import { BrowserRouter, Routes, Route } from "react-router-dom";
import { lazy, Suspense } from "react";

import LandingPage from "./routes/LandingPage";
import NotFound from "./routes/NotFound";
import Loading from "../components/Loading";

function Router() {
    const UploadPage = lazy(() => import("./routes/UploadPage"))
    const NotesPage = lazy(() => import("./routes/Notes"))

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<LandingPage />}/>        
                <Route path="/upload" element={
                    <Suspense fallback={ <Loading/> }>
                        <UploadPage />
                    </Suspense>
                }/>
                <Route path="/notes" element={
                    <Suspense fallback={ <Loading/> }>
                        <NotesPage />
                    </Suspense>
                }/>

                <Route path="*" element={<NotFound />}/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router;