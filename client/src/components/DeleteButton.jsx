import toast from "react-hot-toast";
import { eliminarTarea } from "../api/tasks.api";


export const DeleteButton = ({ id, navegarA }) => {
  const manejarEliminar = async () => {
    const aceptar = window.confirm("estas seguro");
    if (aceptar) {
      await eliminarTarea(id);
      toast.success("Tarea Eliminada", {
        position: "bottom-center",
        style: {
          background: "#404040",
          color: "#fff",
        },
      });
      navegarA("/tasks");
    }
  };
  return (
    <div className="flex justify-end">
      <button
        onClick={manejarEliminar}
        className="bg-red-500 p-3 rounded-lg w-48 mt-3"
      >
        Eliminar
      </button>
    </div>
  );
};
