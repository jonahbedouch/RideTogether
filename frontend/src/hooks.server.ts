import type { Handle } from '@sveltejs/kit';

export const handle = (async ({ event, resolve }) => {
    const token = event.cookies.get('authToken');
    console.log(token)
    if (token == undefined && event.url.pathname.substring(0,4) == "/app") {
        // We know we're not signed in
        console.log('going to hell')
        return Response.redirect(`${event.url.origin}/`, 301);
    }
    else if (token != undefined && event.url.pathname.substring(0,4) != "/app") {
        console.log('so true bestie')
        return Response.redirect(`${event.url.origin}/app`, 301);
    }
    else {
        return resolve(event);
    }
}) satisfies Handle;