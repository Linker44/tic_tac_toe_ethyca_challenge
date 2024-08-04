import './App.css';
import Board from './components/Board';
import PreviousGame from './components/PreviousGame';
import { useState } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

function App() {
  const [showPreviousGames, setShowPreviousGames] = useState(false);
  const [previousGames, setPreviousGames] = useState([]);

  function handlePreviousGames(){
    try{
      axios.get(API_URL).then((response) => {
        let data = response.data;
        setPreviousGames(data);
        }
      )
    } catch (error){
      console.error('Couldnt Get previous games');
    }
    setShowPreviousGames(!showPreviousGames);
  }

  return (
    <div className="App">
      <Board></Board>
      <button onClick={handlePreviousGames}>Show Previous Games</button>
      {showPreviousGames ? (previousGames.length > 1 ? previousGames.map((obj) => <PreviousGame className="previous" board={obj.board}></PreviousGame>) : null) : null}
    </div>
  );
}

export default App;
