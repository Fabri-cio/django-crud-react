import axios from "axios";

const tasksApi = axios.create({
  baseURL: "http://localhost:8000/tasks/api/v1/tasks/",
});

export const obtenerTodasLasTareas = () => tasksApi.get("/");

export const obtenerUnaTarea = (id) => tasksApi.get(`/${id}`)

export const crearTarea = (task) => tasksApi.post("/", task);

export const eliminarTarea = (id) => tasksApi.delete(`/${id}/`);

export const actualizarTarea = (id, task) => tasksApi.put(`/${id}/`, task);


