import { useState, useEffect } from "react";
import "./Calculadora.css";

/* Calculadora v3.0:  */
const Calculadora = () => {
  /* const [form, setForm] = useState({
    valor1: 0,
    valor2: 0,
  });
    */

  /* Calculadora v3.0:  */
  const [valor, setValor] = useState("");
  const [valorAnterior, setValorAnterior] = useState(null);
  const [operacao, setOperacao] = useState(null);

  // const [resultado, setResultado] = useState(0);
  // novo
  // const [operacao, setOperacao] = useState("");

  /* Calculadora v3.0:  */
  const adicionarNumero = (num) => {
    setValor(valor + num);
  };

  /* Calculadora v3.0:  */
  const escolherOperacao = (op) => {
    setValorAnterior(valor);
    setOperacao(op);
    setValor("");
  };

  /* Calculadora v3.0:  */
  const calcular = () => {
    const v1 = Number(valorAnterior);
    const v2 = Number(valor);

    let res;

    switch (operacao) {
      case "+":
        res = v1 + v2;
        break;
      case "-":
        res = v1 - v2;
        break;
      case "*":
        res = v1 * v2;
        break;
      case "/":
        res = v2 === 0 ? "Erro: Divisão por zero" : v1 / v2;
        break;
      default:
        return;
    }

    setValor(String(res));
    setOperacao(null);
    setValorAnterior(null);
  };

  /* Calculadora v3.0:  */
  const limpar = () => {
    setValor("");
    setValorAnterior(null);
    setOperacao(null);
  };

  /* Calculadora v3.0:  */
  const apagar = () => {
    setValor(valor.slice(0, -1));
  };

  /* Removido (sem necessidade para a v3.0 da calculadora)
  const somar = () => {
    setResultado(Number(form.valor1) + Number(form.valor2));
    * novo
    setOperacao("+");
  };

  const subtrair = () => {
    setResultado(Number(form.valor1) - Number(form.valor2));
    * novo
    setOperacao("-");
  };

  const multiplicar = () => {
    setResultado(Number(form.valor1) * Number(form.valor2));
    * novo
    setOperacao("*");
  };

  const dividir = () => {
    if (Number(form.valor2) === 0) {
      setResultado("Erro: divisão por zero");
    } else {
      setResultado(Number(form.valor1) / Number(form.valor2));
    }
    * novo
    setOperacao("/");
  };

  const resto = () => {
    if (Number(form.valor2) === 0) {
      setResultado("Erro: divisão por zero");
    } else {
      setResultado(Number(form.valor1) % Number(form.valor2));
    }
    * novo
    setOperacao("%");
  };
  */

  //  * novo
  // const limpar = () => {
  //   setForm({ valor1: 0, valor2: 0 });
  //   setResultado(0);
  //   setOperacao("");
  // };

  // removendo coisas do formulario que não está mais sendo usada na v3.0 da calculadora
  // useEffect(() => {
  //   console.log("Valores:", form);
  // }, [form]);

  /*      Removi esse useEffect para que o resultado não sofra reset quando o valor do formulário mudar.
  useEffect(() => {
    setResultado(0);
  }, [form]);
  */

  return (
    <div className="calculadora">
      <h2 className="titulo">Calculadora Simples</h2>
      {/* <div className="resultado">
        {form.valor1} {operacao} {form.valor2} = {resultado}
      </div> */}
      {/* Removido (sem necessidade para a v3.0 da calculadora)
      {/* * atualizado *
      <div className="display">
        {operacao === "" ? (
          "Digite Valores"
        ) : (
          <>
            {form.valor1} {operacao} {form.valor2}
            <br />= {resultado}
          </>
        )}
      </div> */}
      {/* <div className="inputs">
        <div className="inputs">
        <input
          type="number"
          value={form.valor1}
          onChange={(e) => setForm({ ...form, valor1: e.target.value })}
        />

        * atualizado *
        <input
          placeholder="Valor 1"
          type="number"
          value={form.valor1 || ""}
          onChange={(e) => setForm({ ...form, valor1: e.target.value })}
        />

        * atualizado *
        <input
          placeholder="Valor 2"
          type="number"
          value={form.valor2 || ""}
          onChange={(e) => setForm({ ...form, valor2: e.target.value })}
        />
      </div> */}
      {/* Calculadora v3.0: Deletando inputs para adicionar botões para mais realismo no projeto */}
      {/* <div className="botoes">
        <button onClick={somar}>+</button>
        <button onClick={subtrair}>-</button>
        <button onClick={multiplicar}>*</button>
        <button onClick={dividir}>/</button>
        <button onClick={resto}>%</button>
        * novo *
        <button onClick={limpar}>C</button>
      </div> */}
      {/* Calculadora v3.0:  */}
      <div className="display">
        {valorAnterior} {operacao}
        <br />
        {valor || "0"}
      </div>

      <div className="botoes">
        <button className="limpar" onClick={limpar}>
          C
        </button>
        <button onClick={apagar}>⌫</button>
        <button onClick={() => escolherOperacao("/")}>/</button>
        <button onClick={() => escolherOperacao("*")}>*</button>

        <button onClick={() => adicionarNumero("7")}>7</button>
        <button onClick={() => adicionarNumero("8")}>8</button>
        <button onClick={() => adicionarNumero("9")}>9</button>
        <button onClick={() => escolherOperacao("-")}>-</button>

        <button onClick={() => adicionarNumero("4")}>4</button>
        <button onClick={() => adicionarNumero("5")}>5</button>
        <button onClick={() => adicionarNumero("6")}>6</button>
        <button onClick={() => escolherOperacao("+")}>+</button>

        <button onClick={() => adicionarNumero("1")}>1</button>
        <button onClick={() => adicionarNumero("2")}>2</button>
        <button onClick={() => adicionarNumero("3")}>3</button>

        <button className="igual" onClick={calcular}>
          =
        </button>

        <button className="zero" onClick={() => adicionarNumero("0")}>
          0
        </button>
        <button onClick={() => adicionarNumero(".")}>.</button>
      </div>
    </div>
  );
};

export default Calculadora;
