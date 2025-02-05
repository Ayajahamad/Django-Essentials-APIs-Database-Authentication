console.log("hello");

// To Get the data
function taskList(url) {
    let ul = document.getElementById('task_list')

    fetch(url)
        .then((data) => data.json())
        .then((data) => {
        console.log(data);
    })
}

let url = 'http://127.0.0.1:8000/api_first/tasks/'
taskList(url)


// To submit the data
let form = document.getElementById('tasksubmit')
form.addEventListener('submit', (e) => {
    e.preventDefault();

    const title = document.getElementById('title').value
    const description = document.getElementById('description').value
    const completed = document.getElementById('completed')

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify({
            title: title,
            description: description,
            complete: completed.checked ? true:false,
        })
    })
    .then((res) => res.json())
    .then((data) => {
    console.log(data);
    }).catch((e) => {
    console.log("error :", e);
})
form.reset()
})

// To get single task
let single_task = document.getElementById('single_task')

single_task.addEventListener('click', (e) => {
    e.preventDefault()
    let number = document.getElementById('number').value

    if (!number) {
        alert('Please enter the number')
    }
    fetch(`http://127.0.0.1:8000/api_first/tasks/${number}/`)
        .then((data) => data.json())
        .then((data) => {
            document.getElementById('u_title').value = data.title
            document.getElementById('u_description').value = data.description
            document.getElementById('u_completed').checked = data.complete

            update(number)
            console.log(data);
        })
    
})

// For Deleting the task
let dlt_task = document.getElementById('delete_task')
dlt_task.addEventListener('click', ((e) => {
    e.preventDefault()
    let dlt = document.getElementById("delete").value

    if (!dlt) {
        alert('Please enter the number')
    }

    fetch(`http://127.0.0.1:8000/api_first/tasks/${dlt}/`, {
        method: 'DELETE'
    })
        .then((response) => {
            if (!response.ok) {
                console.log(response.status);
                alert("failed to delete the task")
                return;
            }

            if (response.status == 204) {
                alert("Deleted Successfully..!")
                console.log(response);
                return;
            }
            return response.json()
        })
        .then((data) => {
            if (data) {
                console.log(data);
            }
        }).catch((err) => console.log(err))

}));

// For updating the data Im getting the data in Get single task
function update(u_id) {
    let u_form = document.getElementById('update_task')

    u_form.addEventListener('submit', (e) => {
        e.preventDefault();

        const title = document.getElementById('u_title').value
        const description = document.getElementById('u_description').value
        const completed = document.getElementById('u_completed')

        fetch(`http://127.0.0.1:8000/api_first/tasks/${u_id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: title,
                description: description,
                complete: completed.checked ? true : false,
            })
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            }).catch((e) => {
                console.log("error :", e);
            })
        
            u_form.reset();
    });
}