import React, { useState } from "react";
import ReactDOM from "react-dom";

const wasm = import("../build/robotlox");

wasm.then((m) => {
  const App = () => {
    return (
      <>
        <div>
          <h1> Rust in Browser 😎</h1>
          <button onClick={m.welcome}>Hello</button>
        </div>
      </>
    );
  };

  ReactDOM.render(<App />, document.getElementById("root"));
});