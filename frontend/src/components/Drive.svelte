<script lang="ts">
	import X from '../icons/X.svelte';
	import { backendStore } from '../stores/backend';
	let drive: boolean;

	backendStore.subscribe((value) => {
		drive = value.drive;
	});

    let close = () => {
        backendStore.toggleDrive();
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
        <form action="" class="flex flex-col w-5/6 mx-auto">
            <label for="driveStartDestination">Start Destination</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-2 rounded-xl" id="driveStartDestination" name="driveStartDestination" type="text" />
            <label for="driveEndDestination">End Destination</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-2 rounded-xl" id="driveEndDestination" name="driveEndDestination" type="text" />
            <label for="maxPassengers">Number of Open Seats</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-6 rounded-xl" type="number" />
            <button class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 rounded-xl text-xl">Start</button>
        </form>
    </div>
</div>
