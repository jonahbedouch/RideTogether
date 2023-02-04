import { writable } from 'svelte/store';

function createLocation() {
	const { subscribe, set, update } = writable({ latitude: 39.923152, longitude: -83.810306 });

	const success = (pos: GeolocationPosition) => {
		const crd = pos.coords;
		set({ latitude: crd.latitude, longitude: crd.longitude })
		console.log(crd)
	}

	const error = (err: GeolocationPositionError) => {
		console.warn(`ERROR(${err.code}): ${err.message}`);
	}

	return {
		subscribe,
		success,
		error
	};
}

export const locationStore = createLocation();