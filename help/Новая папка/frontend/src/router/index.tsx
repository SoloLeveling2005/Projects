import Main from "../pages/Main/Main";
import { createBrowserRouter } from 'react-router-dom'


const router = createBrowserRouter([
    {
        path: '/',
        element: <Main />
    }
])

export default router;
