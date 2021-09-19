import React from 'react';

function Food({name, picture}){
  return (
    <div>
    <h2>I like {name}</h2>
    <img src = {picture} />
  </div>
  );
}


const foodILike = [ // 데이터 입력
  {name : 'KimChi',
image : 'https://cdn.imweb.me/thumbnail/20200415/6b6e035658bac.png',},
{
  name : '불고기',
  image : 'https://recipe1.ezmember.co.kr/cache/recipe/2016/12/30/df939769792632a48a0eba8bc895e8601.jpg',
},
{
  name : 'Bibimbap',
  image : 'https://t1.daumcdn.net/liveboard/SNUH/fed8c48df21b43ada043b4cdda7dfe57.JPG',
},
];

function App() {
  //return <div className="App"/>;
  return ( // App component가 HTML 반환
  <div>
    { <h1>Hello</h1> }
   {foodILike.map(dish => (
    <Food name={dish.name} picture={dish.image}/>
    ))}
    </div>
  );
}

export default App;