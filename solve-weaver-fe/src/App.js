// import logo from './logo.svg';
import './App.css';

import React, { useState } from 'react';

// The WordBox component represents each letter box
const WordBox = ({ letter, isMatch, isGray }) => {
  const style = {
    backgroundColor: isMatch ? 'lightgreen' : isGray ? 'gray' : 'white',
    color: isGray ? 'white' : 'black',
    border: '1px solid black',
    display: 'inline-block',
    width: '40px',
    height: '40px',
    textAlign: 'center',
    lineHeight: '40px',
    margin: '5px',
    fontWeight: 'bold'
  };
  
  return <div style={style}>{letter}</div>;
};

// The WordRow component represents a row of letter boxes
const WordRow = ({ word, targetWord }) => {
  return (
    <div>
      {word.split('').map((letter, index) => (
        <WordBox
          key={index}
          letter={letter.toUpperCase()}
          isMatch={targetWord && targetWord[index] === letter}
          isGray={!targetWord}
        />
      ))}
    </div>
  );
};

const getWordLadder = async (backendURL, startWord, endWord) => {
  // Base URL can be set as an environment variable or configuration setting
  var baseUrl = `http://${backendURL}/wordladder`;

  try {
    const response = await fetch(`${baseUrl}/${startWord}/${endWord}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    if (data) {
      console.log(`Answer is: ${data} (${data.length})`);
    } else {
      console.log(`No answer.`)
    }
    return data; // Your API should return the solution in JSON format
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
};

// The main App component where users can input words and see the solution
const App = () => {
  const [backendURL, setBackendURL] = useState('localhost:8000');
  const [startWord, setStartWord] = useState('');
  const [endWord, setEndWord] = useState('');
  const [solution, setSolution] = useState([]);

  // Function to call the REST API and set the solution
  const findSolution = async () => {
    // You will need to replace this with the actual API call
    // and set the solution with the response data
    var solution = await getWordLadder(backendURL, startWord, endWord);
    console.log(`Got a solution of type ${typeof(solution)}`);
    if (solution) {
      if (solution.length > 2) {
        solution.shift();
        solution.pop();
      }
      solution.map((word, index) => (console.log(`${index}: ${word}`)));
      setSolution(solution);
    } else {
      setSolution([]);
    }
  };

  return (
    <div>
    <h1>Word Weaver Solver</h1>
    <table>
      <tbody>
      <tr>
      <td>
        <label htmlFor="backendURL">Back end server & port: </label>
       </td>
       <td> 
        <input
          type="text"
          id="backendURL"
          value={backendURL}
          onChange={(e) => setBackendURL(e.target.value)}
          onKeyDown={(e) => { if (e.key === 'Enter') { document.getElementById("startWord").focus(); }}}
          placeholder="localhost:8000"
        />
      </td>
      </tr>
      <tr>
      <td>
        <label htmlFor="startWord">Start Word: </label>
      </td>
      <td>
        <input
          type="text"
          id="startWord"
          value={startWord}
          onChange={(e) => setStartWord(e.target.value)}
          onKeyDown={(e) => { if (e.key === 'Enter') { document.getElementById("targetWord").focus(); }}}
          placeholder="Start word"
        />
      </td>
      </tr>
      <tr>
      <td><label htmlFor="targetWord">Target Word:</label></td>
      <td>
      <input
        type="text"
        id="targetWord"
        value={endWord}
        onChange={(e) => setEndWord(e.target.value)}
        onKeyDown={(e) => { if (e.key === 'Enter') { findSolution(); }}}
        placeholder="End word"
      />
      </td>
      </tr>
      </tbody>
      </table>
      <div>
        <button onClick={findSolution}>Find Solution</button>
      </div>
      <WordRow word={startWord} />
      {solution.map((word, index) => (
        <WordRow key={index} word={word} targetWord={endWord} />
      ))}
      <WordRow word={endWord} />
    </div>
  );
};

export default App;


/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/
