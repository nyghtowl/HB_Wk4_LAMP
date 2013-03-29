// First exercise working with expressions and functions

function squareNumber(num){
	return num * num;
}

function halfNumber(num){
	return num/2;
}

function percentOf(num1, num2){
	return (1-(num2-num1)/num2);
}

function areaOfCirlce(rad){
	a = 3.14 * rad * rad; 
// approach to round a number 
	return a.toFixed([2]);
}

function combine(n){
	var ans = halfNumber(n);
	ans = squareNumber(ans);
	ans = areaofCircle(ans);
	return percentOf(ans, squareNumber(ans));
}

// Second exercise working with conditionals and arrays

// set variables - if outside function then global and accesible in function
var ans = ['F', 'O', 'X'];
var guess = ['_','_' ,'_'];
var win = 0;

// set it like Wheel of Fortune with a reward
console.log("Guess a letter to find the answer. Every correct guess will win you money")


// take the guessed letter
function guessLetter(letter){

	// loop through the length of ans for var i in ans would loop through the letters
	for (var i =0; i < ans.length; i++) {
		var found = false;
		// compare the submitted letter to each letter in ans 
		if (letter === ans[i]){
			// if they are the same change the guess character at the same index to that letter
			guess[i] = letter;
			console.log("Congrats, you found a new letter.");
			found = true;
		}
		// determine if answer complete
		if (ans === guess) {
			console.log = ("Congrats on winning the game!");
			//breaks from the loop
			break;
		}
	}
	// outside loop check if the letter was found and if not then print try again
	if (found === false){
		console.log(letter);
	}
		
}