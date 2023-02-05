import { writable, type Writable } from 'svelte/store';
import type { session } from '../interfaces';

interface rideStore {
    active: boolean;
    selectedSession: number;
    sessions: Array<session>;
}

function createRide() {
	const { subscribe, set, update }: Writable<rideStore> = writable({active: false, selectedSession: -1, sessions: []});

    const replace = (active: boolean, selectedSession: number, sessions: Array<session>) => {
        set({active: active, selectedSession: selectedSession, sessions: sessions});
    }
    const reset = () => {
        set({active: false, selectedSession: -1, sessions: []});
    }

	return {
		subscribe,
        replace,
        reset
	};
}

export const rideStore = createRide();