import "./ClassificacaoNota.css";

function ClassificacaoNota({ nota }) {
  const classificacao =
    nota >= 9
      ? "Excelente"
      : nota >= 7
        ? "Bom"
        : nota >= 5
          ? "Regular"
          : "Insuficiente";

  const classe = classificacao.toLowerCase(); // Transforma Excelente em excelente

  return (
    <div className="container">
      <h1>Nota: {nota}</h1>
      <p className={`resultado ${classe}`}>{classificacao}</p>
    </div>
  );
}

export default ClassificacaoNota;
