import { BrowserRouter, Routes, Route } from "react-router-dom";
import { lazy, Suspense } from "react";

import LandingPage from "./routes/LandingPage";
import NotFound from "./routes/NotFound";
import Loading from "../components/Loading";

import DropdownInfo from "@/components/DropdownInfo";

function Router() {
    const UploadPage = lazy(() => import("./routes/UploadPage"))
    const NotesPage = lazy(() => import("./routes/Notes"))

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<LandingPage />}/>        
                <Route path="/upload" element={
                    <Suspense fallback={ <Loading pageTitle="Upload"/> }>
                        <UploadPage />
                    </Suspense>
                }/>
                <Route path="/notes" element={
                    <Suspense fallback={ <Loading pageTitle="Notes"/> }>
                        <NotesPage />
                    </Suspense>
                }/>

                <Route path="/error" element={<DropdownInfo dropdownText="Testing" />}/>
                <Route path="/loading" element={<Loading pageTitle="Testing" />}/>
                <Route path="*" element={<NotFound />}/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router;