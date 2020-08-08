import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function MyInfo() {
  return (
    <div>
      <p></p>
      <h1>Alex Horton</h1>
      <p>
        <p>Top Three Vacation Spots to Visit are</p>
        <ol>
          <li>Hawaii</li>
          <li>Japan</li>
          <li>France</li>
        </ol>
      </p>
    </div>)
}

ReactDOM.render( 
  <MyInfo />
  , document.getElementById("root")
)