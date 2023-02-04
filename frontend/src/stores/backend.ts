import { writable } from "svelte/store";

function createBackend() {
    const { subscribe, set, update } = writable({ sidebar: false });

    return {
        subscribe,
        toggleSidebar: () => { update(backend => {return {sidebar: !backend.sidebar}}) }
    }
}

export const backendStore = createBackend();