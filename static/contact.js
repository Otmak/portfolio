const form = document.getElementById('form')
const email = document.getElementById('email')
const subject = document.getElementById('subject');
const message = document.getElementById('message');
let checker = true;
form.addEventListener('submit', (e)=> {
	if ( validate(email,e) === validate(message,e) === checker ) {
		console.log('submiting...')
	}
	// console.log( validate(email,e) === validate(message,e), 'COMPARE', checker )
	// console.log( 'email:', validate(email,e), 'massage: ',validate(message,e), 'checker:',checker)
})

function validate(tag, target='') {
	let value = tag.value
	if ( value !== '') {
		checker = true
		tag.style.border = '1px solid rgb(35, 255, 57)'
		return true

	} else {
		tag.style.border = '1px solid rgb(255, 57, 35)';
		checker = false
		target.preventDefault()
		return false
	}
	
}




//   validate form
// - validate form (validate returns true or false)
// 	- 1 check inputs for empty value
		// - check if value is ''
		// - if its empty se border to red and prevent submit
		// - 
// 	- 2 
// - send info to server
// 	- gather all required info & send to server