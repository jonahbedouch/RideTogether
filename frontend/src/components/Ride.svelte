<script lang="ts">
	import X from '../icons/X.svelte';
	import { backendStore } from '../stores/backend';
	let ride: boolean;

	backendStore.subscribe((value) => {
		ride = value.ride;
	});

    let close = () => {
        backendStore.toggleRide();
    }
</script>

<div class="flex flex-col text-baby-powder-50">
    <div
        class="absolute w-full h-full transition-transform z-10 bg-oxford-blue-900 overflow-hidden {ride
            ? ''
            : 'translate-y-full h-0'}">
        <div class="flex w-full m-4 align-middle items-center justify-center">
            <button class="mr-auto" on:click={close}>
                <X />
            </button>
            <p class="transition-none absolute self-center text-4xl">Ride</p>
        </div>
        <form action="" class="flex flex-col w-5/6 mx-auto">
            <label for="rideStartDestination">Start Destination</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-2 rounded-xl" id="rideStartDestination" name="rideStartDestination" type="text" />
            <label for="rideEndDestination">End Destination</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-2 rounded-xl" id="rideEndDestination" name="rideEndDestination" type="text" />
            <label for="passengerCnt">Number of Passengers Joining</label>
            <input class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 mb-6 rounded-xl" type="number" id="passengerCnt" name="passengerCnt"/>
            <button class="bg-oxford-blue-600 border-violet-red-700 border-2 p-2 rounded-xl text-xl">Start</button>
        </form>
    </div>
</div>
