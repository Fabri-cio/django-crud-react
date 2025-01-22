import { useEffect } from "react";
import { obtenerUnaTarea } from "../api/tasks.api";

export const useTask = (id, setValue) => {
  useEffect(() => {
    async function cargarDatos() {
      if (id) {
        console.log("obteniendo datos" + id);
        const {
          data: { title, description },
        } = await obtenerUnaTarea(id);
        setValue("title", title);
        setValue("description", description);
      }
    }
    cargarDatos();
  }, [id, setValue]);
};
