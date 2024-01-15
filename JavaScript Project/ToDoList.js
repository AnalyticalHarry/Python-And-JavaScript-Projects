//function to add task
function addTask(doList, task) {
    // Using push method to add task
    doList.push({ task: task, completed: false });
    console.log(`Task '${task}' added to do list.`);
}

//function to remove task
function removeTask(doList, task) {
    //iterate through doList array
    for (let i = 0; i < doList.length; i++) {
        //compare task from array with the function parameter
        if (doList[i].task === task) {
            // Remove the matching task from the array
            doList.splice(i, 1);
            console.log(`Task '${task}' removed from do list.`);
            return;
        }
    }
    console.log(`Task '${task}' not found in do list.`);
}

//function to mark task as completed
function markCompleted(doList, task) {
    //iterate through doList array
    for (let i = 0; i < doList.length; i++) {
        //compare task from array with the function parameter
        if (doList[i].task === task) {
            //if the list task matches with the function parameter, mark it as completed
            doList[i].completed = true;
            console.log(`Task '${task}' marked as completed.`);
            return;
        }
    }
    console.log(`Task '${task}' not found in the to-do list.`);
}

//function to show list
function showList(doList) {
    //print statement for an empty list
    if (!doList.length) {
        console.log("Do list is empty");
    } else {
        console.log("Do list");
        //iterate through doList array
        for (let i = 0; i < doList.length; i++) {
            //making a status variable for the print function, which can be used to check task status
            let status = doList[i].completed ? "Completed" : "Not Completed";
            console.log(`- ${doList[i].task} (${status})`);
        }
    }
}

//declaring an empty list, which is known as doList
let doList = [];

//adding tasks to "doList" list
addTask(doList, "Buy groceries");
addTask(doList, "Read a book");

//marking a task as completed
markCompleted(doList, "Buy groceries");

//removing a task from the list
removeTask(doList, "Read a book");

//showing the "doList" list
showList(doList);
