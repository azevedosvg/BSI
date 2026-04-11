import { useState, useEffect } from "react";
import "./Calculadora.css";

const Calculadora = () => {
  const [form, setForm] = useState({
    valor1: 0,
    valor2: 0,
  });

  const [resultado, setResultado] = useState(0);

  const somar = () => {
    setResultado(Number(form.valor1) + Number(form.valor2));
  };

  const subtrair = () => {
    setResultado(Number(form.valor1) - Number(form.valor2));
  };

  const multiplicar = () => {
    setResultado(Number(form.valor1) * Number(form.valor2));
  };

  const dividir = () => {
    if (Number(form.valor2) === 0) {
      setResultado("Erro: divisão por zero");
    } else {
      setResultado(Number(form.valor1) / Number(form.valor2));
    }
  };

  const resto = () => {
    if (Number(form.valor2) === 0) {
      setResultado("Erro: divisão por zero");
    } else {
      setResultado(Number(form.valor1) % Number(form.valor2));
    }
  };

  useEffect(() => {
    console.log("Valores:", form);
  }, [form]);

  useEffect(() => {
    setResultado(0);
  }, [form]);

  return (
    <div className="calculadora">
      <div className="inputs">
        <input
          type="number"
          value={form.valor1}
          onChange={(e) => setForm({ ...form, valor1: e.target.value })}
        />

        <input
          type="number"
          value={form.valor2}
          onChange={(e) => setForm({ ...form, valor2: e.target.value })}
        />
      </div>

      <div className="botoes">
        <button onClick={somar}>+</button>
        <button onClick={subtrair}>-</button>
        <button onClick={multiplicar}>*</button>
        <button onClick={dividir}>/</button>
        <button onClick={resto}>%</button>
      </div>

      <div className="resultado">Resultado: {resultado}</div>
    </div>
  );
};

export default Calculadora;
