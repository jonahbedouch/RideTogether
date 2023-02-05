import type { Handle } from '@sveltejs/kit';

export const handle = (async ({ event, resolve }) => {
    const token = event.cookies.get('authToken');
    if (token == undefined && event.url.pathname.substring(0,4) == "/app") {
        // We know we're not signed in
        return Response.redirect(`${event.url.origin}/`, 301);
    }
    else if (token != undefined && event.url.pathname.substring(0,4) != "/app") {
        return Response.redirect(`${event.url.origin}/app`, 301);
    }
    else {
        return resolve(event);
    }
}) satisfies Handle;