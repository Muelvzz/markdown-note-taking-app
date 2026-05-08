import { BrowserRouter, Routes, Route } from "react-router-dom";

import LandingPage from "./routes/LandingPage";
import UploadPage from "./routes/UploadPage";
import NotFound from "./routes/NotFound";

function Router() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<LandingPage />}/>
                <Route path="/upload" element={<UploadPage />}/>
                
                <Route path="*" element={<NotFound />}/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router;