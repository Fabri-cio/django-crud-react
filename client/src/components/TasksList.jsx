import { useEffect, useState } from "react";
import { TaskCard } from "./TaskCard";
import { obtenerTodasLasTareas } from "../api/tasks.api";

export function TasksList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    async function cargarTareas() {
      const respuesta = await obtenerTodasLasTareas();
      setTasks(respuesta.data);
      console.log(respuesta.data);
    }
    cargarTareas();
  }, []);

  return (
    <div className="grid grid-cols-2 gap-2">
      {tasks.map((x) => (
        <TaskCard key={x.id} task={x} />
      ))}
    </div>
  );
}
