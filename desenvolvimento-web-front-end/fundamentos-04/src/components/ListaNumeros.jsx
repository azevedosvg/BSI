const numeros = [1, 2, 3, 4, 5];

function ListaNumeros() {
  return (
    <ul style={{ textAlign: "left" }}>
      {/* 
        map percorre o array e transforma cada número em um <li>
        a arrow function já retorna direto o JSX (sem precisar de return)
      */}
      {numeros.map((numero) => (
        // key identifica cada item da lista (aqui usamos o próprio número)
        // toString() só garante que vire string (não é obrigatório nesse caso)
        <li key={numero.toString()}>{numero}</li>
      ))}
    </ul>
  );
}

export default ListaNumeros;
