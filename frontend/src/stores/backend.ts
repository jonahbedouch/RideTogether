import { writable } from "svelte/store";

function createBackend() {
    const { subscribe, set, update } = writable({ sidebar: false, drive: false, ride: false });

    return {
        subscribe,
        toggleSidebar: () => { update(backend => {return {sidebar: !backend.sidebar, drive: backend.drive, ride: backend.ride}})}, 
        toggleDrive: () => { update(backend => {return {sidebar: backend.sidebar, drive: !backend.drive, ride: backend.ride}})}, 
        toggleRide: () => { update(backend => {return {sidebar: backend.sidebar, drive: backend.drive, ride: !backend.ride}})}
    }
}

export const backendStore = createBackend();