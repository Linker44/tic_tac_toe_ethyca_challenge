import Square from "./Square"

export default function PreviousGame({board}){
    return <div className="previous"> 
            <div className="board-row">
                <Square value={board[0][0]} onSquareClick={() => null}/>
                <Square value={board[0][1]} onSquareClick={() => null}/>
                <Square value={board[0][2]} onSquareClick={() => null}/>
            </div>
            <div className="board-row">
                <Square value={board[1][0]} onSquareClick={() => null}/>
                <Square value={board[1][1]} onSquareClick={() => null}/>
                <Square value={board[1][2]} onSquareClick={() => null}/>
            </div>
            <div className="board-row">
                <Square value={board[2][0]} onSquareClick={() => null}/>
                <Square value={board[2][1]} onSquareClick={() => null}/>
                <Square value={board[2][2]} onSquareClick={() => null}/>
            </div>
        </div>
}