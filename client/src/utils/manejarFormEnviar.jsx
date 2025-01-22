import { actualizarTarea, crearTarea } from "../api/tasks.api";

export const manejarFormEnviar = (id, navigate, toast) => {
  return async (datos) => {
    try {
      if (id) {
        console.log(datos);
        await actualizarTarea(id, datos);
        toast.success("Tarea Actualizada", {
          position: "bottom-center",
          style: {
            background: "#404040",
            color: "#fff",
          },
        });
      } else {
        await crearTarea(datos);
        toast.success("Tarea Creada", {
          position: "bottom-center",
          style: {
            background: "#404040",
            color: "#fff",
          },
        });
      }
      navigate("/tasks");
    } catch (error) {
      console.error("Error al manejar la tarea" + error);
      toast.error("Error al procesar la tarea")
    }
  };
};
