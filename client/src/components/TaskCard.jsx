import { useNavigate } from "react-router-dom";

export function TaskCard({ task }) {

  const navegarAEditar = useNavigate();

  return (
    <div
      className="bg-zinc-800 p-3 hover:bg-red-800 hover:cursor-pointer"
      onClick={() => {
        navegarAEditar(`/tasks/${task.id}`);
      }}
    >
      <h1 className="font-bold uppercase">{task.title}</h1>
      <p className="text-slate-400">{task.description}</p>
      <hr />
    </div>
  );
}
