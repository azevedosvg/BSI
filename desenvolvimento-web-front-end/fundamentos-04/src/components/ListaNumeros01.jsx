const numeros = [1, 2, 3, 4, 5];

function ListaNumeros() {
  return (
    <ul style={{ listStyle: "none" }}>
      {numeros.map((numero) => (
        <li key={numero.toString()}>{numero}</li>
      ))}
    </ul>
  );
}

export default ListaNumeros;
