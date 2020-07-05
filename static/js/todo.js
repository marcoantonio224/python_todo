const errorElement = document.getElementById('error');

/*  Custom Fetch Helper  */
function makeRequest(url, method, data) {
  // Check to see if data was passed in
  if(data === undefined) {
    return fetch(url,
      { method: method, headers: {'Content-Type': 'application/json' }
    })
  } else {
    // Send request with data to the user
      return fetch(url, {
                method: method,
                body: JSON.stringify({
                  data : data
                }),
                headers: {
                  'Content-Type': 'application/json'
                }
          })
  }
}
// Assign makeRequest a global function
window.makeRequest = makeRequest;

// ============= API CRUD METHODS =================
/* ============ CREATE A TODO ITEM ============== */
document.getElementById('form').onsubmit = (e)=> {
  e.preventDefault();
  let description = document.getElementById('description');
  const list_id = location.pathname.split('').pop();
  const data = {
    description: description.value,
    list_id: list_id
  }
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
    location.reload();
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
      errorElement.className = "hidden";
    })
    .catch(err => {
      console.log(err)
      errorElement.className = "";
    });
  }
}
/* ===================================================== */

/* ============ DELETE TODO ITEM =========== */
  const deleteButtons = document.querySelectorAll('.delete');
  for(let i =0; i < deleteButtons.length; i++) {
    const deleteButton = deleteButtons[i];
    deleteButton.onclick = function(e) {
      const todoID = e.target.dataset['id'];
      makeRequest(`/todos/${todoID}/set-completed`, 'DELETE')
      .then((response)=>{
        return response.json();
      })
      .then((jsonResponse) => {
        const { todoID } = jsonResponse;
        const todoItemDelete = document.getElementById('todo-item-'+todoID);
        console.log(todoItemDelete)
        todoItemDelete.remove();
        errorElement.className = "hidden";
      })
      .catch(err => {
        console.log(err)
        errorElement.className = "";
      });
    }
  }
/* ===================================================== */



