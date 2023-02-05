import { redirect } from '@sveltejs/kit';
import type { Actions } from './$types';
 
export const actions: Actions = {
  default: async (event) => {
    const data = await event.request.formData();
    const username = data.get('username');
    const password = data.get('password');

    const response = await event.fetch('http://127.0.0.1:8000/ride/api-token-auth/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username,
            password
        })
    })

    const responseData = await response.json();
    
    console.log(responseData.token);

    if (responseData.token) {
        event.cookies.set('authToken', responseData.token, {path: '/'});
        throw redirect(301, '/app')
    }

  }
};