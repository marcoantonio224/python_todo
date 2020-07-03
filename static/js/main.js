const errorElement = document.getElementById('error');

/* ============ CREATE A TODO ITEM ============== */
document.getElementById('form').onsubmit = (e)=> {
  e.preventDefault();
  let description = document.getElementById('description')
  const data = ['description', description.value]; // [key, value]
  // Custom API with fetch method
  makeRequest('/todos/create', 'POST', data)
  .then((response)=>{
    return response.json();
  })
  .then((jsonResponse) => {
    let liItem = document.createElement('li');
    liItem.textContent = jsonResponse['description'];
    document.getElementById('todos').appendChild(liItem);
    errorElement.className = "hidden";
    description.value ='';
  })
  .catch(err => {
    console.log(err)
    errorElement.className = "";
  });
}
/* ===================================================== */

/* ============ UPDATE CHECKBOX TO COMPLETED =========== */
const checkboxes = document.querySelectorAll('.check-completed');
for(let i = 0;  i < checkboxes.length; i++) {
  const checkbox = checkboxes[i];
  checkbox.onchange = function(e) {
    const newCompleted = e.target.checked;
    const todoID = e.target.dataset['id'];
    const data = ['completed', newCompleted]; // [key, value]
    makeRequest(`/todos/${todoID}/set-completed`, 'POST', data)
    .then(()=>{
      errorElement.className = "";
    })
    .catch(err => {
      console.log(err)
      errorElement.className = "";
    });
  }
}
/* ===================================================== */

function makeRequest(url, method, data) {
  const key = data[0];
  const value = data[1];
  return fetch(url, {
            method: method,
            body: JSON.stringify({
              [key] : value
            }),
            headers: {
              'Content-Type': 'application/json'
            }
      })
}