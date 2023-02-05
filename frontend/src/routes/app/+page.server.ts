import { redirect } from "@sveltejs/kit";
import type { Actions } from "./$types";

export const actions: Actions = {
    drive: async (event) => {
        const data = await event.request.formData();
        const origin = data.get('driveOrigin');
        const dest = data.get('driveDest');
        const passengers_max = data.get('maxPassengers');
        const timestart = Date.now();
        const token = event.cookies.get('authToken');

        try {
            const response = await fetch('http://127.0.0.1:8000/ride/start/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Token ${token}`
                },
                body: JSON.stringify({
                    origin,
                    dest,
                    passengers_max,
                    timestart
                })
            })

            if (response.status == 401) {
                event.cookies.delete('authToken');
                throw redirect(301, '/')        
            }

            let x = await response.json();
            
            return x;
        }
        catch {
        }
    },
    ride: async (event) => {
        const data = await event.request.formData();
        const origin = data.get('rideOrigin');
        const dest = data.get('rideDest');
        const people_amt = data.get('passengerCnt');
        const timestart = Date.now();
        const token = event.cookies.get('authToken');

        console.log(origin, dest, people_amt)


        try {
            const response = await fetch('http://127.0.0.1:8000/ride/find/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Token ${token}`
                },
                body: JSON.stringify({
                    origin,
                    dest,
                    people_amt,
                    timestart
                })
            })

            if (response.status == 401) {
                event.cookies.delete('authToken');
                throw redirect(301, '/')        
            }

            return await response.json();
        }
        catch {
            
        }
    },
};