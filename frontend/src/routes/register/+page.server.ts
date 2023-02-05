import { redirect } from "@sveltejs/kit";
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

    const response = await fetch('https://kyle518.pythonanywhere.com/ride/register/', {
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

    const tokenReponse = await fetch('https://kyle518.pythonanywhere.com/ride/api-token-auth/', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        password
      })
    })

    const tokenResponseData = await tokenReponse.json();

    event.cookies.set('authToken', tokenResponseData.token, {path: '/'});
    throw redirect(301, '/app')
  }
};