import { BrowserRouter, Routes, Route } from "react-router-dom";

import LandingPage from "./routes/LandingPage";
import MainPage from "./routes/MainPage";
import NotFound from "./routes/NotFound";

function Router() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<LandingPage />}/>
                <Route path="/home" element={<MainPage />}/>
                
                <Route path="*" element={<NotFound />}/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router;