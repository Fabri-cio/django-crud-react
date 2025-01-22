import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { toast } from "react-hot-toast";
import { useTask } from "../hooks/useTask";
import { manejarFormEnviar } from "../utils/manejarFormEnviar";
import { DeleteButton } from "../components/DeleteButton";

export function TaskFormPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    setValue,
  } = useForm();

  const navegarA = useNavigate();

  const parametro = useParams();

  //llama a la funcion de manejarDatos para crear o actualizar
  const manejarDatos = manejarFormEnviar(parametro.id, navegarA, toast);

  //funcion para obtener la tarea
  useTask(parametro.id, setValue);

  return (
    <div className="max-w-xl mx-auto">
      <form onSubmit={handleSubmit(manejarDatos)}>
        <input
          type="text"
          placeholder="title"
          {...register("title", { required: true })}
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
        />
        {errors.title && <span>Titulo es requerido</span>}

        <textarea
          rows={3}
          placeholder="Descripcion"
          {...register("description", { required: true })}
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
        ></textarea>
        {errors.description && <span>Descripcion es Requerido</span>}

        <button className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">
          Guardar
        </button>
      </form>

      {parametro.id && <DeleteButton id={parametro.id} navegarA={navegarA}/>}
    </div>
  );
}
