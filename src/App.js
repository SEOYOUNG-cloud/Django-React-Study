import React from 'react';

function Food({fav}){
  return <h1>I like {fav}</h1>;
}

function App() {
  //return <div className="App"/>;
  return ( // App component가 HTML 반환
  <div>
    <h1>Hello</h1>
    <Food fav="김치" />
    <Food fav="samsung"/>
    <Food fav="coffee"/>
    </div>
  );
}

export default App;