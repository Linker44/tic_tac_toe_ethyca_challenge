import Square from "./Square";
import { useState} from "react";
import axios from 'axios';

const API_URL = 'http://localhost:8000';

export default function Board() {
    const [gameId, setGameId] = useState(null);
    const [squares, setSquares] = useState(Array(3).fill(null).map(() => Array(3).fill(null)));
    const [gameStart, setGameStart] = useState(false);
    const [gameWinner, setGameWinner] = useState(null);

    function HandleNewGame(){
        if(!gameStart){
            setGameStart(true);
        }
        try{
            axios.post(`${API_URL}/`).then((response) => {
            let data = response.data;
            console.log(data);
            setSquares(data.board);
            setGameId(data.id);
            setGameWinner(data.winner);
        });
        } catch (error){
            console.error("couldnt create a new game");
        }
    }

    function HandleClick(x, y){
        if(squares[x][y] || gameWinner){
            return null;
        }

        try{
            axios.put(`${API_URL}/${gameId}/move/`, {"x": x, "y": y}).then((response) => {
                let data = response.data;
                setSquares(data.board);
                setGameWinner(data.winner);
            })
        } catch(error){
            console.error("Error making move", error);
        }
    }

    return (
        <>
        {gameStart && <>
        
        <div className="board-row">
            <Square value={squares[0][0]} onSquareClick={() => HandleClick(0, 0)}/>
            <Square value={squares[0][1]} onSquareClick={() => HandleClick(0, 1)}/>
            <Square value={squares[0][2]} onSquareClick={() => HandleClick(0, 2)}/>
        </div>
        <div className="board-row">
            <Square value={squares[1][0]} onSquareClick={() => HandleClick(1, 0)}/>
            <Square value={squares[1][1]} onSquareClick={() => HandleClick(1, 1)}/>
            <Square value={squares[1][2]} onSquareClick={() => HandleClick(1, 2)}/>
        </div>
        <div className="board-row">
            <Square value={squares[2][0]} onSquareClick={() => HandleClick(2, 0)}/>
            <Square value={squares[2][1]} onSquareClick={() => HandleClick(2, 1)}/>
            <Square value={squares[2][2]} onSquareClick={() => HandleClick(2, 2)}/>
        </div>
        {gameWinner ? <h1 className="status">Winner: {gameWinner}</h1> : null}
        </>}
        <button onClick={HandleNewGame}>New Game</button>
        </>
    );
}