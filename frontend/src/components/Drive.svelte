<script lang="ts">
	import { enhance } from '$app/forms';
	import { goto } from '$app/navigation';
	import X from '../icons/X.svelte';
	import { backendStore } from '../stores/backend';
	import { driveStore } from '../stores/drive';
	let drive: boolean;

	backendStore.subscribe((value) => {
		drive = value.drive;
	});

    let close = () => {
        backendStore.toggleDrive();
    }

    let submitEvent = () => {
        
    }

</script>

<div class="flex flex-row text-baby-powder-50">
    <div
        class="absolute w-full h-full transition-transform z-10 bg-oxford-blue-900 overflow-hidden {drive
            ? ''
            : 'translate-y-full h-0'}">
        <div class="flex w-full m-4 align-middle items-center justify-center">
            <button class="mr-auto" on:click={close}>
                <X />
            </button>
            <p class="transition-none absolute self-center text-4xl">Drive</p>
        </div>
        <form action="/app?/drive" on:submit|preventDefault method='POST' class="flex flex-col w-5/6 mx-auto" use:enhance={({form, data, cancel}) => {
            console.log(form, data, cancel);
            return async ({result}) => {
                console.log(result);
                if ('data' in result && result.data) {
                    console.log(result);
                    driveStore.replace(true, result.data.id, result.data.driver, result.data.passengers_max, result.data.start_dest, result.data.end_dest, result.data.original_route, result.data.passengers, result.data.timestamp);
                    backendStore.toggleDrive();
                    goto('/app/drive');
                }
            }
        }}>
            <label for="driveOrigin">Start Destination</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-2 rounded-xl" id="driveOrigin" name="driveOrigin" type="text" />
            <label for="driveDest">End Destination</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-2 rounded-xl" id="driveDest" name="driveDest" type="text" />
            <label for="maxPassengers">Number of Open Seats</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-6 rounded-xl" type="number" id="maxPassengers" name="maxPassengers" />
            <button class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 rounded-xl text-xl">Start</button>
        </form>
    </div>
</div>
