import { useState, useEffect } from "react";
import "./Calculadora.css";

const Calculadora = () => {
  const [form, setForm] = useState({
    valor1: 0,
    valor2: 0,
  });

  const [resultado, setResultado] = useState(0);
  // novo
  const [operacao, setOperacao] = useState("");

  const somar = () => {
    setResultado(Number(form.valor1) + Number(form.valor2));
    // novo
    setOperacao("+");
  };

  const subtrair = () => {
    setResultado(Number(form.valor1) - Number(form.valor2));
    // novo
    setOperacao("-");
  };

  const multiplicar = () => {
    setResultado(Number(form.valor1) * Number(form.valor2));
    // novo
    setOperacao("*");
  };

  const dividir = () => {
    if (Number(form.valor2) === 0) {
      setResultado("Erro: divisão por zero");
    } else {
      setResultado(Number(form.valor1) / Number(form.valor2));
    }
    // novo
    setOperacao("/");
  };

  const resto = () => {
    if (Number(form.valor2) === 0) {
      setResultado("Erro: divisão por zero");
    } else {
      setResultado(Number(form.valor1) % Number(form.valor2));
    }
    // novo
    setOperacao("%");
  };

  // novo
  const limpar = () => {
    setForm({ valor1: 0, valor2: 0 });
    setResultado(0);
    setOperacao("");
  };

  useEffect(() => {
    console.log("Valores:", form);
  }, [form]);

  /*      Removi esse useEffect para que o resultado não sofra reset quando o valor do formulário mudar.
  useEffect(() => {
    setResultado(0);
  }, [form]);
  */

  return (
    <div className="calculadora">
      {/* <div className="resultado">
        {form.valor1} {operacao} {form.valor2} = {resultado}
      </div> */}

      {/* atualizado */}
      <div className="display">
        {operacao === "" ? (
          "Digite Valores"
        ) : (
          <>
            {form.valor1} {operacao} {form.valor2}
            <br />= {resultado}
          </>
        )}
      </div>

      <div className="inputs">
        {/*<div className="inputs">
        <input
          type="number"
          value={form.valor1}
          onChange={(e) => setForm({ ...form, valor1: e.target.value })}
        /> */}

        {/* atualizado */}
        <input
          placeholder="Valor 1"
          type="number"
          value={form.valor1 || ""}
          onChange={(e) => setForm({ ...form, valor1: e.target.value })}
        />

        {/* atualizado */}
        <input
          placeholder="Valor 2"
          type="number"
          value={form.valor2 || ""}
          onChange={(e) => setForm({ ...form, valor2: e.target.value })}
        />
      </div>

      <div className="botoes">
        <button onClick={somar}>+</button>
        <button onClick={subtrair}>-</button>
        <button onClick={multiplicar}>*</button>
        <button onClick={dividir}>/</button>
        <button onClick={resto}>%</button>
        {/* novo */}
        <button onClick={limpar}>C</button>
      </div>
    </div>
  );
};

export default Calculadora;
