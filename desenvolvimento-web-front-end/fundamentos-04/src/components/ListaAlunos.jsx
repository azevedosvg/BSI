// Importa uma lista de alunos (array)
import alunos from "../data/alunos";

export default function ListaAlunos() {
  // map percorre o array de alunos e transforma cada item em um elemento <li>
  const alunosLI = alunos.map((aluno) => {
    return (
      // key é obrigatória em listas no React (ajuda na renderização)
      <li key={aluno.id}>
        {/* Exibe os dados de cada aluno */}
        {aluno.id}) {aluno.nome} - {aluno.nota}
      </li>
    );
  });

  return (
    <div>
      <ul style={{ listStyle: "none" }}>{alunosLI}</ul>
    </div>
  );

  // Aqui eu peguei um array de dados (alunos) e transformei em HTML (JSX).
}
