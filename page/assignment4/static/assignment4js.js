function func_users() {

    fetch('https://reqres.in/api/users').then(
        response => response.json()
    ).then(
        response => get_user_fe(response.data)
    ).catch(
        err => console.log(err)
    );
}

function get_user_fe(response) {
    const currMain = document.querySelector("main")
    const user_id = document.getElementById("id_user_front").value;
     num = 0;
    currMain.innerHTML = "";
    if (user_id == 0) {
        num = 0;
        for (let user of response) {
            const section = document.createElement('section')
            section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
             <span>${user.first_name} ${user.last_name}</span>
             <br>
             <a href="mailto:${user.email}"> Email</a>
            </div>
        `
            currMain.appendChild(section)
        }
    }
 if (user_id != 0) {
     for (let user of response) {
         num = num+1;
         const section = document.createElement('section')
         if (user_id == num)
             section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
             <span>${user.first_name} ${user.last_name}</span>
             <br>
             <span>${user.last_name} ${user.last_name}</span>
             <br>
             <a href="mailto:${user.email}"> Email </a>
             <br><br>
            </div>
        `
         currMain.appendChild(section)
     }
 }
}

