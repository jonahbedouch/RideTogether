import { writable } from 'svelte/store';

function createDrive() {
	const { subscribe, set, update } = writable({ active: false, id: '', driver: '', passengers_max: 0, start_dest: [0, 0], end_dest: [0, 0], original_route: [[0, 0]], passengers: [0], timestamp: 0 });

    const replace = (active: boolean, id: string, driver: string, passengers_max: number, start_dest: number[], end_dest: number[], original_route: number[][], passengers: number[], timestamp: number) => {
        set({active: active, id: id, driver: driver, passengers_max: passengers_max, start_dest: start_dest, end_dest: end_dest, original_route: original_route, passengers: passengers, timestamp: timestamp})
    }
    const reset = () => {
        set({ active: false, id: '', driver: '', passengers_max: 0, start_dest: [0, 0], end_dest: [0, 0], original_route: [[0, 0]], passengers: [0], timestamp: 0 });
    }

	return {
		subscribe,
        replace,
        reset
	};
}

export const driveStore = createDrive();