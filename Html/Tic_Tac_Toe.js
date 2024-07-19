let boxes = document.querySelectorAll(".box");
let resetbtn = document.querySelector("#resetbtn");
let newGamebtn = document.querySelector("#newGamebtn");
let msgContainer = document.querySelector(".msg-container");
let msg = document.querySelector("#msg");

let turnO = true;  // playeO and playerX
let count = 0;     // Initialize the count variable

const winPatterns = [   // by this 2D array pattern we will decide the winner.
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8]
];

const resetGame = () => {
    turnO = true;
    count = 0;
    enableBoxes();
    msgContainer.classList.add("hide");
}

boxes.forEach((box) => {
    box.addEventListener("click", () => {
        // console.log("box was clicked!");
        if (turnO) {   // if the turn of player O. then innerText = O.
            box.innerText = "O";
            turnO = false;
        } else {       // if the turn of player X. then innerText = X.
            box.innerText = "X";
            turnO = true;
        }
        box.disabled = true;
        count++;

        let isWinner = checkWinner();

        if (count === 9 && !isWinner) {
            draw();
        }
    });
});

const draw = () => {
    msg.innerText = `It's a Draw`;
    msgContainer.classList.remove("hide");
    disableBoxes();
}

const disableBoxes = () => {      // This function is used to disable the boxes when one of the players wins the game.
    for (let box of boxes) {
        box.disabled = true;
    }
}

const enableBoxes = () => {      // This function is used to enable the boxes to restart the game.
    for (let box of boxes) {
        box.disabled = false;
        box.innerText = "";
    }
}

const showWinner = (winner) => {
    msg.innerText = `Congratulations, Winner is ${winner}`;
    msgContainer.classList.remove("hide");
    disableBoxes();       // calling disable function
}

const checkWinner = () => {
    for (let pattern of winPatterns) {
        let pos1 = boxes[pattern[0]].innerText;
        let pos2 = boxes[pattern[1]].innerText;
        let pos3 = boxes[pattern[2]].innerText;

        if (pos1 !== "" && pos1 === pos2 && pos2 === pos3) {
            // console.log("winner", pos1);
            showWinner(pos1);    // here calling showWinner function.
            return true;
        }
    }
    return false;
}

newGamebtn.addEventListener("click", resetGame);
resetbtn.addEventListener("click", resetGame);
