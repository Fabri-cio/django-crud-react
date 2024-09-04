// 1
// rfce atajo de teclado de un componente muy basico
// primeo crear las pages (funciones)
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { TaskPage } from "./pages/TaskPage";
import { TaskFormPage } from "./pages/TaskFormPage";
import { Navigation } from "./components/Navigation";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto">
        <Navigation />
        <Routes>
          <Route path="/" element={<Navigate to="tasks" />}></Route>
          <Route path="/tasks" element={<TaskPage />}></Route>
          <Route path="/tasks-create" element={<TaskFormPage />}></Route>
          <Route path="/tasks/:id" element={<TaskFormPage />}></Route>
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;
