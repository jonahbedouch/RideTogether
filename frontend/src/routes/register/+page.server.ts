import type { Actions } from "./$types";

export const actions: Actions = {
  default: async (event) => {
    const data = await event.request.formData();
    console.log(data)
    const firstName = data.get('firstName');
    const lastName = data.get('lastName');
    const email = data.get('email');
    const username = data.get('username');
    const password = data.get('password');

    console.log(JSON.stringify({
      first_name: firstName,
      last_name: lastName,
      email,
      username,
      password
  }))

    const response = await fetch('http://127.0.0.1:8000/ride/register', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
          first_name: firstName,
          last_name: lastName,
          email,
          username,
          password
      })
    })

    const responseData = await response.json();

    event.cookies.set('id', responseData.id);
  }
};